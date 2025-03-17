from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime


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
