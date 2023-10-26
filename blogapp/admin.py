from django.contrib import admin
from .models import *


class FlowerAdmin(admin.ModelAdmin):
    list_display = ['name', 'color', 'type', 'isWhite']  # Показывает столбцы в списке объектов
    list_filter = ['type', 'color']  # Создает фильтры по данным полям
    readonly_fields = ['color']  # Блокирует поля только в админке, оставляя возможность только для чтения!
    ordering = ['name', 'color']  # Сортировка, слева на право по приоритету
    search_fields = ['name']

    def isWhite(self, flower):  # Создаем собственное поле, которого нет в модельке
        if flower.color == 'White':
            return "Да"
        return "Нет"

    isWhite.short_description = 'Белый?'  # Дает нашему новому полю название


class BouquetAdmin(admin.ModelAdmin):
    filter_horizontal = ['flowers']


admin.site.register(Bouquet, BouquetAdmin)
admin.site.register(Flower, FlowerAdmin)
admin.site.register(Post)
admin.site.register(FlowerType)
admin.site.register(Music)
