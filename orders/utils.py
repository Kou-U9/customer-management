from io import BytesIO
import os


from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors

def generate_order_pdf(order):
    buffer = BytesIO()
    p = canvas.Canvas(buffer,pagesize=A4)
    width, height = A4

    font_path = os.path.abspath(os.path.join('static', 'fonts', 'ipaexg.ttf'))
    pdfmetrics.registerFont(TTFont('IPAexGothic', font_path))

    # タイトルを中央に表示
    title = "受注伝票"
    p.setFont("IPAexGothic", 24)
    title_width = p.stringWidth(title,"IPAexGothic",24)
    x_title = (width - title_width) / 2
    y_title = height - 100
    p.drawString(x_title, y_title, title)
    
    # アンダーバー
    underline_y = y_title - 2
    p.setLineWidth(1)
    p.line(x_title,underline_y,x_title + title_width, underline_y)

    # 日付
    x_center = width / 2
    x_date = x_center + 100
    y_date = height - 50
    p.setFont("IPAexGothic",12)
    p.drawString(x_date, y_date, "日付")
    # 日付のアンダーバー
    p.setLineWidth(1)
    p.line(x_date, y_date - 2,x_date + 120, y_date - 2)

    # 受注番号
    x_order_num = x_center + 100
    y_order_num = height - 70
    p.setFont("IPAexGothic",12)
    p.drawString(x_order_num, y_order_num, "受注番号")
    # 受注番号のアンダーバー
    p.setLineWidth(1)
    p.line(x_order_num,y_order_num - 2, x_order_num + 120, y_order_num -2)

    # 顧客名
    x_name = 40 + 220
    y_name = height - 150
    p.setFont("IPAexGothic",12)
    p.drawString(x_name, y_name, "様")

    # 文章
    sentence = "下記の通り、確かに受注いたしました"
    x_sentence = 40
    y_sentence = height - 190
    p.setFont("IPAexGothic",12)
    p.drawString(x_sentence, y_sentence, sentence)

    # 件名
    subject = "件名："
    x_sub = 40
    y_sub = height - 220
    p.setFont("IPAexGothic",12)
    p.drawString(x_sub, y_sub, subject)
    # 件名のアンダーライン
    p.setLineWidth(1)
    p.line(x_sub,y_sub-2,x_sub + 300,y_sub-2)

    # 会社名
    company_name = "内田株式会社"
    x_company_name = x_center + 100
    y_company_name = height - 170
    p.setFont("IPAexGothic",12)
    p.drawString(x_company_name, y_company_name, company_name)

    # テーブル
    data = [
        ["項目", "内容", "数量", "受注日"],
        ["product 1","詳細", "10", "2025/3/19"],
        ["小計","","","100"]
    ]

    table = Table(data, colWidths=[200,200,50,70])
    table.setStyle(TableStyle([
        ('GRID',(0,0),(-1,-1),1,colors.black),
        ('FONTNAME',(0,0),(-1,0),'IPAexGothic'),
        ('FONTNAME',(0,1),(-1,-1),'IPAexGothic'),
        ('SPAN', (0, -1), (2, -1))  # 最後の行のセルを結合
        
    ]))
    table_x = 40
    table_y = height - 300
    table.wrapOn(p, width, height)
    table.drawOn(p, table_x, table_y)

    p.showPage()
    p.save()

    buffer.seek(0)

    return buffer