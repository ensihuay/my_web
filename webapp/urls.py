from django.urls import path

from webapp.views import (
    home,
    resumn_yu,
)


app_name = 'webapp'

urlpatterns = [
    # Home
    path('', home, name='home'),
    #resumn Yu
    path('resumn_yu', resumn_yu, name='resumn_yu'),
]