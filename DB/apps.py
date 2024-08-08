from django.apps import AppConfig
<<<<<<< HEAD
from apscheduler.schedulers.background import BackgroundScheduler

class YourAppConfig(AppConfig):
    name = 'DB'

    def ready(self):
        from .task import update_scooters
        
        scheduler = BackgroundScheduler()
        scheduler.add_job(update_scooters, 'interval', minutes=2)
        scheduler.start()
=======


class AppsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'DB'
>>>>>>> 2a6cb2766cf213d452a569e2c1f63982f1aaaec0
