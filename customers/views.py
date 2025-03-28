from datetime import timezone
from django.shortcuts import render,redirect,get_object_or_404
from .models import Customer
from .forms import CustomerForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def customer_list(request):
    customers =Customer.objects.all()
    return render(request, 'customers/customer_list.html',{'customers':customers})

@login_required
def customer_list(request):
    username = request.user.username
    print(username)
    query = request.GET.get("q","")
    customers = Customer.objects.all()

    if query:
        customers = customers.filter(name__icontains=query)|customers.filter(phone_number__icontains=query)

    
    return render(request, "customers/customer_list.html",{"customers":customers,"query":query,'username':username})

def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'customers/customer_form.html',{'form':form})

def customer_update(request, pk):
    customer = get_object_or_404(Customer,pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm(instance=customer)
    return render(request,'customers/customer_form.html',{'form':form})

def customer_delete(request,pk):
    customer = get_object_or_404(Customer,pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')
    return render(request,'customers/customer_confirm_delete.html',{'customer':customer})


import csv
from django.http import HttpResponse

def export_customers_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="customers.csv"'


    writer = csv.writer(response)
    writer.writerow(["法人名","代表者名","法人番号","住所", "電話番号", "登録日", "更新日"])

    for customer in Customer.objects.all():
        writer.writerow([
            customer.name,
            customer.representative_name,
            customer.company_number,
            customer.address,
            customer.phone_number,
            customer.created_at.strftime("%Y/%m/%d"),
            customer.updated_at.strftime("%Y/%m/%d")
        ])
    
    return response


from django.http import JsonResponse

def import_customers(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']

        file_content = csv_file.read().decode('utf-8').splitlines()
        csv_reader = csv.reader(file_content)

        rows = []
        for row in csv_reader:
            rows.append(row)

        return JsonResponse({'rows':rows})
    return render(request, 'your_template.html')

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os


def customer_export_pdf(request):
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = 'attachment; filename="customer_list.pdf"'

    # PDFのキャンバスを作成
    pdf = canvas.Canvas(response, pagesize=letter)

    # 日本語フォントの登録（Windows用のパスに修正）
    font_path = os.path.abspath(os.path.join('static', 'fonts', 'ipaexg.ttf'))
    pdfmetrics.registerFont(TTFont('IPAexGothic', font_path))
    pdf.setFont("IPAexGothic", 12)
    pdf.drawString(200, 750, "顧客一覧")
    pdf.line(100, 745, 500, 745)  # ヘッダー線

    # テーブルのヘッダー
    y_position = 725
    headers = ["法人名", "代表者名", "法人番号", "住所", "電話番号"]
    x_positions = [100, 200, 300, 400, 500]

    for i, header in enumerate(headers):
        pdf.drawString(x_positions[i], y_position, header)

    # 顧客データの取得とPDFへの書き込み
    customers = Customer.objects.all()
    y_position -= 20  # 一行下に移動

    for customer in customers:
        pdf.drawString(100, y_position, customer.name)
        pdf.drawString(200, y_position, customer.representative_name)
        pdf.drawString(300, y_position, customer.company_number)
        pdf.drawString(400, y_position, customer.address)
        pdf.drawString(500, y_position, customer.phone_number)
        y_position -= 20

    pdf.showPage()
    pdf.save()
    return response

import json
def customer_bulk_update(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            customer_ids = data.get("ids", [])

            if not customer_ids:
                return JsonResponse({"error": "選択されたレコードがありません"}, status=400)

            # 例: 更新フィールド (適宜カスタマイズ)
            Customer.objects.filter(id__in=customer_ids).update(updated_at=timezone.now())

            return JsonResponse({"message": "一括更新が完了しました"})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "無効なリクエスト"}, status=400)

def base(request):
    return render(request,'customers/base.html')

def list_2(request):
    customers =Customer.objects.all()
    return render(request,'customers/customer_list_2.html',{'customers':customers})
