from utilitarios.filtros import formatar_dinheiro  
class GastoTotalizador:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GastoTotalizador, cls).__new__(cls)
        return cls._instance

    def calcular_total(self, gastos):
        total = sum(gasto.valor for gasto in gastos)
        return formatar_dinheiro(total) 
