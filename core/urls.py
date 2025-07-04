from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('certificate-pending/', views.certificate_pending, name='certificate_pending'),
     path('project-not-deployed/', views.not_deployed_view, name='not_deployed'),

]
