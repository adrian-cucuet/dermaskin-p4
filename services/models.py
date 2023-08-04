from django.db import models


class Service(models.Model):
    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    name = models.CharField(max_length=300)
    image = models.ImageField()
    description = models.TextField()
    benefits = models.TextField()
    duration = models.IntegerField()
    sessions_needed = models.IntegerField()
    duration_of_results = models.IntegerField()
    frequency = models.IntegerField()
    faq1 = models.CharField(max_length=500)
    faq1_answer = models.TextField()
    faq2 = models.CharField(max_length=500)
    faq2_answer = models.TextField()
    faq3 = models.CharField(max_length=500)
    faq3_answer = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return self.name
