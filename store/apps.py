from django.apps import AppConfig

# настройка приложения store
class StoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # Название приложения
    name = 'store'
