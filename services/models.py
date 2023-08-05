from django.db import models


class Service(models.Model):
    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    name = models.CharField(max_length=300, null=True, blank=True)
    slug = models.SlugField(max_length=300, unique=True)
    description = models.TextField(null=True, blank=True)
    benefits = models.TextField(null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    sessions_needed = models.IntegerField(null=True, blank=True)
    duration_of_results = models.IntegerField(null=True, blank=True)
    frequency = models.IntegerField(null=True, blank=True)
    faq1 = models.CharField(max_length=500, null=True, blank=True)
    faq1_answer = models.TextField(null=True, blank=True)
    faq2 = models.CharField(max_length=500, null=True, blank=True)
    faq2_answer = models.TextField(null=True, blank=True)
    faq3 = models.CharField(max_length=500, null=True, blank=True)
    faq3_answer = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0,
                                null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
