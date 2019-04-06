
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.
from django.utils import timezone


class Article(models.Model):
    title = models.CharField(max_length=20)
    img = models.ImageField(upload_to='files', blank=True)
    date = models.DateTimeField(default=timezone.now)
    article = RichTextUploadingField(verbose_name='内容')

