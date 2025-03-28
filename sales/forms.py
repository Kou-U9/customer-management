from django import forms
from django.forms import inlineformset_factory

from customer_management.sales.models import Sale, SaleItem

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        field = ['sale_date', 'customer_name']

SaleItemFormSet = inlineformset_factory(Sale, SaleItem,fields=('product_name', 'quantity','price'), extra=1)