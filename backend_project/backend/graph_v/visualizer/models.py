from django.db import models

# Create your models here.
from django.core.validators import MinValueValidator, MaxValueValidator

class GraphVisualization(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    
    c = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(20)],
        help_text='A float value between 0 and 20'
    )
    t = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text='A float value between 0 and 100'
    )
    graph_file = models.FileField(upload_to='graphs/', help_text='Upload a graph txt file')

    image_file = models.ImageField(upload_to='images/', help_text='Upload an image file')

    def __str__(self):
        return f'Graph Visualization - c: {self.c}, t: {self.t}'

    class Meta:
        ordering = ['created']
