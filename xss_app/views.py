from django.shortcuts import render, redirect
from xss_app.models import Comment
from django.utils.safestring import mark_safe

# Create your views here.
def unsafe_xss_view(request):
    if request.method == "POST":
        content = request.POST.get("content","")
        Comment.objects.create(content=content)

    comments = Comment.objects.all()
    return render(request,"xss_app/unsafe_xss.html",{"comments": comments})