from django.apps import AppConfig

import awardapp


class AwardappConfig(AppConfig):
    name = 'awardapp'

    def ready(self):
        import awardapp.signals
