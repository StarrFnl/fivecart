from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from ..models import *
from django.db.models import Q

def index(request):
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')  # 검색어
    book_list = Book.objects.order_by("-book_date")
    if kw:
        book_list = book_list.filter(
            Q(title__icontains=kw) |  # 제목 검색
            Q(book_writer__book_writer__icontains=kw) |  # 저자 검색
            Q(company__company_name__icontains=kw)   # 출판사 검색
        ).distinct()

    paginator = Paginator(book_list, 30)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'book_list': page_obj, 'page':page, 'kw':kw }
    return render(request, 'fivecart/book_list.html', context)