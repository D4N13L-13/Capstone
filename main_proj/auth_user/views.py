from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .forms import RegisterForm
from django.contrib.auth import logout as auth_logout

from .forms import LoginForm


# Creating views here.
def logout(request):
    """
    The `logout` function logs out the user and redirects them to the
    login page.

    :param request: The `request` parameter in the `logout` function is
        typically an object that represents the HTTP request made by a
        user. It contains information about the request such as the
        user's session, cookies, headers, and other data related to the
        request being processed by the server.
    In this context,
    the :return: The `logout` function is returning a redirect response to
    the 'login' URL after logging out the user.
    """
    auth_logout(request)
    return redirect('login')


def login(request):
    """
    The `login` function handles user authentication by processing a
    POST request with a login form and  redirecting to the home page
    upon successful login.

    :param request: The `request` parameter in the `login` function is
        typically an HttpRequest object that represents the current HTTP
        request. It contains information about the request made by the
        client to the server, such as the request method (GET, POST,
        etc.), user data, and other metadata.
    In this context,
    :return: The `login` function is returning a rendered template
    `login.html` with the form data if the request method is not POST.
    If the request method is POST and the form is valid, it will
    redirect to the 'home' page.
    """
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def register(request):
    """
    The `register` function handles user registration by processing form
    data, saving the user, and authenticating them if the form is valid.

    :param request: The `request` parameter in the `register` function
        is an object that contains information about the current HTTP
        request. It includes details such as the request method (GET,
        POST, etc.), user session data, form data, and more. In this
        context, the function is handling a registration form submission
    :return: The `register` function returns a rendered HTML template
        named 'register.html' along with a form object (either a blank
        form or a form with user input data) based on the request
        method. If the request method is POST and the form is valid, it
        saves the form data, authenticates the user, logs them in, and
        redirects them to the 'home' page. If the request method
    """
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            auth_login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def signup(request):
    """
    The `signup` function in Python returns a rendered `signup.html`
    template in response to a request.
    
    :param request: The `request` parameter in the `signup` function is
        typically an HttpRequest object that represents the request made
        by a user to the server. It contains information about the
        request, such as the user's browser details, session data, and
        any data sent in the request (e.g., form data)
    :return: The `signup` function is returning a rendering of the
        `signup.html` template in response to
        the `request`.
    """
    return render(request, 'signup.html')


def home(request):
    """
    The `home` function in Python returns a rendered response for the
    'home.html' template.

    :param request: The `request` parameter in the `home` function is
        typically an HttpRequest object that represents the request
        made by a user to access a particular view in a Django web
        application. It contains information about the request, such as
        the user's browser details, session data, and any data sent in
        the request
    :return: The `home` function is returning a rendering of the
        `home.html` template in response to the `request`.
    """
    return render(request, 'home.html')
