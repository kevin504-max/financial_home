from ..models import Gastos 

class GastoFactory:
    @staticmethod
    def criar_gasto(descricao, valor, data, metodo_pagamento, usuario, categoria, recorrencia):
        print(data)
        return Gastos(
            descricao=descricao,
            valor=valor,
            data=data,
            metodo_pagamento=metodo_pagamento,  
            usuario=usuario,  
            categoria=categoria,  
            recorrencia=recorrencia
        )
