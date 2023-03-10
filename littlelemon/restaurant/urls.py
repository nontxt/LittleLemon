from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import MenuItemView, SingleMenuItemView, BookingViewSet, index

booking_routers = DefaultRouter()
booking_routers.register(r'tables', BookingViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('menu/', MenuItemView.as_view(), name='menu'),
    path('menu/<int:pk>/', SingleMenuItemView.as_view(), name='menu'),
    path('bookings/', include(booking_routers.urls), name='bookings'),
    path('api-token-auth/', obtain_auth_token),
]
