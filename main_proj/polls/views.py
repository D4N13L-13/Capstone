from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Question, Choice


# Create your views here.
@login_required
def index(request):
    """
    The `index` function retrieves the latest questions from the
    database and renders them in a template called "poll.html".

    :param request: The `request` parameter in the `index` function is
        typically an HttpRequest object that represents the request made
        by a user to the server. It contains information about the
        request, such as the HTTP method used (GET, POST, etc.), request
        headers, user session data, and any data sent in
    :return: The `index` function is returning a rendered HTML template
        named "poll.html" along with the context data containing the
        latest question list to be displayed on the webpage.
    """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, "polls/poll.html", context)


@login_required
def detail(request, question_id):
    """
    This Python function retrieves a specific question object based on
    its ID and renders a detail template with the question data.

    :param request: The `request` parameter in the `detail` function is
        typically an HttpRequest object that represents the request made
        by a user to a web application. It contains information about
        the request, such as the HTTP method used (GET, POST, etc.),
        headers, user session data, and any data sent in
    :param question_id: The `question_id` parameter in the `detail`
        function is used to identify a specific question in the
        database. It is typically passed as an argument in the URL when
        a user  requests to view the details of a particular question
    :return: The function `detail` is returning a rendered HTML template
        named 'polls/detail.html' along with the context data containing
        the `question` object.
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


@login_required
def results(request, question_id):
    """
    The function `results` retrieves a specific question object and
    renders a template with the question data.

    :param request: The `request` parameter in the `results` function is
        typically an HttpRequest object that represents the current HTTP
        request. It contains information about the request made by the
        client, such as the request method, headers, and any data sent
        with the request. This parameter is commonly used in Django
        views to process
    :param question_id: The `question_id` parameter in the `results`
        function is used to identify the specific question for which the
        results are being displayed. It is typically passed as an
        argument in the URL when a user requests to view the results of
        a particular question in a web application
    :return: The function `results` is returning a rendered HTML
        template called 'results.html' along with the `question` object
        as context data.
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


@login_required
def vote(request, question_id):
    """
    The `vote` function in Python handles user voting for a specific
    question in a web application by incrementing the vote count for the
    selected choice.

    :param request: The `request` parameter in the `vote` function
        represents an HTTP request that is sent to the server when a
        user interacts with a web application. It contains information
        such as the user's input data, session details, and other
        metadata related to the request. In this context, the `request`
    :param question_id: The `question_id` parameter in the `vote`
        function is used to identify the specific question for which a
        user is voting. It is passed as an argument to the function and
        is used to retrieve the corresponding question object from the
        database. This ID is typically obtained from the URL or form
        data submitted
    :return: The `vote` function is returning an HTTP response redirect
        to the 'polls:results' URL with the `question_id` as an
        argument. This redirect is performed after processing the user's
        vote choice and updating the vote count for the selected choice.
    """
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(
            pk=request.POST['choice']
        )
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(
            reverse('polls:results', args=(question_id,))
        )
