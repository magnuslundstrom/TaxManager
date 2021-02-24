from django.urls import path
from . import views
app_name = 'movements'

urlpatterns = [
    path('', views.index, name='movements'),
    path('create/', views.create, name='createMovements'),
    path('delete/', views.delete, name='deleteMovements'),
    path('item/<int:id>', views.displayItem, name='item')
]
