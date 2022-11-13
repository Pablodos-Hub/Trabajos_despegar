# ------ ESTADOS ------
class Nueva:
    def precio_final(self,precio):
        return precio

class Promocion:
    def __init__(self,valor_promo):
        self.valor = valor_promo
    def precio_final(self,precio):
        return precio - self.valor

class Liquidacion:
    def precio_final(self,precio):
        return precio /2