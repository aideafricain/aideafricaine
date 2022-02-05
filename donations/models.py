# from django.db import models
# from django.utils import timezone
#
#
# # Create your models here.
#
# class Donation(models.Model):
#
#     name = models.CharField(max_length=50)
#     amount = models.FloatField(default=0)
#     email = models.EmailField()
#     message = models.CharField(max_length=280, blank=True)
#     date = models.DateTimeField(default=timezone.now)
#     payment_method = models.CharField(max_length=50, blank=True)
#     payment_status = models.CharField(max_length=25, blank=True)
#
#     def __str__(self):
#         return self.name
