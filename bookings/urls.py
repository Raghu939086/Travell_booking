from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path("", views.register, name="register"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("accounts/login/", RedirectView.as_view(url="/login/")),
    path("profile/", views.profile, name="profile"),
    path("travel_list/", views.travel_list, name="travel_list"),
    path("book/<int:travel_id>/", views.book_travel, name="book_travel"),
    path("my-bookings/", views.my_bookings, name="my_bookings"),
    path("cancel/<int:booking_id>/", views.cancel_booking, name="cancel_booking"),
]
