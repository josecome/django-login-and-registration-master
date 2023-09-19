from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect


class app_notifications:
    def send_email(request):
        subject = 'Password for Django app successfully changed'
        message = 'Password successfully changed for ' + request.POST['username'] + '. If is not you, change you password please!'
        from_email = 'djangoexample@example.com'
        if subject and message and from_email:
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('login.html')
        else:
            return HttpResponse('Make sure all fields are entered and valid.')
            
            
            
            
            
            
            
            