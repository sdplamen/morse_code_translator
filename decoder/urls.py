from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from decoder import views
from decoder.views import MorseMappingListCreate, MorseMappingRetrieveUpdateDestroy

urlpatterns = [
    # --- Web App Paths ---
    path('decoder/', views.morse_decoder_view, name='decoder'),
    path('encoder/', views.morse_encoder_view, name='encoder'),
    path('', views.morse_decoder_view, name='home'),
    path('api/morse_mappings/', MorseMappingListCreate.as_view(), name='morse-mapping-list-create'),
    path('api/morse_mappings/<int:pk>/', MorseMappingRetrieveUpdateDestroy.as_view(), name='morse-mapping-detail'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]