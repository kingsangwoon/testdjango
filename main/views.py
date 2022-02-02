from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from django.utils import timezone
from .forms import QuestionForm

def index(request):
    question_list = Question.objects.order_by('-date')
    context = {'question_list': question_list}
    return render(request, 'main/question_list.html', context)


def detail(request, question_id):

    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'main/question_detail.html', context)


def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'),date=timezone.now())
    return redirect('main:detail', question_id=question.id)


def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.date = timezone.now()
            question.save()
            return redirect('main:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'main/question_form.html', context)