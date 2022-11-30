"""Supported Editors"""
EDITORS = {
    'ckeditor': {
        'v5': {
            'balloon': {
                'css': {
                    'front': { 'theme': None, 'custom': None, },
                    'admin': { 'theme': None, 'custom': None, },
                },
                'js': {
                    'build': '//cdn.ckeditor.com/ckeditor5/15.0.0/balloon/ckeditor.js',
                    'init-config': None,
                    'init-script': 'js/django_richtexteditor/ckeditor/v5/balloon.js',
                },
            },
            'balloon-block': {
                'css': {
                    'front': { 'theme': None, 'custom': None, },
                    'admin': { 'theme': None, 'custom': None, },
                },
                'js': {
                    'build': '//cdn.ckeditor.com/ckeditor5/15.0.0/balloon-block/ckeditor.js',
                    'init-config': None,
                    'init-script': 'js/django_richtexteditor/ckeditor/v5/balloon-block.js',
                },
            },
            'classic': {
                'css': {
                    'front': { 'theme': None, 'custom': None, },
                    'admin': { 'theme': None, 'custom': None, },
                },
                'js': {
                    'build': '//cdn.ckeditor.com/ckeditor5/15.0.0/classic/ckeditor.js',
                    'plugins': [],
                    'init-config': None,
                    'init-script': 'js/django_richtexteditor/ckeditor/v5/classic.js',
                },
            },
            'decoupled-document': {
                'css': {
                    'front': { 'theme': None, 'custom': None, },
                    'admin': { 'theme': None, 'custom': None, },
                },
                'js': {
                    'build': '//cdn.ckeditor.com/ckeditor5/15.0.0/decoupled-document/ckeditor.js',
                    'init-config': None,
                    'init-script': 'js/django_richtexteditor/ckeditor/v5/decoupled-document.js',
                },
            },
            'inline': {
                'css': {
                    'front': { 'theme': None, 'custom': None, },
                    'admin': { 'theme': None, 'custom': None, },
                },
                'js': {
                    'build': '//cdn.ckeditor.com/ckeditor5/15.0.0/inline/ckeditor.js',
                    'init-config': None,
                    'init-script': 'js/django_richtexteditor/ckeditor/v5/inline.js',
                },
            },
        },
        'v4': {
            'basic': {
                'css': 'css/django_richtexteditor/ckeditor/v4/basic.css',
                'js': {
                    'build': '//cdn.ckeditor.com/4.13.0/basic/ckeditor.js',
                    'init-config': None,
                    'init-script': 'js/django_richtexteditor/ckeditor/v4/basic.js',
                },
            },
            'full': {
                'css': 'css/django_richtexteditor/ckeditor/v4/full.css',
                'js': {
                    'build': '//cdn.ckeditor.com/4.13.0/full/ckeditor.js',
                    'init-config': None,
                    'init-script': 'js/django_richtexteditor/ckeditor/v4/full.js',
                },
            },
            'full-all': {
                'css': 'css/django_richtexteditor/ckeditor/v4/full-all.css',
                'js': {
                    'build': '//cdn.ckeditor.com/4.13.0/full-all/ckeditor.js',
                    'init-config': None,
                    'init-script': 'js/django_richtexteditor/ckeditor/v4/full-all.js',
                },
            },
            'standard': {
                'css': 'css/django_richtexteditor/ckeditor/v4/standard.css',
                'js': {
                    'build': '//cdn.ckeditor.com/4.13.0/standard/ckeditor.js',
                    'init-config': None,
                    'init-script': 'js/django_richtexteditor/ckeditor/v4/standard.js',
                },
            },
            'standard-all': {
                'css': 'css/django_richtexteditor/ckeditor/v4/standard-all.css',
                'js': {
                    'build': '//cdn.ckeditor.com/4.13.0/standard-all/ckeditor.js',
                    'init-config': None,
                    'init-script': 'js/django_richtexteditor/ckeditor/v4/standard-all.js',
                },
            },
        },
    },
    'tinymce': {
        'v5': {
            'XXX': {
                'css': 'css/django_richtexteditor/tinymce/v5/XXX.css',
                'js': {
                    'build': '//cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js',
                    'init-script': 'js/django_richtexteditor/tinymce/v5/XXX.js',
                },
            },
        },
    },
}
