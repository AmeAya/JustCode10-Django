from django.urls import path
from .views import *

# path('<Роут маршрут>', <Имя вашей вьюшки>.as_view(), name='<Внутреннее имя для маршрута>'),
urlpatterns = [
    path('posts', PostListView.as_view(), name='post_list_url'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail_url'),
    path('post/create', PostCreateView.as_view(), name='post_create_url'),
    path('post/update/<int:pk>', PostUpdateView.as_view(), name='post_update_url'),
    path('post/delete/<int:pk>', PostDeleteView.as_view(), name='post_delete_url'),

    path('flowers', FlowersView, name='flowers_url'),
    path('flower/<int:flower_id>', FlowersDetailView, name='flowers_detail_url'),
    path('create_flower', FlowerCreateView, name='flower_create_url'),
    path('flower_update/<int:flower_id>', FlowerUpdateView, name='flower_update_url'),

    path('bouquets', BouquetsView, name='bouquets_url'),
    path('bouquet/<int:bouquet_id>', BouquetsDetailView, name='bouquets_detail_url'),
    path('create_bouquet', BouquetsCreateView, name='bouquets_create_url'),

    path('music', musicView, name='music_url'),
]
