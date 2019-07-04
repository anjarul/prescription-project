from django.urls import path
from django.contrib.auth.views import (

    login,
    logout,
)

# from .views import signup


app_name = 'user_auth'


urlpatterns = [

    # path('signup/', signup, name='signup'),

    path('login/', login,
         {'template_name': 'user_auth/login.html'}, name='login'),

    path('logout/', logout,
         {'template_name': 'user_auth/logout.html'}, name='logout'),

]
