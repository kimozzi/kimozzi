from django.shortcuts import redirect, render, get_object_or_404
from blog.forms import PostForm, CommentForm
from blog.models import Post
from django.views.generic import DetailView
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'blog/index.html')


def post_list(request):
    post_list = Post.objects.all()
    return render(request, 'blog/post_list.html', {'post_list' : post_list})


def post_detail(request):
    post = Post.objects.get()
    return render(request, 'blog/post_detail.html')


class PostDetailView(DetailView):
    def get_object(self, queryset=None):
        # self.kwargs : year, month, day, pk
        # self.kwargs['year']
        return Post.objects.get(pk=self.kwargs['pk'])

# post_detail = DetailView.as_view(model=Post)
post_detail = PostDetailView.as_view()


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect('blog:post_detail', post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html',{
        'form' : form,
    })

def post_edit(request, pk):
    post =Post.objects.get(pk = pk)
    if request.method == 'POST':
        form =PostForm(request.POST, request.FILES, instance = post)
        if form.is_valid():
            post=form.save()
            return redirect('blog:post_detail', post.pk)
    else:
        form = PostForm(instance = post)
    return render(request, 'blog/post_form.html', {
        'form' : form,
    })

def comment_new(request, post_pk):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.post = Post.objects.get(pk = post_pk)
            comment.save()
            messages.debug(request, '새로운 댓글을 등록했습니다.')
            return redirect('blog:post_detail', post_pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {
        'form' : form,
    })

def comment_edit(request, post_pk, pk):
    comment = Comment.objects.get(pk = pk)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance = comment)
        if form.is_valid():
            form.save()
            return redirect('blog:post_detail', post_pk)
    else:
        form = CommentForm(instance = comment)
    return render(request, 'blog/comment_form.html', {
        'form' : form,
    })




post_detail = DetailView.as_view(model = Post)