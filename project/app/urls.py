from .views import main_page
from django.urls import path

app_name = 'app'

urlpatterns = [
    path('', main_page)
]