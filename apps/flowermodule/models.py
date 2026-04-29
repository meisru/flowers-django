from django.db import models

SEASON_CHOICES = [
    ('spring',   'الربيع'),
    ('summer',   'الصيف'),
    ('autumn',   'الخريف'),
    ('winter',   'الشتاء'),
    ('yearround','طوال العام'),
]


class Flower(models.Model):
    name            = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=150, blank=True)
    description     = models.TextField()
    color           = models.CharField(max_length=50)
    origin          = models.CharField(max_length=100, blank=True)
    season          = models.CharField(max_length=20, choices=SEASON_CHOICES, default='spring')
    care_tips       = models.TextField(blank=True)
    image_url       = models.URLField(blank=True)

    def __str__(self):
        return self.name
