from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever

escritor = Escritor('Aldair')

caneta = Caneta('Bic')

maquina = MaquinaDeEscrever()

# associando
escritor.ferramenta = maquina
escritor.ferramenta.escrever()
