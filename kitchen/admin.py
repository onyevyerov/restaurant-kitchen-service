from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from kitchen.models import Dish, Cook, DishType, Ingredient


@admin.register(Cook)
class CookAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("years_of_experience",)
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("years_of_experience",)}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "years_of_experience",
                    )
                },
            ),
        )
    )


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("dish_type",)


@admin.register(DishType)
class DishTypeAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("country",)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    search_fields = ("name",)
