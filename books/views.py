from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from datetime import datetime
from . import models

def book_list(request):
    if request.method == 'GET':
        query = models.BookModel.objects.all().order_by('-id')
        return render(request, 'book.html', {'query': query })

def book_detail(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(models.BookModel, id=id)
        return render(request, 'book_detail.html', {'book_id': book_id})

def about_me(request):
    if request.method == 'GET':
        return HttpResponse(' Меня зовут Василиса, учусь на направлении Backend')


def pet_name(request):
    if request.method == 'GET':
        return HttpResponse(
            " <img src='https://www.osh.by/wp-content/uploads/2023/12/1041436899_0_206_2905_1840_1920x0_80_0_0_c7022893b761781d76fe592010d14bd2.jpg'/> Его имя Мурзик")


def system_time(request):
    current_time = datetime.today()
    return HttpResponse(current_time)
