# PG-Direct Project - Quick Start Guide

## 🚀 What's Been Created

Your complete PG-Direct Django application is ready! This is a two-sided marketplace where:
- **PG Managers** can list and manage their property accommodations
- **Seekers** can browse, search, and apply for available PGs

## 📁 Project Structure Overview

```
pgMate/
├── manage.py                          # Django management script
├── requirements.txt                   # Python dependencies
├── SETUP_GUIDE.md                    # Detailed setup instructions
├── db.sqlite3                        # Database (created after first run)
├── .gitignore                        # Git ignore rules
│
├── pgMate/                           # Main project settings
│   ├── settings.py                   # Django configuration
│   ├── urls.py                       # URL routing (updated with media serving)
│   ├── wsgi.py                       # WSGI configuration
│   └── asgi.py                       # ASGI configuration
│
├── listings/                         # Main app
│   ├── models.py                     # CustomUser, PGListing, Application
│   ├── views.py                      # Class-based views (20+ views)
│   ├── forms.py                      # Django forms for all features
│   ├── urls.py                       # URL patterns
│   ├── admin.py                      # Admin panel configuration
│   ├── apps.py                       # App configuration
│   └── tests.py                      # Test framework (ready to use)
│
├── templates/                        # HTML templates
│   ├── base.html                     # Base template with Bootstrap 5
│   ├── auth/                         # Authentication templates
│   │   ├── register.html             # User registration
│   │   ├── login.html                # User login
│   │   ├── profile.html              # View profile
│   │   └── update_profile.html       # Edit profile
│   └── listings/                     # Listing templates
│       ├── home.html                 # Home page with search
│       ├── listing_detail.html       # Individual listing details
│       ├── manager_dashboard.html    # Manager dashboard
│       ├── create_listing.html       # Create/update listing form
│       ├── delete_listing.html       # Delete confirmation
│       ├── applications_list.html    # Manager's application review
│       ├── apply_listing.html        # Apply to PG
│       └── seeker_applications.html  # View my applications
│
├── static/                           # Static files (CSS, JS, images)
│   └── css/                          # (Ready for custom CSS)
│
└── media/                            # User uploads
    └── pg_images/                    # PG images and profile pictures
```

## 50-Second Setup

```bash
# 1. Navigate to project
cd c:\Users\ADMIN\OneDrive\Desktop\NS_learning\Project\pgMate

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create database
python manage.py makemigrations
python manage.py migrate

# 5. Create admin user
python manage.py createsuperuser

# 6. Start server
python manage.py runserver
```

## 🌐 Access Points

After running `python manage.py runserver`:

| URL | Purpose |
|-----|---------|
| `http://localhost:8000/` | Home page (Browse PGs) |
| `http://localhost:8000/register/` | User registration |
| `http://localhost:8000/login/` | User login |
| `http://localhost:8000/admin/` | Admin panel |
| `http://localhost:8000/dashboard/` | Manager dashboard |
| `http://localhost:8000/my-applications/` | Seeker's applications |

## 👥 Key Features

### For PG Managers
✅ Create, read, update, delete PG listings  
✅ Add images and amenities (WiFi, AC, Food, Laundry)  
✅ Dashboard with statistics  
✅ Review and manage applications  
✅ Approve/reject seeker applications  

### For Seekers
✅ Browse all available PGs  
✅ Advanced search (city, price, amenities)  
✅ View detailed listing information  
✅ Apply to listings with optional message  
✅ Track application status  
✅ Profile management  

### Admin Panel Features
✅ Manage all users  
✅ View and moderate listings  
✅ Monitor applications  
✅ View system statistics  

## 🗄️ Database Models

### CustomUser
Extends Django's built-in User model
- Fields: username, email, first_name, last_name, phone, role, profile_image
- Roles: 'manager' or 'seeker'

