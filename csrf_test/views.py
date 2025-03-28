from django.shortcuts import render,redirect
from .forms import CommentForm
from .models import Comment
from django.views.decorators.csrf import csrf_exempt

def post_comment(request):
    if request.method == "post":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('comment_list')
    else:
        form = CommentForm()

    return render(request, 'csrf_test/post_comment.html',{'form': form})

def comment_list(request):
    comments = Comment.objects.all()
    return render(request, 'csrf_test/comment_list.html', {'comments': comments})

# Create your views here.
