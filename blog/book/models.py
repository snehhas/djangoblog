from django.db import models

# Create your models here.
class Book(models.Model):
    CATEGORY = (
        ('science','Science'),
        ('tech','Technology'),
        ('sports','Sportss'),
        ('ent','Entertainment')
    )
    id = models.BigAutoField(
        primary_key=True
    )

    name=models.CharField(
        max_length=150,
        unique=True,
        null=False,
        blank=False,
        verbose_name='Book Name'
    )

    category=models.CharField(
        max_length=50,
        choices=CATEGORY,
        verbose_name='category'
    )

    author=models.CharField(
        max_length=150,
        null=False,
        blank=False,
        verbose_name='author'
    )

    price=models.IntegerField(
        default=0,
        verbose_name='Price'
    )

    published_on=models.DateField(
        verbose_name='Published on',
        null=False,
        blank=False
    )

    created_on=models.DateField(
        auto_now_add=True
    )

    updated_on=models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name