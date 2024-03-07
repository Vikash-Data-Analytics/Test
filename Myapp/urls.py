from django.urls import path
from Myapp import views
urlpatterns = [

     path('user/', views.user.as_view(), name='user'),
]
