from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, PGListing, Application


class CustomUserAdmin(UserAdmin):
    """Admin configuration for CustomUser model."""
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'user_role')
    list_filter = ('user_role', 'date_joined')
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('user_role', 'phone_number', 'profile_image')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('user_role', 'phone_number')}),
    )


class PGListingAdmin(admin.ModelAdmin):
    """Admin configuration for PGListing model."""
    list_display = ('pg_name', 'owner', 'city', 'price_per_month', 'rooms_available', 'is_active', 'created_at')
    list_filter = ('city', 'is_active', 'created_at', 'has_wifi', 'has_ac', 'has_food', 'has_laundry')
    search_fields = ('pg_name', 'city', 'address', 'owner__username')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Basic Information', {
            'fields': ('owner', 'pg_name', 'description', 'is_active')
        }),
        ('Location & Price', {
            'fields': ('city', 'address', 'price_per_month')
        }),
        ('Availability', {
            'fields': ('rooms_available',)
        }),
        ('Amenities', {
            'fields': ('has_wifi', 'has_ac', 'has_food', 'has_laundry')
        }),
        ('Image', {
            'fields': ('image',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


class ApplicationAdmin(admin.ModelAdmin):
    """Admin configuration for Application model."""
    list_display = ('applicant', 'pg', 'status', 'applied_on', 'updated_at')
    list_filter = ('status', 'applied_on', 'pg__city')
    search_fields = ('applicant__username', 'pg__pg_name', 'pg__owner__username')
    readonly_fields = ('applied_on', 'updated_at')
    fieldsets = (
        ('Application Details', {
            'fields': ('pg', 'applicant', 'status')
        }),
        ('Message', {
            'fields': ('message',)
        }),
        ('Timestamps', {
            'fields': ('applied_on', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(PGListing, PGListingAdmin)
admin.site.register(Application, ApplicationAdmin)
