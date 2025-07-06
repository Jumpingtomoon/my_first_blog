from django.shortcuts import render
from django.http import HttpResponse

# 必须添加这个index视图函数
def index(request):
    return render(request,'./blog/post_list.html')
    
    # 或者如果你想返回模板：
    # return render(request, 'blog/index.html')
# Create your views here.
