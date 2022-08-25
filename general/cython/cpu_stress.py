import datetime
import compute

def main():
	inicio = datetime.datetime.now()

	#computar(fim=50_000_000) # Python3
	compute.compute(end=50000000) # Python2

	tempo = datetime.datetime.now() - inicio

	#print(f"Terminou em {tempo.total_seconds():.2f} segundos.") # Python3
	print("Terminou em {tempo:.2f} segundos.".format(tempo=tempo.total_seconds())) # Python2

if __name__ == '__main__':
	main()

"""
cpython -> with standard python types and library -> Terminou em 5.81 segundos.
cpython -> with c types and c library -> Terminou em 0.15 segundos.
cpython -> with c types, c library and nogil ->Terminou em 0.17 segundos.
"""