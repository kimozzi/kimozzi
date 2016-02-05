from django.conf.urls import url, include
from django.http import JsonResponse
from django.conf.urls import url
from blog.models import Post

def post_list(request):
    return JsonResponse({'posts' : []}, safe=False)

urlpatterns = [
    url(r'^posts/$', post_list, name='post_list')
]