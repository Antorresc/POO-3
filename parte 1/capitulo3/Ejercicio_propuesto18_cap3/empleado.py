from salario import Salario

class Empleado:
    def __init__(self, codigo, nombres, horas_trabajadas, valor_hora, retencion_fuente):
        self.codigo = codigo
        self.nombres = nombres
        self.salario = Salario(horas_trabajadas, valor_hora, retencion_fuente)

    def obtener_informacion(self):
        salario_bruto = self.salario.calcular_salario_bruto()
        salario_neto = self.salario.calcular_salario_neto()
        return {
            "codigo": self.codigo,
            "nombres": self.nombres,
            "salario_bruto": salario_bruto,
            "salario_neto": salario_neto,
        }
