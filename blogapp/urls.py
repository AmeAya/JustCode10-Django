from django.urls import path
from .views import *

# path('<Роут маршрут>', <Имя вашей вьюшки>.as_view(), name='<Внутреннее имя для маршрута>'),
urlpatterns = [
    path('posts', PostListView.as_view(), name='post_list_url'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail_url'),
    path('post/create', PostCreateView.as_view(), name='post_create_url'),
]
