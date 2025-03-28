from django.shortcuts import get_object_or_404, redirect, render

from customer_management.sales.forms import SaleForm, SaleItemFormSet
from customer_management.sales.models import Sale

# Create your views here.
def sale_list(request):
    sales = Sale.objects.all()
    return render(request, 'sale/sale_list.html',{'sales':sales})

def sale_detail(request,pk):
    sale = get_object_or_404(Sale, pk=pk)
    return render(request,'sales/sale_detail.html',{'sale':sale})

def sale_create(request):
    if request.method == "POST":
        form = SaleForm(request.POST)
        formset = SaleItemFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            sale = form.save()
            items = formset.save(commit=False)
            for item in items:
                item.sale = sale
                item.save()
            return redirect('sale_list')
    else:
        form = SaleForm()
        formset = SaleItemFormSet()
    return render(request, 'sales/sale_form.html',{'form':form, 'formset':formset})

def sale_delete(request,pk):
    sale = get_object_or_404(Sale,pk)
    sale.delete()
    return redirect('sale_list')