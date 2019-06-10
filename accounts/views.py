from django.shortcuts import render, redirect, HttpResponse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegisterUserForm
from takeaway_app.views import index

    
@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, "You have logged out")
    return redirect(index)
    
def login(request):
    if request.method == 'POST':
        # extract the user name from the form
        form_username = request.POST.get('username')
        # extract the password from the form
        password = request.POST.get('password')
        # then we check if the user name and password are correct 
        # i.e if both exists in the database
        user = auth.authenticate(username=form_username, password=password)
        # if user is not None, then redirect
        if user is not None:
            # actually logs in the user
            auth.login(user=user, request=request)
            messages.success(request, "Welcome back")
            return redirect(index)
        else:
            messages.error(request, "Invalid Login")
            return redirect(index)
    else:
        login_form = LoginForm()
        return render(request, 'login.html', {
            'form':login_form
        })
 
 
def register(request):
    if request.method == "POST":
        # process the creation
        # recreate the form with whatever data the user has keyed in
        register_form = RegisterUserForm(request.POST)
         # check if the form is valid
        if register_form.is_valid():
            # save the user
            register_form.save()
            # will show the message after the redirect
            messages.success(request, "Your account has been created!")
            return redirect(login)
        else:
            messages.error(request, "Unable to register your account")
            return render(request, 'register.html', {
              'form':register_form
            })
    else:
        register_form = RegisterUserForm()
        return render(request, 'register.html', {
            'form':register_form
        })