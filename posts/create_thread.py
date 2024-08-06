from posts.models import Post

def create_thread(request):
    title = request.POST['title']
    message = request.POST['message']
    Post.objects.create(category='category', title=title, description=message, id_creator=request.user.id)
    return True