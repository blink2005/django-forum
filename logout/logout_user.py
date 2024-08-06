from django.contrib.auth import logout

def logout_user(request):
    logout(request)