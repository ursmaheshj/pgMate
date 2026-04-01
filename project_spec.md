# Project Specification: PG-Direct Management System

## 1. Project Overview
Build a two-sided marketplace using **Python Django** where PG (Paying Guest) Owners can list accommodations and Students/Seekers can browse and apply for them.

## 2. Core Tech Stack
- **Backend:** Django 5.0+
- **Database:** SQLite (Default for development)
- **Frontend:** HTML5, CSS3, Bootstrap 5 (Responsive UI)
- **Icons:** FontAwesome CDN

## 3. User Roles & Authentication
- **Custom User Model:** Extend `AbstractUser` to include a `user_role` field.
    - `is_manager`: Can Add/Edit/Delete PG listings and view applications.
    - `is_seeker`: Can browse listings, search by city, and submit applications.

## 4. Database Schema (Models)
### Table: PGListing
- `owner`: ForeignKey to User
- `pg_name`: CharField
- `description`: TextField
- `city`: CharField (e.g., Pune, Mumbai)
- `address`: TextField
- `price_per_month`: DecimalField
- `rooms_available`: IntegerField
- `amenities`: JSONField or multiple BooleanFields (WiFi, AC, Food, Laundry)
- `image`: ImageField (upload_to='pg_images/')

### Table: Application
- `pg`: ForeignKey to PGListing
- `applicant`: ForeignKey to User
- `status`: CharField (Choices: Pending, Approved, Rejected)
- `applied_on`: DateTimeField

## 5. Required Features & Views
### For Managers:
- **Dashboard:** Show all active listings and a count of "Pending Applications."
- **Manage Listing:** Create, Update, and Delete PG details.
- **Application Review:** List of students who applied; buttons to "Approve" or "Reject."

### For Seekers:
- **Home/Search:** A landing page with a search bar for "City" and price filters.
- **Listing Gallery:** Responsive Bootstrap cards showing PG images and prices.
- **Application Portal:** A simple "Apply Now" button that creates a record in the Application table.

## 6. UI/UX Requirements (Responsive)
- **Navbar:** Dynamic links (Login/Register for guests, Dashboard/Add PG for Managers).
- **Cards:** Use Bootstrap `.card` classes with hover effects for PG listings.
- **Mobile First:** Ensure the search bar and tables stack vertically on mobile.

## 7. Development Steps for Agent
1. Initialize Django project and `listings` app.
2. Create `CustomUser` model and register in `settings.py`.
3. Define `PGListing` and `Application` models with proper relationships.
4. Set up `Media` root for image uploads.
5. Create Class-Based Views (CBVs) for CRUD operations.
6. Design `base.html` with Bootstrap 5 CDN and navigation.
7. Build the `index.html` (Search/Gallery) and `dashboard.html`.