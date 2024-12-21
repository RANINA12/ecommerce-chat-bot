from django.contrib import admin
from .models import Product, Chat

# Register the Product model with custom admin settings
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'model_name', 'price')  # Fields to display in the list view
    search_fields = ('model_name', 'details')     # Add search functionality for model_name and details
    list_filter = ('price',)                      # Filter options for price
    ordering = ('model_name',)                    # Default ordering by model_name

# Register the Chat model with custom admin settings
@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'query_type', 'user_input', 'response', 'timestamp')  # Fields to display
    search_fields = ('user__username', 'query_type', 'user_input')                      # Search by user, query_type, and user_input
    list_filter = ('query_type', 'timestamp')                                           # Filter options for query_type and timestamp
    ordering = ('-timestamp',)                                                          # Default ordering by latest timestamp
    readonly_fields = ('timestamp',)                                                    # Make timestamp read-only
