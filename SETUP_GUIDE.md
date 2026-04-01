# PG-Direct: Two-Sided Marketplace for PG Accommodations

A comprehensive Django application for managing PG (Paying Guest) accommodations where PG owners can list properties and students/seekers can browse and apply.

## Features

### For PG Managers
- **Dashboard**: Overview of active listings and pending applications
- **Manage Listings**: Create, update, and delete PG listings
- **Application Review**: Review and manage applications from seekers
- **Amenity Management**: Add WiFi, AC, Food, Laundry amenities to listings

### For Seekers
- **Browse Listings**: View all available PG accommodations
- **Advanced Search**: Filter by city, price, and amenities
- **Application Tracking**: Track status of submitted applications
- **Profile Management**: Maintain personal profile

## Tech Stack
- **Backend**: Django 5.0+
- **Database**: SQLite (Default)
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Icons**: FontAwesome CDN
- **Image Handling**: Pillow

## Project Structure

```
pgMate/
├── manage.py
├── requirements.txt
├── db.sqlite3
├── pgMate/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── listings/
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── admin.py
│   └── tests.py
├── templates/
│   ├── base.html
│   ├── auth/
│   │   ├── register.html
│   │   ├── login.html
│   │   ├── profile.html
│   │   └── update_profile.html
│   └── listings/
│       ├── home.html
│       ├── listing_detail.html
│       ├── manager_dashboard.html
│       ├── create_listing.html
│       ├── update_listing.html
│       ├── delete_listing.html
│       ├── applications_list.html
│       ├── apply_listing.html
│       └── seeker_applications.html
├── static/
│   └── css/
├── media/
│   └── pg_images/
└── project_spec.md
```

## Setup Instructions

### 1. Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### 2. Installation

```bash
# Clone or navigate to the project directory
cd c:\Users\ADMIN\OneDrive\Desktop\NS_learning\Project\pgMate

# Create a virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Database Setup

```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create a superuser (admin)
python manage.py createsuperuser
# Follow prompts:
# Username: admin
# Email: admin@example.com
# Password: (set your password)
# User role: When prompted, enter 'manager' or 'seeker'
```

### 4. Run Development Server

```bash
python manage.py runserver
```

Access the application at: `http://localhost:8000`

Admin panel: `http://localhost:8000/admin`

## Usage Guide

### First Time Setup

1. **Create Admin Account**: Run `python manage.py createsuperuser` to create a superuser account
2. **Access Admin Panel**: Go to `/admin` and log in
3. **Create Sample Data**: Add some PG listings through the admin panel

### For PG Managers

1. **Register**: Go to `/register` and create an account with role "PG Manager"
2. **Add PG**: Click "Add PG" in the navigation
3. **Fill Details**: 
   - PG Name, Description
   - City, Address
   - Price per month
   - Number of rooms available
   - Select amenities (WiFi, AC, Food, Laundry)
   - Upload PG image
4. **Manage Applications**: 
   - Go to Dashboard
   - Review pending applications
   - Approve or Reject applications
   - View application statistics

### For Seekers

1. **Register**: Go to `/register` and create an account with role "Seeker"
2. **Browse**: Browse available PGs on the home page
3. **Search & Filter**: 
   - Search by city
   - Filter by price range
   - Select required amenities
4. **Apply**: Click "Apply Now" on a listing
5. **Track**: View "My Applications" to track application status

## Models

### CustomUser
- Extends Django's AbstractUser
- Fields: username, email, first_name, last_name, phone_number, profile_image, user_role
- Roles: 'manager' (PG Owner) or 'seeker' (Student/Applicant)

### PGListing
- owner (ForeignKey to CustomUser)
- pg_name, description, city, address
- price_per_month, rooms_available
- Amenities: has_wifi, has_ac, has_food, has_laundry
- image (ImageField)
- created_at, updated_at, is_active

### Application
- pg (ForeignKey to PGListing)
- applicant (ForeignKey to CustomUser)
- status: 'pending', 'approved', 'rejected'
- message (Optional)
- applied_on, updated_at

## Views (Class-Based Views)

### Authentication
- RegisterView: User registration
- CustomLoginView: User login
- CustomLogoutView: User logout
- ProfileView: View user profile
- UpdateProfileView: Update profile

### Listings
- HomeView: Browse and search listings
- ListingDetailView: View listing details
- ManagerDashboardView: Manager dashboard
- CreateListingView: Create new listing
- UpdateListingView: Update listing
- DeleteListingView: Delete listing

### Applications
- ApplicationListView: Managers view applications
- UpdateApplicationStatusView: Update application status
- ApplyListingView: Seekers apply to listings
- SeekerApplicationsView: Seekers view their applications

## URLs

### Authentication
- `/register/` - User registration
- `/login/` - User login
- `/logout/` - User logout
- `/profile/` - View profile
- `/profile/update/` - Update profile

### Home & Listings
- `/` - Home (Browse listings)
- `/listing/<id>/` - View listing details

### Manager
- `/dashboard/` - Manager dashboard
- `/listing/create/` - Create listing
- `/listing/<id>/update/` - Update listing
- `/listing/<id>/delete/` - Delete listing

### Applications
- `/applications/` - Managers: Review applications
- `/application/<id>/update-status/` - Update application status
- `/listing/<id>/apply/` - Seekers: Apply to listing
- `/my-applications/` - Seekers: View applications

## Admin Panel

Access Django admin at `/admin` with superuser credentials to:
- Manage users
- Manage PG listings
- Review applications
- View statistics

## Common Tasks

### Add a New PG Listing (as Manager)
1. Login as Manager
2. Click "Add PG" in navigation
3. Fill form with details
4. Upload image
5. Click "Create Listing"

### Apply for a PG (as Seeker)
1. Login as Seeker
2. Browse listings on home page
3. Click "View Details"
4. Click "Apply Now"
5. Optionally add a message
6. Submit application

### Review Applications (as Manager)
1. Go to Dashboard
2. Click "Applications"
3. See all applications for your listings
4. Use filters to sort
5. Click Approve/Reject buttons
6. Confirm action

## Troubleshooting

### Static files not loading
- Run: `python manage.py collectstatic`
- Check STATIC_ROOT and STATICFILES_DIRS in settings.py

### Images not uploading
- Ensure `createing media/pg_images/` directory exists
- Check MEDIA_ROOT in settings.py
- Ensure file permissions are correct

### Database errors
- Run: `python manage.py migrate`
- Clear old migrations if needed
- Delete db.sqlite3 and start fresh if necessary

### Import errors
- Ensure all packages in requirements.txt are installed
- Run: `pip install -r requirements.txt`
- Check Python path

## Production Deployment Checklist

- [ ] Set `DEBUG = False` in settings.py
- [ ] Set `ALLOWED_HOSTS` appropriately
- [ ] Use a production database (PostgreSQL recommended)
- [ ] Set `SECRET_KEY` to a secure value
- [ ] Enable HTTPS/SSL
- [ ] Use a production web server (Gunicorn, uWSGI)
- [ ] Set up proper static file serving (WhiteNoise, CDN)
- [ ] Configure environment variables for sensitive data
- [ ] Set up logging and error tracking
- [ ] Run security checks: `python manage.py check --deploy`

## Support & License

This is an educational project. For modifications or improvements, follow Django best practices.

## Future Enhancements

- Email notifications for application status updates
- Chat between managers and seekers
- Rating and review system
- Payment integration
- Tour booking system
- Video gallery for PGs
- Advanced analytics for managers
- Mobile app using React Native or Flutter

---

**Developed for PG accommodation management and student placement.**
