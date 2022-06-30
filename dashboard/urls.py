from django.urls import path
from .views import DashboardHomeView,NewslettersDashboardHomeView,NewslettersCreateView, NewsletterDetailView

app_name ='dashboard'
urlpatterns =[
    path('',DashboardHomeView.as_view(), name='home'),
    path('list/',NewslettersDashboardHomeView.as_view(), name='list'),
    path('create/',NewslettersCreateView.as_view(), name='create'),
    path('detail/<int:pk>/',NewsletterDetailView.as_view(), name='detail'),
]