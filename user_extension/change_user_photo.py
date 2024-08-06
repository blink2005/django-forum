from user_extension.models import Extension

def change_user_photo(request, id):
    handle_uploaded_file(request.FILES['file_upload'], id)
    new_photo = Extension.objects.get(user_id=id)
    new_photo.photo = f'{id}.png'
    new_photo.save()
    return True

def handle_uploaded_file(file, name):
    with open(f"frontend/static/avatars/{name}.png", "wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)