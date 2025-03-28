from django import forms
from .models import Customer
from django.core.exceptions import ValidationError
import re

def validate_numeric(value):
    if not re.fullmatch(r'^\d+$',value):
        raise ValidationError('数字のみを入力してください。')
    
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name','representative_name','company_number','address','phone_number']
        widgets = {
            'name': forms.TextInput(
                attrs={
                'class':'form-control w-50',
                'placeholder': '名前を入力してください'
            }),
            'representative_name':forms.TextInput(attrs= {'class':'form-control w-50'}),
            'company_number':forms.TextInput(attrs= {'class':'form-control w-50'}),
            'address':forms.Textarea(attrs={'class':'form-control w-50','rows':3}),
            'phone_number':forms.TextInput(attrs= {'class':'form-control w-50'}),
        }
    
    # company_number = forms.CharField(validators=[validate_numeric])
    # phone_number = forms.CharField(validators=[validate_numeric])