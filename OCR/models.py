from django.conf import settings
from django.db import models
from django.utils import timezone

class Factura(models.Model):
    id = models.IntegerField(primary_key=True) #Rossum Id
    pdf_url = models.URLField(max_length=500)
    numero_factura = models.CharField(max_length=50, blank=True)
    numero_orden = models.CharField(max_length=50, blank=True)
    fecha_factura = models.DateField(blank=True)
    fecha_vencimiento = models.DateField(blank=True)
    numero_cuenta = models.CharField(max_length=50, blank=True)
    numero_banco = models.CharField(max_length=50, blank=True)
    iban = models.CharField(max_length=50, blank=True)
    monto = models.FloatField(null=True, blank=True, default=None)
    ivu = models.FloatField(null=True, blank=True, default=None)
    monto_total = models.FloatField(null=True, blank=True, default=None)
    nombre_empresa = models.CharField(max_length=100)
    direccion_empresa = models.CharField(max_length=200)
    nombre_cliente = models.CharField(max_length=100)
    direccion_cliente = models.CharField(max_length=200)
    
    def __str__(self):
        return self.fecha_factura.strftime("%m/%d/%Y") + " | " + self.nombre_empresa + " - Factura (" + self.numero_factura + ") " + self.nombre_cliente  