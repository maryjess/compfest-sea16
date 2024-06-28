# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Admin, Customer, Service, Reservation, Review, Branch

class AdminAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_active')
    search_fields = ('email', 'first_name', 'last_name')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'phone_number', 'is_active')
    search_fields = ('email', 'first_name', 'last_name', 'phone_number')

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_type', 'duration')
    search_fields = ('service_type',)

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('customer', 'service', 'date', 'time')
    search_fields = ('customer__first_name', 'customer__last_name', 'service__service_type')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'rating', 'created_at')
    search_fields = ('first_name', 'last_name', 'rating')

class BranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'opening_time', 'closing_time')
    search_fields = ('name', 'location')

admin.site.register(Admin, AdminAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Branch, BranchAdmin)