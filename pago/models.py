from django.db import models

# Create your models here.
class DatosPago(models.Model):
    monto_pago = models.DecimalField(max_digits=10, decimal_places=2)
    moneda_pago = models.CharField(max_length=3, choices=(('CLP', 'Peso Chileno'), ('USD', 'Dólar Estadounidense'), ('EUR', 'Euro')))
    metodo_pago = models.CharField(max_length=20, choices=(('ONLINE', 'Online'), ('TRANSFERENCIA', 'Transferencia'), ('EFECTIVO', 'Efectivo')))
    moneda_final = models.CharField(max_length=3, choices=(('CLP', 'Peso Chileno'), ('USD', 'Dólar Estadounidense'), ('EUR', 'Euro')))
    fecha_pago = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pago de {self.monto_pago} {self.moneda_pago} mediante {self.metodo_pago}"

class Boleta(models.Model):
    fecha_emision = models.DateTimeField(auto_now_add=True)
    total_original = models.DecimalField(max_digits=10, decimal_places=2)
    moneda_original = models.CharField(max_length=3, default='CLP')
    total_final = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    moneda_final = models.CharField(max_length=3, choices=(('CLP', 'Peso Chileno'), ('USD', 'Dólar Estadounidense'), ('EUR', 'Euro')))
    estado = models.CharField(max_length=10, choices=(('PENDIENTE', 'Pendiente'), ('PAGADA', 'Pagada'), ('ANULADA', 'Anulada')))

    def __str__(self):
        return f"Boleta {self.id} - {self.estado}"
