
# connect installed app auth --> urls ===> myapp users
from django.urls import path, include
from .views import create_user, profile, logout_view

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', create_user, name='register'),  
    path('login/', profile, name='login'),
    path('logout/', logout_view, name='logout user')  
]
