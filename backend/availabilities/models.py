from django.db import models


class Availability(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    booked = models.BooleanField(default=False)

    @property
    def end_time(self):
        return self.start_time.timedelta(minutes=30)

    class Meta:
        ordering = ["date", "start_time", "booked"]
