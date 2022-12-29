from django.urls import path

from . import views

app_name = 'planner'
urlpatterns = [
    path('<int:year>/<int:month>/', views.month, name='month'),
    path('<int:year>/<int:month>/<int:day>/', views.day, name='day'),
]
