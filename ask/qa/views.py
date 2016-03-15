from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET

from django.http import HttpResponse

from models import Question, Answer
from pagination import pagination

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
    return pagination(request, Question,
                      sorter='-added_at')

@require_GET
def base_popular(request, *args, **kwargs):
    return pagination(request, Question,
                      sorter='-rating',
                      baseurl='/popular/?page=')

@require_GET
def post_details(request, slug=0, *args, **kwargs):
    post = get_object_or_404(Question, id=slug)
    answers = Answer.objects.filter(question_id=post.id)
    return render(request, 'one_post.html',
                  {'post': post,
                   'answers': answers[:]}
                  )
