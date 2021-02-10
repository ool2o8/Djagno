from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    if 'page' in request.GET:
        p = int(request.GET['page'])
        posts = posts[(p - 1) * 10, p * 10]
    #return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")    
    return render(request, 'blog\post_list.html', {'posts':posts})
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog\post_detail.html', {'post':post})