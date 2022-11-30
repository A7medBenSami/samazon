from django import forms
from django.core.exceptions import ImproperlyConfigured
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from .settings import EDITORS
from .utils import recursive_update, key_from_configdict


class RichTextarea(forms.Textarea):
    template_name = 'django_richtexteditor/richtextarea.html'

    def __init__(self, attrs=None):
        editor = self.get_editor()
        if editor['name'] == 'ckeditor':
            if editor['version'] == 'v5':
                if editor['distribution'] == 'classic':
                    default_attrs = {'class': 'editor'}
                else:
                    default_attrs = {'style': 'display: none;'}

            if editor['version'] == 'v4':
                if editor['distribution'] == 'basic':
                    default_attrs = {'class': 'editor'}


        if attrs:
            if 'class' in default_attrs and 'class' in attrs:
                attrs['class'] = ' '.join([default_attrs['class'], attrs['class']])
            default_attrs.update(attrs)

        super().__init__(default_attrs)

    def get_context(self, name, value, attrs):
        context = {}
        context['widget'] = {
            'name': name,
            'is_hidden': self.is_hidden,
            'required': self.is_required,
            'value': self.format_value(value),
            'attrs': self.build_attrs(self.attrs, attrs),
            'editor': self.get_editor(),
            'template_name': self.template_name,
        }
        return context

    @property
    def media(self):
        CONFIG = self.build_editor_config()
        EDITOR = key_from_configdict(CONFIG)
        VERSION = key_from_configdict(CONFIG[EDITOR])
        DISTRIBUTION = key_from_configdict(CONFIG[EDITOR][VERSION])

        css = {'all' : []}
        if CONFIG[EDITOR][VERSION][DISTRIBUTION]['css']['front']['theme']:
            css['all'].append(CONFIG[EDITOR][VERSION][DISTRIBUTION]['css']['front']['theme'])
        if CONFIG[EDITOR][VERSION][DISTRIBUTION]['css']['front']['custom']:
            css['all'].append(CONFIG[EDITOR][VERSION][DISTRIBUTION]['css']['front']['custom'])

        js = []
        js += [CONFIG[EDITOR][VERSION][DISTRIBUTION]['js']['build']]
        if CONFIG[EDITOR][VERSION][DISTRIBUTION]['js']['init-config']:
            js += [CONFIG[EDITOR][VERSION][DISTRIBUTION]['js']['init-config']]
        js += [CONFIG[EDITOR][VERSION][DISTRIBUTION]['js']['init-script']]

        return forms.Media(css=css, js=js)

    def get_editor(self):
        CONFIG = self.build_editor_config()
        name = key_from_configdict(CONFIG)
        version = key_from_configdict(CONFIG[name])
        distribution = key_from_configdict(CONFIG[name][version])
        return {'name': name, 'version': version, 'distribution': distribution}

    def build_editor_config(self):

        # init dict keys
        EDITOR = None
        VERSION = None
        DISTRIBUTION = None

        # Based on User Config, we build our Default Editor Config
        DEFAULT_CONFIG = {}
        
        RICHTEXTEDITOR_CONFIG = getattr(settings, 'RICHTEXTEDITOR_CONFIG', {})
        if RICHTEXTEDITOR_CONFIG:

            EDITOR = key_from_configdict(RICHTEXTEDITOR_CONFIG)
            if EDITOR:
                if EDITOR in EDITORS:
            
                    VERSION = key_from_configdict(RICHTEXTEDITOR_CONFIG[EDITOR])
                    if VERSION:
                        if VERSION in EDITORS[EDITOR]:

                            DISTRIBUTION = key_from_configdict(RICHTEXTEDITOR_CONFIG[EDITOR][VERSION])
                            if DISTRIBUTION:
                                if DISTRIBUTION in EDITORS[EDITOR][VERSION]:

                                    DEFAULT_CONFIG = {
                                        EDITOR: {
                                            VERSION: {
                                                DISTRIBUTION: EDITORS[EDITOR][VERSION][DISTRIBUTION]
                                            }
                                        }
                                    }
                                    
                                    CONFIG = DEFAULT_CONFIG.copy()
                                    recursive_update(CONFIG, RICHTEXTEDITOR_CONFIG)
                                
                                else:
                                    raise ImproperlyConfigured(_(
                                        'Distribution "%s" of Editor "%s" is not supported.'
                                    ) % (DISTRIBUTION, EDITOR))
            
                            else:
                                DISTRIBUTION = 'classic' if VERSION == 'v5' else 'basic'
            
                        else:
                            raise ImproperlyConfigured(_(
                                'Version "%s" of Editor "%s" is not supported.'
                            ) % (VERSION, EDITOR))
            
                    else:
                        VERSION = 'v5'
                        DISTRIBUTION = 'classic'
            
                else:
                    raise ImproperlyConfigured(_(
                        'Editor "%s" is not supported.'
                    ) % (EDITOR))

            else:
                EDITOR = 'ckeditor'
                VERSION = 'v5'
                DISTRIBUTION = 'classic'

        else:
            EDITOR = 'ckeditor'
            VERSION = 'v5'
            DISTRIBUTION = 'classic'


        # Now, we build our final valid CONFIG Dict
        CONFIG = {
            EDITOR: {
                VERSION: {
                    DISTRIBUTION: EDITORS[EDITOR][VERSION][DISTRIBUTION]
                }
            }
        }

        return CONFIG


# class AdminRichTextareaWidget(forms.Textarea):
    # def __init__(self, attrs=None):
        # super().__init__(attrs={'class': 'vLargeTextField', **(attrs or {})})

    # @property
    # def media(self):
        # load assets for admin only
