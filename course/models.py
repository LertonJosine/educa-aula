from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Course(models.Model):
    name = models.CharField(max_length=100)
    trainer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    resume = models.TextField()
    sits = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.ImageField(upload_to=".", blank=True)
    
    def __str__(self) -> str:
        return self.name[:50]
    
    def get_absolute_url(self):
        return reverse("list_courses")
    
    
