from django.core.paginator import Paginator, InvalidPage, EmptyPage

def gerenciar_paginacao(request, object_list):
    paginator = Paginator(object_list, 10)
    try:
        page_num = int(request.GET.get('page', '1'))
    except ValueError:
        page_num = 1
    try:
        current_page = paginator.page(page_num)
    except (InvalidPage, EmptyPage):
        current_page = paginator.page(paginator.num_pages)
    return current_page