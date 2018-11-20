from django.db import models

# Create your models here.
class QueueLength(models.Model):
    cameraid = models.CharField(max_length = 30)
    cameraip = models.CharField(max_length = 30)
    alarmtime = models.DateTimeField(auto_now_add = True)
    alarmdata = models.CharField(max_length = 50)

    def __str__(self):
        return self.cameraid

class StationHall(models.Model):
    cameraid = models.CharField(max_length = 30)
    cameraip = models.CharField(max_length = 30)
    alarmtime = models.DateTimeField(auto_now_add = True)
    alarmdata = models.IntegerField()

    def __str__(self):
        return self.cameraid
