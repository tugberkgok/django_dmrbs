from django.db import models

# Create your models here.
class Worker(models.Model):
    person = models.CharField(max_length=50, verbose_name="isim")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Kayıt Tarihi")

    def __str__(self):
        return self.person

class Device(models.Model):
    stok = models.CharField(max_length=10, null=True, blank=True, verbose_name="Stok")
    device = models.CharField(max_length=20, null=True, blank=True, verbose_name="Cihaz")
    number = models.CharField(max_length=5, null=True, blank=True, verbose_name="Sayı")
    brand = models.CharField(max_length=30, null=True, blank=True, verbose_name="Marka")
    model = models.CharField(max_length=30, null=True, blank=True, verbose_name="Model")
    serial = models.CharField(max_length=50, null=True, blank=True, verbose_name="Seri No")
    status = models.CharField(max_length=10, null=True, blank=True, verbose_name="Durumu")
    exp = models.CharField(max_length=100, null=True, blank=True, verbose_name="Açıklama")
    person_id = models.ForeignKey(Worker, default=1, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Kayıt Tarihi")

    def __str__(self):
        return self.device






