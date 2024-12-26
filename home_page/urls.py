from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name="index"),
    path('suggestion/', views.suggestion_view, name='suggestion'),
    path('suggestion/received', views.suggestion_received_view, name='suggestion-received'),
    path('user/details', views.user_details_view, name='user-details'),
]
