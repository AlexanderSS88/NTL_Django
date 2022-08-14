from django.shortcuts import render
from django.core.paginator import Paginator
from datetime import datetime
from .models import Book


def books_view(request):
    template = 'books/books_list.html'
    objects_books = Book.objects.all()
    context = {'books': objects_books}
    return render(request, template, context)

def pub_date(request, pub_date_url: datetime):
    date_request = datetime.date(pub_date_url)
    template = 'books/books_list.html'
    objects_all_books_sorted = Book.objects.order_by('pub_date')
    objects_filtred_books = objects_all_books_sorted.filter(pub_date=pub_date_url)
    date_list = []
    [date_list.append(book.pub_date) for book in objects_all_books_sorted]
    number = len(date_list)
    previous, next = '', ''
    if date_request == date_list[number-1]:
        previous = date_list[number-2]
    elif date_request == date_list[0]:
        next = date_list[1]
    else:
        num = ''
        for id, position in enumerate(date_list):
            if date_request == position:
                num = id
        next = date_list[num+1]
        previous = date_list[num-1]
    context = {'books': objects_filtred_books,
               'next': str(next),
                'previous': str(previous)
               }
    return render(request, template, context)

