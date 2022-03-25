from django.urls import path

from webapp.views import (
    home,
)


app_name = 'webapp'

urlpatterns = [
    # Home
    path('', home, name='home'),
]