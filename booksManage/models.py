from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
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
    rent_user = models.ForeignKey(get_user_model(), verbose_name="貸出ユーザー", null=True, blank=True, on_delete=models.SET_NULL)
    
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.title
    
class RentHistory(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    lent_at = models.DateTimeField(auto_now_add=True)
    returned_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.book.title}"