from blog.models import Post
from django.http import JsonResponse
from django.conf.urls import url

def post_list(request):
    post_list = [post.title for post in Post.objects.all()]
    return JsonResponse([post_list], safe=False)


urlpatterns = [
    url(r'^posts/$', post_list)

]