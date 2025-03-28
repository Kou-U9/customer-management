from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import FileResponse, Http404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView,UpdateView,DeleteView

from .models import Order
from .utils import generate_order_pdf
# Create your views here.

class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'orders/order_list.html'
    context_object_name = 'orders'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

class OrderCreateView(CreateView):
    model = Order
    template_name ='orders/order_form.html'
    fields = ['customer', 'product', 'quantity', 'order_date']
    success_url = reverse_lazy('orders:order_list')

class OrderUpdateView(UpdateView):
    model = Order
    template_name = 'orders/order_form.html'
    fields = ['customer', 'product', 'quantity', 'order_date']
    success_url = reverse_lazy('orders:order_list')

class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'orders/order_confirm_delete.html'
    success_url = reverse_lazy('orders:order_list')

class OrderPdfView(View):
    def get(self, request, pk):
        try:
            order = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404("Order not found")
        
        pdf = generate_order_pdf(order)
        return FileResponse(pdf, as_attachment=True,filename=f"order_{order.id}.pdf")