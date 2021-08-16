from django.db import models

# Create your models here.


class demirbasobje(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Ekleyen Kişi")
    title = models.CharField(max_length=50, verbose_name="Nesne Türü")
    no = models.CharField(max_length=10, verbose_name="Demirbas No")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Eklenme Tarihi")

  #