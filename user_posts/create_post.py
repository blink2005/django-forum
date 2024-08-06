from user_posts.models import UserPost

def create_post(request):
    post_message = request.POST['post_message']
    if len(post_message) > 0:
        UserPost.objects.create(title=post_message, user=request.user.id)
    return True
