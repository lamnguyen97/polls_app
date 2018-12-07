from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question,Choice
from django.urls import reverse
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'question'

    def get_queryset(self):
        return Question.objects.order_by('pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'detail.html'


class ResultView(generic.DetailView):
    model = Question
    template_name = 'result.html'

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




# Create your views here.
