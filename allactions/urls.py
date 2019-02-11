from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.enter),
    path('<int:section_id>', views.send, name='section_page'),
]
