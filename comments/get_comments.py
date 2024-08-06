from comments.models import Comment
from django.contrib.auth.models import User


def get_comments(request, id):
    comment_user = []
    for i in Comment.objects.filter(post_id=id):
        comment_user.append({'user_comment': User.objects.get(id=i.id_creator), 'message': i.message})
    return comment_user
    