from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuItemView, SingleMenuItemView, BookingViewSet

booking_routers = DefaultRouter()
booking_routers.register(r'tables', BookingViewSet)

urlpatterns = [
    path('menu/', MenuItemView.as_view()),
    path('menu/<int:pk>/', SingleMenuItemView.as_view()),
    path('bookings/', include(booking_routers.urls)),
]
