from django.contrib import admin
from django.db.models.fields import Field
from api.models import Brand, Car, Category, ExtendUser, Order, Model, City, Country


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("model", "get_brand", "category", "fuel_type",
                    "registration", "color_type", "booking",)

    def get_brand(self, obj):
        return obj.model.brand


admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(ExtendUser)
admin.site.register(Order)
admin.site.register(Model)
admin.site.register(Country)
admin.site.register(City)
