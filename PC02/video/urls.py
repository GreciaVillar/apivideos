from django.urls import path
from .views import TipoDeVideoListView, TipoDeVideoDetailView, AlquilerListView, AlquilerDetailView, ClienteListView, ClienteDetailView

app_name = 'video'

urlpatterns = [
    path('tipos-de-video/', TipoDeVideoListView.as_view(), name='tipo_de_video_list'),
    path('tipos-de-video/<int:tipo_video_id>/', TipoDeVideoDetailView.as_view(), name='tipo_de_video_detail'),
    path('alquileres/', AlquilerListView.as_view(), name='alquiler_list'),
    path('alquileres/<int:alquiler_id>/', AlquilerDetailView.as_view(), name='alquiler_detail'),
    path('clientes/', ClienteListView.as_view(), name='cliente_list'),
    path('clientes/<int:cliente_id>/', ClienteDetailView.as_view(), name='cliente_detail'),
]
