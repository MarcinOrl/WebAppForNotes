from django.apps import AppConfig

class NotesAppConfig(AppConfig):
    name = 'notes_app'

    def ready(self):
        import notes_app.signals
