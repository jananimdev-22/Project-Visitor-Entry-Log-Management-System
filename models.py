from django.db import models

class Visitor(models.Model):
    visitor_name = models.CharField(max_length=100)
    purpose = models.CharField(max_length=200)
    in_time = models.CharField(max_length=50)
    out_time = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return self.visitor_name
