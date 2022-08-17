import datetime
import math

def main():
	inicio = datetime.datetime.now()

	#computar(fim=50_000_000) # Python3
	computar(fim=50000000) # Python2

	tempo = datetime.datetime.now() - inicio

	#print(f"Terminou em {tempo.total_seconds():.2f} segundos.") # Python3
	print("Terminou em {tempo:.2f} segundos.".format(tempo=tempo.total_seconds())) # Python2

def computar(fim, inicio=1):
	pos = inicio
	fator = 1000 * 1000
	while pos < fim:
		pos += 1
		math.sqrt((pos - fator) * (pos - fator))

if __name__ == '__main__':
	main()

"""
Terminou em 9.03 segundos.
"""
