from django.contrib import admin

from .models import Order, OrderLineItem


# Code adapted from Boutique Ado
class OrderLineItemAdminInline(admin.TabularInline):
    """
    defines how OrderLineItem will appear in admin
    panel
    """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    defines how Orderwill appear in admin
    panel
    """
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'order_total', 'original_basket', 'stripe_pid')

    fields = ('order_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'order_total',
              'original_basket', 'stripe_pid')

    list_display = ('order_number', 'date', 'full_name',
                    'order_total',)

    ordering = ('-date',)
