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
        rest_framework_permissions = data['rest_framework_permissions']

        if enable_rest_framework:
            settings['INSTALLED_APPS'].extend([
                'rest_framework',
            ])
            settings['ADDON_URLS'].append('aldryn_django_rest_framework.urls')
        return settings
