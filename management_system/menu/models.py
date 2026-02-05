from django.db import models

# Create your models here.
class Menu(models.Model):
    MENU_TYPE_LIST=[
        ('Hot Coffee','Hot Coffee'),
        ('Cold Coffee', 'Cold Coffee'),
        ('Special Coffee', 'Special Coffee'),
    ]
    name = models.CharField(max_length=60)
    image = models.ImageField(upload_to='menu/')
    description = models.TextField(default="")
    type = models.CharField(max_length=20 , choices=MENU_TYPE_LIST)
    price = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        default="",
    )
def __str__(self):
    return self.name

