# Travel Booking Application

## Project Overview

This is a Travel Booking web application built using **Python Django** framework.  
It allows users to view available travel options (flight, train, bus), perform bookings, and manage their existing bookings through a clean and responsive web interface.

---
## Features

- User registration, login, and logout using Django's authentication system.
- User profile management.
- Search and filter travel options by type, source, destination, and date.
- Booking system with seat availability validation and total price calculation.
- View current and past bookings with cancellation capability.
- Responsive and user-friendly frontend design using Django templates and CSS.
- Backend powered by MySQL database.



# Backend

- User management with:
  - Registration
  - Login and logout using Django’s built-in authentication
  - Profile information update

- Travel Options model with:
  - Travel ID
  - Type (Flight, Train, Bus)
  - Source and Destination
  - Date and Time
  - Price
  - Available seats

- Booking model includes:
  - Booking ID
  - User (Foreign Key)
  - Travel Option (Foreign Key)
  - Number of seats booked
  - Total price calculation
  - Booking date
  - Status (Confirmed, Cancelled)

- Validations including:
  - Seat availability checks
  - Basic input validation

- Search and filtering of travel options by type, source, destination, and date.

---

### Frontend

- User-friendly pages using Django templates.
- Views for:
  - User registration, login, and profile management.
  - Listing travel options with filters.
  - Booking form to select travel options and confirm.
  - Displaying current and past bookings, with cancellation feature.
- Responsive design for desktop and mobile devices.
- Styling with CSS (and optionally Bootstrap for faster development).