### PGListing
PG accommodation listings
- Fields: owner, name, description, city, address, price, rooms, image
- Amenities: WiFi, AC, Food, Laundry (boolean fields)
- Timestamps: created_at, updated_at

### Application
Application from seeker to PG
- Fields: applicant, pg, status, message, timestamps
- Status: Pending, Approved, Rejected
- Unique constraint on (applicant, pg) pair

## 📝 How to Use

### Step 1: Create Test Accounts

**Option A: Via Registration Page**
- Go to `/register/`
- Fill form with Manager or Seeker role
- Login with credentials

**Option B: Via Admin Panel**
- Go to `/admin/` with superuser account
- Create users with different roles

### Step 2: As a Manager

1. Login as manager account
2. Click "Add PG" in navbar
3. Fill in PG details:
   - Name, description
   - City, address
   - Monthly price
   - Number of rooms
   - Select amenities
   - Upload image
4. Submit to create listing
5. View dashboard with statistics
6. Check "Applications" for seeker applications
7. Approve or reject applications

### Step 3: As a Seeker

1. Login as seeker account
2. Browse home page for listings
3. Use search bar to filter by city
4. Use price range filter
5. Check desired amenities
6. Click "View Details" on a listing
7. Click "Apply Now"
8. Optionally add a message about yourself
9. Submit application
10. Check "My Applications" to track status

## 🎨 Frontend Details

- **Framework**: Bootstrap 5 (CDN)
- **Icons**: FontAwesome 6.4
- **Responsive**: Mobile-first design
- **Colors**: Professional blue theme with gradients
- **Cards**: Hover animations and shadows
- **Forms**: Bootstrap-styled with validation

## 🔧 Technology Stack

- **Django**: 5.0.3
- **Python**: 3.8+
- **Database**: SQLite (development)
- **Image Processing**: Pillow
- **Frontend**: Bootstrap 5, HTML5, CSS3

## 📚 Important Files

- `project_spec.md` - Original project requirements
- `SETUP_GUIDE.md` - Comprehensive setup guide
- `requirements.txt` - All dependencies
- `models.py` - Database schema definition
- `views.py` - Business logic (20+ views)
- `forms.py` - Form validation and rendering
- `urls.py` - URL routing

## ⚡ Quick Commands

```bash
# Start development server
python manage.py runserver

# Create database tables
python manage.py migrate

# Create migrations after model changes
python manage.py makemigrations

# Create superuser (admin)
python manage.py createsuperuser

# Access Django shell (for debugging)
python manage.py shell

# Run tests
python manage.py test

# Clear database and start fresh
python manage.py flush
```

## 🚨 Troubleshooting

**Images not showing?**
- Check `media/` folder exists
- Ensure `MEDIA_URL` and `MEDIA_ROOT` in settings.py

**Static files missing?**
- Run: `python manage.py collectstatic`

**Module not found errors?**
- Ensure virtual environment is activated
- Run: `pip install -r requirements.txt`

**Login not working?**
- Make sure user is created
- Check `AUTH_USER_MODEL = 'listings.CustomUser'` in settings

**Database locked?**
- Delete `db.sqlite3`
- Run migrations again

## 🔐 Security Notes

- DEBUG is currently enabled (set to False for production)
- SECRET_KEY should be protected in production
- Use environment variables for sensitive data
- HTTPS/SSL required for production
- CSRF protection is enabled by default

## 📈 Next Steps

1. **Test the application** thoroughly
2. **Customize styling** in static/css/
3. **Add more features** (ratings, messaging, etc.)
4. **Deploy to production** when ready
5. **Set up email notifications** (optional)
6. **Implement payment system** (optional)

## 📧 Support

Refer to:
- `SETUP_GUIDE.md` - Detailed instructions
- Django Documentation: https://docs.djangoproject.com/
- Bootstrap Documentation: https://getbootstrap.com/docs/

---

**You're all set! 🎉 The application is ready to run. Start with the 50-second setup above.**
