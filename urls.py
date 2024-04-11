from django.urls import path
from dataapp import views

urlpatterns = [
    path('',views.index,name='index'),
    path('person/',views.person,name='person'),
    path('person/', views.person, name='person'),
    path('form_view/', views.form_view, name='form_view'),
    path('delete/<int:person_id>/', views.delete, name='delete'),
    path('edit/<int:person_id>/', views.edit, name='edit'),
]