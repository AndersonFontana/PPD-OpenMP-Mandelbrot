#!/usr/bin/env python3

'''
	Script para disciplina de Programação Paralela e Distribuída
	                                    by: Anderson A. Fontana
	Parar: Ctrl+C
'''

import subprocess, re

##  Variáveis  ##############################################

THRDs = [2, 4, 8, 16]
MAX_ROWs    = [1024]#[50, 200, 500]#, 900,  1500]
MAX_COLUMNs = [768]#[60, 300, 400]#, 1000, 1600]
MAX_Ns = [18000]#[1000, 10000]#, 100000]
timesToRun = 5

pSequent = "mandelbrot"
pParallel = "mandelbrotParallel"

##############################################################

# Retorna o tempo em segundos
def getRunTime(output):
	tempo = re.findall(r'Tempo\s+(\d+\.\d+)', output)[0]
	return float(tempo)

# Retorna o speedup e a eficiência
def getStats(time, timeSeq, threads=1):
	speedUp = timeSeq/time
	efficiency = speedUp/threads
	return (speedUp, efficiency)

# Faz a média de $numOfRuns execuções
def execCommandNTimes(cmd, numOfRuns):
	avg = 0
	output = ''
	for i in range(0, numOfRuns):
		output = subprocess.getoutput(cmd)
		time = getRunTime(output)
		avg += time
		print("(#{}: {:.4f})".format(i+1, time))

	time = avg/numOfRuns
	print("avg: {:.4f}".format(time))

	return time, re.sub(r'Tempo\s+(\d+\.\d+)', '', output)

print (__doc__)

# Compila os fontes
subprocess.run("g++ " + pSequent  + ".cpp -o " + pSequent  + " -fopenmp -std=c++11", shell=True)
subprocess.run("g++ " + pParallel + ".cpp -o " + pParallel + " -fopenmp -std=c++11", shell=True)

outFile = open('tempos', 'w')

for i in range(0, len(MAX_ROWs)): # ou MAX_COLUMNs, pois len(MAX_ROWs) == len(MAX_COLUMNs)
	print("\n\n", file=outFile)
	for MAX_N in MAX_Ns:

		# Executa o programa sequêncial
		cmd = "./" + pSequent + " " + str(MAX_ROWs[i]) + " " + str(MAX_COLUMNs[i]) + " " + str(MAX_N)
		print("\n" + cmd)
		timeSeq, outputSeq = execCommandNTimes(cmd, timesToRun)

		# Mostra o cabeçalho da execução atual e os dados da execução sequêncial
		print('\n\t MAX_ROW= {}\t MAX_COLUMN= {}\t TAM= {}'.format(MAX_ROWs[i], MAX_COLUMNs[i], MAX_N), file=outFile)
		print('{:<10}\t{:<10}\t{:<10}\t{:<10}'.format('Threads', 'Tempo', 'SpeedUp', 'Eficiência'), file=outFile)
		print('{:<10}\t{:<10.4f}\t{:<10.4f}\t{:<10.4f}'.format('seq', timeSeq, 1, 1).replace(".",","), file=outFile)

		# Para cada número de Threads
		for THRD in THRDs:
			cmd = "./" + pParallel + " " + str(THRD) + " " + str(MAX_ROWs[i]) + " " + str(MAX_COLUMNs[i]) + " " + str(MAX_N)

			print(cmd)
			time, outputParallel = execCommandNTimes(cmd, timesToRun)

			if outputSeq != outputParallel:
				print(outputSeq, open('outputSeq', 'w'))
				print(outputParallel, open('outputParallel', 'w'))
				print("\n\n\n  Saidas diferentes!!!  \n\n\n")
				exit(1)

			# Calcula e mostra algumas estatísticas da execução paralela, como tempo, speedup e eficiência;
			sp, ef = getStats(time, timeSeq, THRD)
			print('{:<10}\t{:<10.4f}\t{:<10.4f}\t{:<10.4f}'.format(THRD, time, sp, ef).replace(".",","), file=outFile)
