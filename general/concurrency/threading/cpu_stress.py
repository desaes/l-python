from concurrent.futures import thread
import datetime
import math

import threading
import multiprocessing

def main():
    qtd_cores = multiprocessing.cpu_count()
    print(f'Realizando processamento com {qtd_cores} core(s)')
    inicio = datetime.datetime.now()

    threads = []
    for n in range(1, qtd_cores + 1):
        ini = 50_000_000 * (n-1) / qtd_cores
        fim = 50_000_000 * n / qtd_cores
        print(f'Core {n} processando de {ini} ate {fim}')
        threads.append(
            threading.Thread(
                target=computar, 
                kwargs={'inicio': ini, 'fim': fim},
                daemon=True
            )
        )

	#computar(fim=50_000_000) # Python3
    #computar(fim=50000000) # Python2
    [th.start() for th in threads]
    [th.join() for th in threads]

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
Terminou em 16.46 segundos.
"""
