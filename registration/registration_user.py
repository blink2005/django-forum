from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from user_extension.models import Extension
from recaptcha.check_recaptcha import CheckCaptcha

def registration_user(request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        result_captcha = CheckCaptcha().grecaptcha_verify(request)
        if result_captcha['success'] == True:
            if len(User.objects.filter(email=email)) == 0 and len(email) > 0:
                if len(User.objects.filter(username=username)) == 0 and len(username) > 0:
                    if len(password) > 2:
                        user = User.objects.create_user(username=username, email=email, password=password)
                        Extension.objects.create(user=user, photo='default.png')
                        login(request, authenticate(username=username, password=password))
                        return True
                    else:
                        return {'error': 'Пароль должен содержать больше 2 символов'}
                else:
                    return {'error': 'Данный username занят'}
            else:
                return {'error': 'Данный email занят'}
        else:
            return {'error': 'Капча не пройдена'}