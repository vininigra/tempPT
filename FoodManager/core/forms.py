from django import forms
import datetime

# produto, requerente, doador


class ProdutoForm(forms.Form):
    nome = forms.CharField(max_length=100, required=True)
    quantidade = forms.IntegerField(required=True)
    # validade do produto
    validade = forms.DateField(required=True)

    # metodo validacao
    def clean_nome(self):
        nome = self.cleaned_data["nome"]
        if nome.isnumeric():
            raise forms.ValidationError("Nome não pode ser numerico")
        return nome

    def clean_quantidade(self):
        quantidade = self.cleaned_data["quantidade"]
        if quantidade < 0:
            raise forms.ValidationError("Quantidade não pode ser negativa")
        return quantidade

    def clean_validade(self):
        validade = self.cleaned_data["validade"]
        if validade < datetime.date.today():
            raise forms.ValidationError(
                "Data de validade não pode ser anterior a data atual"
            )
        return validade
