'''
Utilizando a linguagem python, implemente a classe e o objeto que você pensou na aula passada.
Dica: 
1.A classe tem que ter pelo menos um atributo mutável.
2. Os métodos devem ter relação com algum atributo mutável.
'''

class fone_de_ouvido:
# Atributos
    estado = None
    bluetooth = None
    volume_atual = None
    volume_maximo = 100
    modelo = None
    marca = None
    ano = None
    cor = None

# Métodos

    def ligar(self, estado):
        self.estado = "ligado"
        self.bluetooth = "ativado"
        print(f"O fone {self.modelo} está {self.estado}. ao dispositivo: ")
        import platform
        print(platform.node())

    def alm_vol(self, volume_atual):
        if self.estado == "ligado" and self.volume_atual < self.volume_maximo:
            self.volume_atual += 1
            print(f"O volume atual é: {self.volume_atual}")
        else:
            print(f"O estado atual é : {self.estado}, ligue o fone, ou então diminua o volume, pois está no máximo.")

    def dim_vol(self, volume_atual):
        if self.estado == "ligado" and self.volume_atual < self.volume_maximo:
            self.volume_atual -= 1
            print(f"O volume atual é: {self.volume_atual}")
        else:
            print(f"O estado atual é : {self.estado}, ligue o fone, ou então aumente o volume, pois está zerado.")


# Objeto
            
objeto1 = fone_de_ouvido()
objeto1.estado = "desligado"
objeto1.bluetooth = "desativado"
objeto1.volume_atual = 50
objeto1.volume_maximo = 100
objeto1.modelo = "QCY T17"
objeto1.marca = "Philips"
objeto1.ano = "2022"
objeto1.cor = "Branco"


# Testando comportamentos
# O volume só aumenta e diminui de 1 em 1
objeto1.ligar("desligado")
objeto1.alm_vol(1)
objeto1.alm_vol(1)
objeto1.dim_vol(1)