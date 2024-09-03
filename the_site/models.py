from django.db import models

from django.contrib.auth.models import User
from django.db import models

class Consumo(models.Model):
    Titulo = models.CharField(max_length=255, verbose_name='Título')
    Media_mensal = models.CharField(max_length=100, verbose_name='Média Mensal')
    Valor_consumo = models.CharField(max_length=100, verbose_name='Valor do Consumo')
    Kwp = models.CharField(max_length=100)
    Area_placas = models.CharField(max_length=100, verbose_name='Área das Placas')
    Custo = models.CharField(max_length=100)
    Parcelas_mensais = models.CharField(max_length=100, verbose_name='Parcelas Mensais')
    Parcela_fixa = models.CharField(max_length=100, verbose_name='Parcela Fixa')
    Valor_mensal = models.CharField(max_length=100, verbose_name='Valor Mensal')
    Autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Titulo

class Sobre(models.Model):
    Sobre_tituloUm = models.CharField(max_length=200, verbose_name='Primeiro Título')
    Sobre_paragrafoUm = models.TextField(max_length=400, verbose_name='Primeiro Paragráfo')
    Sobre_tituloDois = models.CharField(max_length=200, verbose_name='Segundo Título')
    Sobre_paragrafoDois = models.TextField(max_length=400, verbose_name='Segundo Paragráfo')
    Sobre_imagem = models.CharField(max_length=255, verbose_name='Imagem')

    class Meta:
        verbose_name_plural = "Sobre"

    novoTitulo = 'Alterar Conteúdo'
    def __str__(self):
        return self.novoTitulo

class Beneficios(models.Model):
    Beneficios_imagem = models.CharField(max_length=255, verbose_name='Imagem')
    Beneficios_descricao = models.TextField(max_length=100, verbose_name='Descrição')
    Autor = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Benefício"
    
    def __str__(self):
        return 'Benefício ' + f'{self.pk}'
    

class Depoimentos(models.Model):
    Nome = models.CharField(max_length=255)
    Cargo = models.CharField(max_length=255)
    Texto_depoimento = models.TextField(max_length=500, verbose_name='Depoimento')
    Depoimento_imagem = models.CharField(max_length=255, verbose_name='Imagem da Pessoa')
    Descricao_box = ''
    Depoimento_iden = '1'
    Autor = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Depoimento"

    def __str__(self):
        return self.Nome 

class Projetos(models.Model):
    Nome_projeto = models.CharField(max_length=400, verbose_name='Nome do Projeto')
    Cidade = models.CharField(max_length=255)
    Imagens = models.TextField()
    Autor = models.ForeignKey(User, on_delete=models.CASCADE)
    Galeria = ''
    Galeria_capa = ''
    Galeria_imagens = ''

    class Meta:
        verbose_name = "Projeto"

    def __str__(self):
        return self.Nome_projeto
