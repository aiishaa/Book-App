
# connect installed app auth --> urls ===> myapp users
from django.urls import path, include
from .views import create_user, login_user, logout_view

urlpatterns = [
    path('register/', create_user, name='register'),  
    path('login/', login_user, name='login view'),
    path('logout/', logout_view, name='logout view')  
]
