from django.urls import path

from . import views

app_name = 'planner'
urlpatterns = [
    path('<int:year>/<int:month>/', views.month, name='month'),
    path('<int:year>/<int:month>/<int:day>/', views.day, name='day'),
    path('<int:year>/<int:month>/<int:day>/add',
         views.add_event, name='add_event'),
    path('<int:year>/<int:month>/<int:day>/delete',
         views.delete_event, name='delete_event'),
]
