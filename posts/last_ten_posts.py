from posts.models import Post

def last_ten_posts(request):
    return Post.objects.order_by('-id')[:5]