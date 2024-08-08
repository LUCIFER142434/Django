# from django.urls import path
# from . import views

# urlpatterns = [
#     path('',views.text,name="text")
# ]


from django.urls import path
from . import views

urlpatterns = [
    path('',views.hello_world, name='hello')
]