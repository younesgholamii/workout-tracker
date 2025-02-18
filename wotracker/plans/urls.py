from django.urls import path
from . import views


app_name = 'plans'
urlpatterns = [
    path('details/', views.PlansDetailView.as_view(), name='details')
]