from django.urls import path
from . import views


app_name = "main"

urlpatterns = [
    path('', views.home_view, name='home_view'),  #  empty path
    path('booking/trip/<trip_id>/' , views.booking_trip_view , name='booking_trip_view'),
    path('add/trip/' , views.add_trip_view , name='add_trip_view'),
    path('confirmation/page/' , views.confirmation_page , name='confirmation_page'),
    path('error/page/' , views.error_page_view , name='error_page_view'),
    path('payment/<int:trip_id>/' , views.payment_view , name='payment_view'),
    path("search/", views.search_view, name="search_view"),


]