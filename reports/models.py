from django.db import models
from django.contrib.auth.models import User

class ReportType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class VisualizationType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class ReportLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    report_type = models.ForeignKey(ReportType, on_delete=models.CASCADE)
    date_range_start = models.DateField()
    date_range_end = models.DateField()
    visualization_type = models.ForeignKey(VisualizationType, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.report_type} for {self.user.username} from {self.date_range_start} to {self.date_range_end}'