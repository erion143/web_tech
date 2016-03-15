from django.core.paginator import Paginator
from django.shortcuts import render

def pagination(request, model, sorter=None, filters={}, baseurl='/?page='):
    if filters:
        pass
    elif sorter:
        mods = model.objects.order_by(sorter)
    else:
        mods = model.objects.all()
    limit = request.GET.get('limit', 10)
    try:
        limit = int(limit)
    except ValueError:
        limit = 10
    paginator = Paginator(mods, limit)
    page = int(request.GET.get('page', 1))
    if page > paginator.num_pages:
        page = paginator.num_pages
    paginator.baseurl = baseurl
    page = paginator.page(page)
    return render(request, 'base_pagin.html',
                  {'posts': page.object_list,
                   'paginator': paginator,
                   'page': page}
                  )
