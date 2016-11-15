from django_cron import CronJobBase, Schedule
from tables.cached_media import *
from datetime import datetime, timedelta
import os
from django.conf import settings
class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 60*24

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'cronjobs.cronjobs.my_cron_job'

    def do(self):
        # if its been in cache unused for more than 3 days
        # remove the media
        d = datetime.today() - timedelta(days=3)
        cached_media = CachedMedia.objects.filter(last_hit_at__lte = d)
        for query in cached_media:
            name = str(query.image)
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
            query.delete()