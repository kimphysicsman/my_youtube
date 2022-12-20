from django.db import models

class ChartModel(models.Model):
    rank_1 = models.CharField("1위", max_length=128)
    rank_2 = models.CharField("2위", max_length=128)
    rank_3 = models.CharField("3위", max_length=128)
    rank_4 = models.CharField("4위", max_length=128)
    rank_5 = models.CharField("5위", max_length=128)

    date = models.DateTimeField("날짜", auto_now_add=True)

    def __str__(self):
        return f"{self.id} - {self.date}" 