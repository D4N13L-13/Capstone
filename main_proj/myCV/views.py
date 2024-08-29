from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def myCV(request):
    """
    This Python function is decorated with `@login_required` and renders
    a template called "myCV.html" when called.

    :param request: The `request` parameter in the `myCV` function is an
    object that contains information about the current HTTP request,
    including details such as the user making the request, any data
    being sent with the request, and other metadata related to the
    request. This object is typically passed to view functions in Django
    :return: The function `myCV` is returning a rendered template
    `myCV.html` in response to the request.
    """
    return render(request, "myCV.html")
