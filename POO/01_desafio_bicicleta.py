class Bicicleta:
    def _init_(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def Buzinar(self):
        print("Plim plim...")
    
    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")
    
    def correr(self):
        print("Vrummmmm...")

    def _str_(self):
        return f"{self._class_._name_}: {', '.join([f'{chave}={valor}' for chave, valor, in self._dict_.items()])}"


b1 = Bicicleta("vermelha", "caloi", 2022, 600)
b1.Buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("verde", "monark", 2000, 189)
print(b2)