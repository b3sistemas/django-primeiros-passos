from django.db import models

class Pessoa(models.Model):
    nome_completo = models.CharField(max_length=256)
    data_nascimento = models.DateField(null=True)
    ativo = models.BooleanField(default=True)

    def __str__(self) -> str:
        return super().__str__()
        #return self.nome_completo