from django.db import models
from django.utils import timezone

class Post(models.Model):

    title = models.CharField(
        'Название поста',
        max_length=128,
        null= True
    )
    brand = models.CharField(
        'brands',
        max_length=128,
        null= True

    )
    color = models.CharField(
        'colors',
        max_length=128,
        null= True
    )
    capacity = models.IntegerField(
        null = True
    )
    horse_power = models.IntegerField(
        null = True
    )
    price = models.IntegerField(
        blank=True,
        null =True
    )


    description = models.TextField(
        'Описание',
        blank=True,  
        null=True    
    )

    created_date = models.DateField(
        'Дата создания',
        default=timezone.now
    )

    image = models.ImageField(
        'Фото поста',
        upload_to='posts-images/'
    )
    

    def __str__(self):
        return f'{self.title}'
    
    class Meta:

        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ('-id',)