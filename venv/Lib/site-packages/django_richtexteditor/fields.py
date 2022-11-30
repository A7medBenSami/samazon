from django.contrib.admin.widgets import AdminTextareaWidget
from django.db import models
from django.utils.translation import gettext_lazy as _

from .widgets import RichTextarea


class RichTextField(models.TextField):
    description = _("Rich Text")

    def formfield(self, **kwargs):
        defaults = {'widget': RichTextarea}
        defaults.update(kwargs)

        # override the admin widget
        if defaults['widget'] == AdminTextareaWidget:
            defaults['widget'] = RichTextarea

        return super().formfield(**defaults)

