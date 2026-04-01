from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import Http404
from django.db.models import Q, Count
from .models import CustomUser, PGListing, Application
from .forms import (
    CustomUserCreationForm, CustomUserChangeForm, CustomAuthenticationForm,
    PGListingForm, ApplicationForm, ApplicationStatusForm, SearchListingForm
)


# ===================== Authentication Views =====================

class RegisterView(CreateView):
    """View for user registration."""
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        messages.success(self.request, 'Registration successful! Please log in.')
        return super().form_valid(form)


class CustomLoginView(LoginView):
    """View for user login."""
    form_class = CustomAuthenticationForm
    template_name = 'auth/login.html'
    
    def get_success_url(self):
        user = self.request.user
        if user.is_manager():
            return reverse_lazy('manager_dashboard')
        else:
            return reverse_lazy('home')


class CustomLogoutView(LogoutView):
    """View for user logout."""
    next_page = reverse_lazy('home')


class ProfileView(LoginRequiredMixin, DetailView):
    """View for user profile."""
    model = CustomUser
    template_name = 'auth/profile.html'
    context_object_name = 'profile_user'
    
    def get_object(self):
        return self.request.user


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """View for updating user profile."""
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'auth/update_profile.html'
    success_url = reverse_lazy('profile')
    
    def get_object(self):
        return self.request.user
    
    def form_valid(self, form):
        messages.success(self.request, 'Profile updated successfully!')
        return super().form_valid(form)


# ===================== Home & Search Views =====================

class HomeView(View):
    """Home page with search and listing gallery."""
    
    def get(self, request):
        form = SearchListingForm(request.GET)
        listings = PGListing.objects.filter(is_active=True)
        
        if form.is_valid():
            city = form.cleaned_data.get('city')
            min_price = form.cleaned_data.get('min_price')
            max_price = form.cleaned_data.get('max_price')
            
            if city:
                listings = listings.filter(city__icontains=city)
            
            if min_price is not None:
                listings = listings.filter(price_per_month__gte=min_price)
            
            if max_price is not None:
                listings = listings.filter(price_per_month__lte=max_price)
            
            if form.cleaned_data.get('has_wifi'):
                listings = listings.filter(has_wifi=True)
            
            if form.cleaned_data.get('has_ac'):
                listings = listings.filter(has_ac=True)
            
            if form.cleaned_data.get('has_food'):
                listings = listings.filter(has_food=True)
            
            if form.cleaned_data.get('has_laundry'):
                listings = listings.filter(has_laundry=True)
        
        context = {
            'listings': listings,
            'form': form,
        }
        return render(request, 'listings/home.html', context)


class ListingDetailView(DetailView):
    """View for displaying listing details."""
    model = PGListing
    template_name = 'listings/listing_detail.html'
    context_object_name = 'listing'
    
    def get_queryset(self):
        return PGListing.objects.filter(is_active=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        listing = self.get_object()
        context['can_apply'] = (
            self.request.user.is_authenticated and 
            self.request.user.is_seeker() and 
            not Application.objects.filter(pg=listing, applicant=self.request.user).exists()
        )
        return context


# ===================== Manager Dashboard & Listing Management =====================

class ManagerDashboardView(LoginRequiredMixin, UserPassesTestMixin, View):
    """Dashboard for PG managers."""
    
    def test_func(self):
        return self.request.user.is_manager()
    
    def get(self, request):
        listings = PGListing.objects.filter(owner=request.user)
        pending_applications = Application.objects.filter(
            pg__owner=request.user,
            status='pending'
        ).count()
        
        context = {
            'listings': listings,
            'pending_applications': pending_applications,
            'total_listings': listings.count(),
            'total_applications': Application.objects.filter(pg__owner=request.user).count(),
        }
        return render(request, 'listings/manager_dashboard.html', context)


class CreateListingView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """View for creating a new PG listing."""
    model = PGListing
    form_class = PGListingForm
    template_name = 'listings/create_listing.html'
    success_url = reverse_lazy('manager_dashboard')
    
    def test_func(self):
        return self.request.user.is_manager()
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        messages.success(self.request, 'Listing created successfully!')
        return super().form_valid(form)


class UpdateListingView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """View for updating a PG listing."""
    model = PGListing
    form_class = PGListingForm
    template_name = 'listings/update_listing.html'
    success_url = reverse_lazy('manager_dashboard')
    
    def test_func(self):
        listing = self.get_object()
        return self.request.user == listing.owner
    
    def form_valid(self, form):
        messages.success(self.request, 'Listing updated successfully!')
        return super().form_valid(form)


class DeleteListingView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """View for deleting a PG listing."""
    model = PGListing
    template_name = 'listings/delete_listing.html'
    success_url = reverse_lazy('manager_dashboard')
    
    def test_func(self):
        listing = self.get_object()
        return self.request.user == listing.owner
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Listing deleted successfully!')
        return super().delete(request, *args, **kwargs)


# ===================== Application Management Views =====================

class ApplicationListView(LoginRequiredMixin, UserPassesTestMixin, View):
    """View for managers to review applications."""
    
    def test_func(self):
        return self.request.user.is_manager()
        
        listings = PGListing.objects.filter(owner=request.user)
        applications = Application.objects.filter(pg__owner=request.user).select_related('pg', 'applicant')
        
        # Filter by status if provided
        status_filter = request.GET.get('status')
        if status_filter:
            applications = applications.filter(status=status_filter)
        
        # Filter by listing if provided
        listing_filter = request.GET.get('listing')
        if listing_filter:
            applications = applications.filter(pg_id=listing_filter)
        
        context = {
            'applications': applications,
            'listings': listings,
            'status_filter': status_filter,
            'listing_filter': listing_filter,
        }
        return render(request, 'listings/applications_list.html', context)


class UpdateApplicationStatusView(LoginRequiredMixin, View):
    """View for updating application status."""
    
    def post(self, request, pk):
        application = get_object_or_404(Application, pk=pk)
        
        # Check if user is the owner of the PG
        if request.user != application.pg.owner:
            raise Http404("You don't have permission to access this page.")
        
        form = ApplicationStatusForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            status_text = dict(Application.STATUS_CHOICES)[form.cleaned_data['status']]
            messages.success(request, f"Application status updated to {status_text}!")
        
        return redirect('applications_list')


class ApplyListingView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """View for seekers to apply to a listing."""
    model = Application
    form_class = ApplicationForm
    template_name = 'listings/apply_listing.html'
    
    def test_func(self):
        return self.request.user.is_seeker()
    
    def dispatch(self, request, *args, **kwargs):
        # Check if already applied
        listing_id = self.kwargs.get('listing_id')
        listing = get_object_or_404(PGListing, pk=listing_id)
        if Application.objects.filter(pg=listing, applicant=request.user).exists():
            raise Http404("You have already applied to this listing.")
        
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        listing_id = self.kwargs.get('listing_id')
        context['listing'] = get_object_or_404(PGListing, pk=listing_id)
        return context
    
    def form_valid(self, form):
        form.instance.applicant = self.request.user
        form.instance.pg_id = self.kwargs.get('listing_id')
        messages.success(self.request, 'Application submitted successfully!')
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('listing_detail', kwargs={'pk': self.kwargs.get('listing_id')})


class SeekerApplicationsView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    """View for seekers to see their applications."""
    model = Application
    template_name = 'listings/seeker_applications.html'
    context_object_name = 'applications'
    
    def test_func(self):
        return self.request.user.is_seeker()
    
    def get_queryset(self):
        return Application.objects.filter(applicant=self.request.user).select_related('pg', 'pg__owner')
