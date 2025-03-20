from django.urls import path
from . import views

urlpatterns = [

    path('book_list/', views.book_list),
    path('book_detail/<int:id>/', views.book_detail),

    path('about_me/', views.about_me),
    path('pet_name/', views.pet_name),
    path('system_time/', views.system_time)
]