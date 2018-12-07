from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question,Choice
from django.urls import reverse


def index(request):

    question = Question.objects.order_by('pub_date')

    return render(request,'./index.html',{'question': question})


def detail(request, question_id):
    question = get_object_or_404(Question,pk = question_id)
    return render(request,'./detail.html',{'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question,pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST["choice"])
    except(KeyError, Choice.DoesNotExist):
        return render(request, './detail.html' , {
            'question': question,
            'error_message': 'You didnt select a choice'
        })
    else:
        selected_choice.vote += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:result',args = [question_id]))


def result(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request,'./result.html',{'question': question})


# Create your views here.
