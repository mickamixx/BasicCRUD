from django.forms import ModelForm

from . import models
from .models import Transacao

Transacao

class TransacaoForm(ModelForm):
    class Meta:
        model = Transacao
        fields = ['data', 'descricao', 'valor', 'categoria', 'observacoes']


