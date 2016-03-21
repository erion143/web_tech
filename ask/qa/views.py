from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET, require_POST

from django.http import HttpResponse, HttpResponseRedirect

from models import Question, Answer
from pagination import pagination
from forms import AskForm, AnswerForm

def test(request, *args, **kwargs):
    return HttpResponse('OK')

@require_GET
def base(request, *args, **kwargs):
    posts = Question.objects.all()
    return render(request, 'base.html',
                  {'posts': posts[1:10]}
                  )

@require_GET
def base_pagin(request, *args, **kwargs):
    form = AskForm()
    paginator, page = pagination(request, Question,
                                 sorter='-added_at')
    return render(request, 'base_pagin.html',
                  {'posts': page.object_list,
                   'paginator': paginator,
                   'page': page,
                   'form':form}
                  )

@require_GET
def base_popular(request, *args, **kwargs):
    paginator, page =  pagination(request, Question,
                                  sorter='-rating',
                                  baseurl='/popular/?page=')
    return render(request, 'base_pagin.html',
                  {'posts': page.object_list,
                   'paginator': paginator,
                   'page': page})

def post_details(request, slug=0, *args, **kwargs):
    if request.method == 'POST':
        add_answer(request)
    question = get_object_or_404(Question, id=slug)
    answers = Answer.objects.filter(question_id=question.id)
    form = AnswerForm(initial={'question': question.id})
    return render(request, 'one_post.html',
                  {'post': question,
                   'answers': answers[:],
                   'form': form,}
                  )

def test_action(request):
    return HttpResponse(str(request.body))


def add_action(request):
    if request.method == 'POST':
        return add_question(request)
    else:
        return add_question_field(request)

@require_GET
def add_question_field(request):
    form = AskForm()
    return render(request, 'ask_form.html',
                  {'form': form})

@require_POST
def add_question(request):
    form = AskForm(request.POST)
    if form.is_valid():
        question = form.save()
        url = question.get_url()
        return HttpResponseRedirect(url)
    else:
        return HttpResponseRedirect(r'/')

@require_POST
def add_answer(request):
    f = open('req.log', 'a')
    form = AnswerForm(request.POST)
    f.write('form is created\n')
    if form.is_valid:
        f.write('form is valid\n')
        f.close()
        answer = form.save()
        url = answer.get_url()
        f = open('req.log', 'a')
        f.write('url = %s\n' % url)
        f.close()
        return HttpResponseRedirect(url)
    else:
        pk = form.question
        url = '/question/%s/' % pk
        f.close()
        return HttpResponseRedirect(url)

