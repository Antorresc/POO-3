#aqui se almacena el salario 
class Salario:
    def __init__(self, horas_trabajadas, valor_hora, retencion_fuente):
        self.horas_trabajadas = horas_trabajadas
        self.valor_hora = valor_hora
        self.retencion_fuente = retencion_fuente

    def calcular_salario_bruto(self):
        return self.horas_trabajadas * self.valor_hora

    def calcular_salario_neto(self):
        salario_bruto = self.calcular_salario_bruto()
        descuento = salario_bruto * (self.retencion_fuente / 100)
        return salario_bruto - descuento
