from django.db import models
from django.urls import reverse

# Create your models here.
class Books(models.Model):
    class Meta:
        db_table = 'books'
    isbn = models.CharField(verbose_name="ISBN", max_length=140)
    title = models.CharField(verbose_name="タイトル", max_length=140)
    author = models.CharField(verbose_name="著者", max_length=140)
    publisher = models.CharField(verbose_name="出版社", max_length=140)
    published_date = models.DateTimeField(verbose_name="出版日", null=True, blank=True)
    genre = models.CharField(verbose_name="ジャンル", max_length=140)
    rent = models.BooleanField(verbose_name="貸出状況", default=False)
    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})
    
    
    def __str__(self):
        return self.title