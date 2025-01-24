from django.contrib import admin
from core.apps.products.models.products import Product
from core.apps.products.models.reviews import Review


class ProductReviewInline(admin.TabularInline):
    model = Review
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_visible')
    inlines = (ProductReviewInline, )
    

@admin.register(Review)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'customer', 'created_at', 'updated_at', 'rating')
    list_select_related = ('customer', 'product')