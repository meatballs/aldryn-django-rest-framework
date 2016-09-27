# -*- coding: utf-8 -*-
from functools import partial

from aldryn_client import forms


class Form(forms.BaseForm):
    enable_rest_framework = forms.CheckboxField(
        'Enable Django REST Framework',
        required=False,
        initial=True,
    )

    def to_settings(self, data, settings):
        enable_rest_framework = data['enable_rest_framework']

        from aldryn_addons.utils import djsenv
        env = partial(djsenv, settings=settings)
        env_stage = '' if env('STAGE') is None else str(env('STAGE'))
        development_mode = True if env_stage in ['test', 'local'] else False

        settings['INSTALLED_APPS'].extend([
            'rest_framework',
        ])
        settings['ADDON_URLS'].append('aldryn_django_rest_framework.urls')
        settings['REST_FRAMEWORK'] = {
            'DEFAULT_PERMISSION_CLASSES': [
                'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
            ]
        }
        return settings
