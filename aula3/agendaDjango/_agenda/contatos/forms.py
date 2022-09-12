from django import forms
from .models import *

<<<<<<< HEAD
class FormularioCadastro(forms.ModelForm):
        class Meta:
            model = Contato
            fields = ['nome', 'sobrenome', 'telefone', 'email', 'data_nascimento', 'descricao', 'categoria']
=======

class FormularioCadstro(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'sobrenome', 'telefone', 'email',
                  'data_nascimento', 'descricao', 'categoria']
>>>>>>> bfd7902bf4844fd86db8738608e40358c7c809e1
