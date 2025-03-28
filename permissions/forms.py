from django import forms
from .models import ScreenPermission

class ScreenPermissionForm(forms.ModelForm):
    class Meta:
        model = ScreenPermission
        fields = ['user', 'screen_name', 'can_access']
    