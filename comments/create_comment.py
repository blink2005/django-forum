from comments.models import Comment


def create_comment(request, id):
    comment = request.POST['post_message']
    if len(comment) > 0:
        Comment.objects.create(message=comment, post_id=id, id_creator=request.user.id)
        return True