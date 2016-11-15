from django_cron import CronJobBase, Schedule

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 0.1 # every 2 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'cronjobs.cronjobs.my_cron_job'    # a unique code

    def do(self):
        print("HULA")
        pass    # do your thing here