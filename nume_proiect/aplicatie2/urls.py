from django.urls import path

from aplicatie2 import views

app_name = 'companies'

urlpatterns = [
    path('', views.CompanyView.as_view(), name='lista_companii'),
    path('adaugare/', views.CreateCompanyView.as_view(), name='add'),
    path('<int:pk>/update/', views.UpdateCompanyView.as_view(), name='modifica'),
    path('<int:pk>/delete/', views.delete_company, name='sterge'),
    path('<int:pk>/activeaza/', views.activate_company, name='activeaza'),
    path('companii_inactive', views.CompanyInactiveView.as_view(), name='companii_inactive'),
]
