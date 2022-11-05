from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404

# There’s also a get_list_or_404() function, which works just as get_object_or_404() – except using filter() instead of get(). It raises Http404 if the list is empty.

from .models import Question

# Create your views here.
# def index(request):
#   latest_question_list = Question.objects.order_by('-pub_date')[:5]
#   template = loader.get_template('polls/index.html')
#   context = { 'latest_question_list': latest_question_list }
#   # output = ', '.join([q.question_text for q in latest_question_list])
#   return HttpResponse(template.render(context, request))

# shortcut for view above
def index(request):
  latest_question_list = Question.objects.order_by('-pub_date')[:5]
  context = { 'latest_question_list': latest_question_list }
  return render(request, 'polls/index.html', context)

def detail(request, question_id):
  try:
    question = Question.objects.get(pk=question_id)
    # question = get_object_or_404(Question, pk=question_id) -> shortcut
  except Question.DoesNotExist:
    raise Http404("Question does not exist, from Karla")
  # return render(request, 'polls/detail.html', {'question': question})
  return HttpResponse("You are looking at questions %s" % question_id)

def results(request, question_id):
  response = "You are looking at the results of question %s"
  return HttpResponse(response % question_id)

def vote(request, question_id):
  return HttpResponse("You are voting on question %s" % question_id)
