from django.shortcuts import render,redirect
from .models import User,PasswordReset
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from hostel.views import home

# Create your views here.
def profile(request):
    context={   
        'user':User.objects.all()
    }
    return render(request, 'profile.html')
def loginView(request):
    if request.method=='POST':
        username=request.POST.get('username')        
        password=request.POST.get('password')

        user=authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
        
    return render(request, 'login.html')

def logoutView(request):
    logout(request)
    return redirect(home)

def signup(request):
    if request.method=='POST':

        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        username=request.POST.get('username')

        user_data_has_error=False

        #validate email
        if User.objects.filter(email=email).exists():
            user_data_has_error=True
            messages.error(request, 'Email already exists')

        #validate username
        if User.objects.filter(username=username).exists():
            user_data_has_error=True
            messages.error(request, 'Username already exists')
        
        #vallidate password matching
        if password != confirm_password:
            user_data_has_error=True
            messages.error(request, 'passwords do not match')

        #validate password length
        if len(password)<5:
            user_data_has_error=True
            messages.error(request, 'password is too short')


        #create user if no error is found
        if user_data_has_error:
            return redirect('signup')
        else:
            User.objects.create_user(

                first_name=first_name,
                last_name=last_name,
                phone=phone,
                email=email,
                password=password,
                username=username,

            )
            messages.success(request, 'Account created succesfully, Login now')
            return redirect('login')

    return render(request, 'signup.html')


def forgot_password(request):
    if request.method=='POST':
        email=request.POST.get('email')

        try:
            user=User.objects.get(email=email)
            new_password_reset=PasswordReset(user=user)
            new_password_reset.save()

            password_reset_url = reverse('reset_password', kwargs={'reset_id': new_password_reset.reset_id})
            full_password_reset_url=f'{request.scheme}://{request.get_host()}{password_reset_url}' 
            email_body=f'Reset your password using this link: \n\n\n\n{full_password_reset_url}'
            email_message=EmailMessage(
                'Reset your password',
                email_body,
                settings.EMAIL_HOST_USER,
                [email] 
        )
            email_message.fail_silently=True
            email_message.send()

            return redirect('password_reset_sent', reset_id=new_password_reset.reset_id)

        except User.DoesNotExist:
            messages.error(request, f'No user with {email} found')
            return redirect('forgot_password')
        
        
    return render(request, 'forgot_password.html')

def reset_password_sent(request, reset_id ):
    if PasswordReset.objects.filter(reset_id=reset_id).exists():
        return render(request, 'password_reset_sent.html')
    else:
        messages.error(request, 'Invalid reset_id')
        return redirect('forgot_password')
    
    return render(request, 'password_reset_sent.html')

def reset_password(request, reset_id):

    try:
        password_reset_id=PasswordReset.objects.get(reset_id=reset_id)

        if request.method=="POST":
            password=request.POST.get('password')
            confirm_password=request.POST.get('confirm_password')

            password_has_error=False

            #vallidate password matching
            if password != confirm_password:
                password_has_error=True
                messages.error(request, 'passwords do not match')

            #validate password length
            if len(password)<5:
                password_has_error=True
                messages.error(request, 'password is too short') 

            #making sure that reset_id has not expired
            expiration_time=password_reset_id.created_when + timezone.timedelta(minutes=10)
            if timezone.now()>expiration_time:
                password_has_error=True
                messages.error(request, 'Reset link has expired')

                password_reset_id.delete()

            if not password_has_error:
                user=password_reset_id.user
                user.set_password(password)
                user.save()

                #delet reset_id
                password_reset_id.delete()

                #redirect to login
                messages.success(request, 'Password reset succesfully, Proceed to login')
                return redirect('login')
            

            else:
                #redirect to password reset page if any error is later detected
                return redirect('reset_password', reset_id=reset_id)
        return render(request, 'reset_password.html', {'reset_id':reset_id})


    except PasswordReset.DoesNotExist:
        messages.error(request, 'Invalid reset Id')
        return redirect('forgot_password')

def contact(request):
    return render(request, 'contact.html')

