from django.urls import path
from .views import (
    RegisterView, CustomLoginView, CustomLogoutView, ProfileView, UpdateProfileView,
    HomeView, ListingDetailView, ManagerDashboardView, CreateListingView, UpdateListingView,
    DeleteListingView, ApplicationListView, UpdateApplicationStatusView, ApplyListingView,
    SeekerApplicationsView
)

urlpatterns = [
    # Authentication URLs
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/update/', UpdateProfileView.as_view(), name='update_profile'),
    
    # Home and Search
    path('', HomeView.as_view(), name='home'),
    path('listing/<int:pk>/', ListingDetailView.as_view(), name='listing_detail'),
    
    # Manager Dashboard and Listings
    path('dashboard/', ManagerDashboardView.as_view(), name='manager_dashboard'),
    path('listing/create/', CreateListingView.as_view(), name='create_listing'),
    path('listing/<int:pk>/update/', UpdateListingView.as_view(), name='update_listing'),
    path('listing/<int:pk>/delete/', DeleteListingView.as_view(), name='delete_listing'),
    
    # Applications
    path('applications/', ApplicationListView.as_view(), name='applications_list'),
    path('application/<int:pk>/update-status/', UpdateApplicationStatusView.as_view(), name='update_application_status'),
    path('listing/<int:listing_id>/apply/', ApplyListingView.as_view(), name='apply_listing'),
    path('my-applications/', SeekerApplicationsView.as_view(), name='seeker_applications'),
]
