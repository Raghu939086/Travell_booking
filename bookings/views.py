from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.http import JsonResponse
from django.urls import reverse
from .models import TravelOption, Booking
from django.contrib.auth import logout
from django.views.decorators.http import require_POST
from .forms import RegisterForm, ProfileUpdateForm, BookingForm


class CustomLoginView(LoginView):
    template_name = "login.html"

    def is_ajax(self):
        val = self.request.headers.get("x-requested-with")
        print("AJAX header received:", val)  
        return val == "XMLHttpRequest"

    def dispatch(self, *args, **kwargs):
        print("Request headers on dispatch:", self.request.headers) 
        return super().dispatch(*args, **kwargs)

    def form_invalid(self, form):
        if self.is_ajax():
            errors = form.errors.as_json()
            print("Form invalid errors JSON:", errors)  # Debug print errors JSON
            return JsonResponse({"success": False, "errors": errors}, status=400)
        messages.error(self.request, "Invalid username or password.")
        return super().form_invalid(form)

    def form_valid(self, form):
        login(self.request, form.get_user())
        redirect_url = self.get_success_url()
        if self.is_ajax():
            print("Form valid: sending success JSON with redirect URL:", redirect_url)
            return JsonResponse({"success": True, "redirect_url": redirect_url})
        return redirect(redirect_url)


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)   
            return redirect("travel_list")
    else:
        form = RegisterForm()
    return render(request, "registration.html", {"form": form})


@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect("profile")
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, "profile.html", {"form": form})


@login_required
def travel_list(request):
    travels = TravelOption.objects.all()
    travel_type = request.GET.get("type")
    source = request.GET.get("source")
    destination = request.GET.get("destination")
    date = request.GET.get("date")

    if travel_type and travel_type != "All":
        travels = travels.filter(type=travel_type)
    if source:
        travels = travels.filter(source__icontains=source)
    if destination:
        travels = travels.filter(destination__icontains=destination)
    if date:
        travels = travels.filter(date_time__date=date)

    return render(request, "travel_list.html", { 
        "travels": travels,
        "selected_type": travel_type,
        "source": source,
        "destination": destination,
        "date": date,
    })


@login_required
def book_travel(request, travel_id):
    travel = get_object_or_404(TravelOption, pk=travel_id)
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            num_seats = form.cleaned_data["num_seats"]
            if num_seats > travel.available_seats:
                messages.error(request, "Not enough seats available")
            else:
                total_price = num_seats * travel.price
                Booking.objects.create(
                    user=request.user,
                    travel_option=travel,
                    num_seats=num_seats,
                    total_price=total_price,
                    status="Confirmed"  # Explicitly set status here
                )
                travel.available_seats -= num_seats
                travel.save()
                messages.success(request, "Booking successful!")
                return redirect("my_bookings")
    else:
        form = BookingForm()

    return render(request, "booking.html", {"form": form, "travel": travel})


@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, "my_bookings.html", {"bookings": bookings})


@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id, user=request.user)
    booking.status = "Cancelled"
    booking.save()
    messages.success(request, "Booking cancelled successfully!")
    return redirect("my_bookings")


