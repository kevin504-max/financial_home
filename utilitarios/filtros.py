from django import template
from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def formatar_dinheiro(valor):
    return locale.currency(valor, grouping=True)

