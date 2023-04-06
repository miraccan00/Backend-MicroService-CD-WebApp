from django.db import models


class MicroServices(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    version = models.CharField(max_length=100, null=True, blank=True)
    has_microui = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name + " | " + self.version + " | " + str(self.date)

class TrackMicroServiceVersion(models.Model):
    service = models.ForeignKey(MicroServices, on_delete=models.CASCADE)
    old_version = models.CharField(max_length=100, null=True, blank=True)
    new_version = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.service.name} ({self.old_version} -> {self.new_version}) on {self.date}'
