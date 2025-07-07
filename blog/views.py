from django.shortcuts import render
from django.http import HttpResponse
from .models import Post 
from django.utils import timezone
# 必须添加这个index视图函数
def index(request):
    posts=Post.objects.all().order_by('-published_date')
    return render(request,'./blog/post_list.html',{'posts':posts})
    
    # 或者如果你想返回模板：
    # return render(request, 'blog/index.html')
# Create your views here.
