from django.shortcuts import render
from the_site.models import Sobre, Consumo, Beneficios, Depoimentos, Projetos

def Home(request):
    TabelaConsumo = Consumo.objects.all()
    SobreItem = Sobre.objects.get(pk=1)
    return render(request, 'index.html', {'TabelaConsumo': TabelaConsumo, 'SobreItem': SobreItem})

def SobreDse(request):
    SobreItem = Sobre.objects.get(pk=1)
    return render(request, 'sobre-a-dse.html', {'SobreItem': SobreItem})

def BeneficiosDse(request):
    BeneItens = Beneficios.objects.all()
    return render(request, 'beneficios.html', {'BeneItens': BeneItens})

def DepoimentosClientes(request):
    DepoItens = Depoimentos.objects.all()
    for dItem in DepoItens:
        dItem.Depoimento_iden = dItem.pk
        if len(dItem.Texto_depoimento) > 129:
            dItem.Descricao_box = dItem.Texto_depoimento[0:129] + '(...)'
        else:
            dItem.Descricao_box = dItem.Texto_depoimento
    return render(request, 'depoimentos.html', {'DepoItens': DepoItens})

def ProjetosFeitos(request):
    ProjeItens = Projetos.objects.all()
    for pItem in ProjeItens:
        pItem.Galeria = pItem.Imagens.split('@')
        pItem.Galeria_capa = pItem.Galeria[0]
        pItem.Galeria_imagens = pItem.Galeria[1:]
    return render(request, 'projetos.html', {'ProjeItens': ProjeItens})

def Contato(request):
    return render(request, 'contato.html')