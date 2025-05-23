from django.db import models

class Categoria(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    dt_created = models.DateTimeField(auto_now_add=True)


class Transacao (models.Model):
    data=models.DateTimeField()
    descricao=models.CharField(max_length=200)
    valor=models.DecimalField(decimal_places=2, max_digits=7)
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)
    observacoes=models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Transações"

    def __str__(self):
        return self.descricao

