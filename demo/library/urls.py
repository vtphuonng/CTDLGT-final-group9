from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('signup/', views.signup_user, name='signup'),
    path('record/<str:pk>', views.book_record, name='record'),
    path('delete_book/<str:pk>', views.delete_book, name='delete_book'),
    path('add_book/', views.add_book, name='add_book'),
    path('update/<str:pk>', views.update, name='update'),
]
