from django.contrib.auth import authenticate, login
from recaptcha.check_recaptcha import CheckCaptcha

def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    result_captcha = CheckCaptcha().grecaptcha_verify(request)
    if result_captcha['success'] == True:
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return True
        else:
            return {'error': 'Неверный Username или Password'}
    else:
        return {'error': 'Капча не пройдена'}