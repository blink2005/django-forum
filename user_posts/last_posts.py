from user_posts.models import UserPost


def last_posts(id):
    return UserPost.objects.filter(user=id).order_by('-id')