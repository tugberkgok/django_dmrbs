from django.db import models

# Create your models here.
class Worker(models.Model):
    person = models.CharField(max_length=50, verbose_name="isim")
    stok = models.CharField(max_length=10, verbose_name="Stok")
    device = models.CharField(max_length=20, verbose_name="Cihaz")
    number = models.CharField(max_length=5, verbose_name="Sayı")
    brand = models.CharField(max_length=30,verbose_name="Marka")
    serial = models.CharField(max_length=50,verbose_name="Seri No")
    status = models.CharField(max_length=10,verbose_name="Durumu")
    exp = models.CharField(max_length=100,verbose_name="Açıklama")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Kayıt Tarihi")
    def __str__(self):
        return self.person


