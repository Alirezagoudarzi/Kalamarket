
# from django.urls import path,include
# from .views import login,register


# urlpatterns = [
#     path('login', login.as_view(), name='login'),
#     path('register', register.as_view(), name='register'),
# ]



from django.urls import path,include
from .views import login,register


urlpatterns = [
    path('login', login, name='login'),
    path('register', register, name='register'),
]
