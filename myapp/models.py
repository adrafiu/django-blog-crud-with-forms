from django.db import models

# Create your models here.


class Blog(models.Model):
    CATEGORY_CHOICES = [
        ("Educational", "Educational"),
        ("Technology", "Technology"),
        ("Sports", "Sports"),
        ("Others", "Others"),
    ]
    title = models.CharField(max_length=200)
    author_name = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to="blogs/")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
