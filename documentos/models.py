from django.db import models
from funcionarios.models import Funcionarios


class Documentos(models.Model):
    pertence = models.ForeignKey(Funcionarios, models.PROTECT)
    descricao = models.CharField(max_length= 70)




