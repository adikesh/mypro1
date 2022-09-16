from datetime import datetime
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Youtuber(models.Model):
    crew_choices=(
        ('solo','solo'),
        ('small','small'),
        ('large','large'),
    )

    camera_choices=(
        ('nikon','nikon'),
        ('sony','sony'),
        ('canon','canon'),
    )
    category_choices=(
        ('review','review'),
        ('comedy','comedy'),
        ('edu','edu'),
    )



    name=models.CharField(max_length=255)
    price=models.IntegerField()
    photo=models.ImageField(upload_to="media/youtuber/%Y/%m/%d")
    video_url=models.CharField(max_length=255)
    description=RichTextField()
    city=models.CharField(max_length=255)
    age=models.IntegerField()
    height=models.IntegerField()
    crew=models.CharField(choices=crew_choices,max_length=255)
    camera_type=models.CharField(choices=camera_choices,max_length=255)
    is_featured=models.BooleanField(default=False)
    category=models.CharField(choices=category_choices,max_length=255)
    created_date=models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name
