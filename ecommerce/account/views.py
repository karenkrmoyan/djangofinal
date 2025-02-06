#
from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
#
from .forms import CreateUserForm, LoginForm
from .token import user_tokenizer_generate


def register(request):

    # - Creating an empty user form for further actions

    form = CreateUserForm()

    if request.method == "POST":

        # - Creating a form instance but this time we are passing data to it (username,
        #  password, email)

        form = CreateUserForm(request.POST)

        # - This checks if the form data is valid based on the rules defined in CreateUserForm class
        # - and then saves it to db.

        if form.is_valid():

            user = form.save()

            user.is_active = False

            user.save()

            # - Email verification setup (template)

            # - This retrives a current domain name of the site based on request object

            current_site = get_current_site(request)

            subject = "Account verification email"

            # - Creates a string from URL with the data: user object, current domain, 
            # - user's primary key and generates a unique token for him

            message = render_to_string("account/registration/email-verification.html",{

                    "user": user,
                    "domain": current_site.domain,
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "token": user_tokenizer_generate.make_token(user),

            })

            # - Sends an email to user for further confirmation

            user.email_user(subject=subject, message=message)



            return redirect("email-verification-sent")

        
    context = {"form": form}



    return render(request, "account/registration/register.html", context=context)



def email_verification(request, uidb64, token):

    # - Decoding user id 
    
    unique_id = force_str(urlsafe_base64_decode(uidb64))

    # - Getting user by his id 

    user = User.objects.get(pk=unique_id)

    # Success

    # - At first if statement checks that the user exists then 
    # - compares current token with the one that we generated earlier

    if user and user_tokenizer_generate.check_token(user, token):

        user.is_active = True

        user.save()

        return redirect("email-verification-success")
    
    else:

        return redirect("email-verification-failed")


def email_verification_sent(request):

    return render(request, "account/registration/email-verification-sent.html")


def email_verification_success(request):

    return render(request, "account/registration/email-verification-success.html")


def email_verification_failed(request):

    return render(request, "account/registration/email-verification-failed.html")




def my_login(request):
    
    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return redirect("dashboard")
            
    context = {"form": form}

    return render(request, "account/my-login.html", context=context)



def user_logout(request):

    auth.logout(request)

    return redirect("store")


# - Decorator ensures that the user is logged in before processing to dashboard page

@login_required(login_url="my-login")
def dashboard(request):

    return render(request, "account/dashboard.html")