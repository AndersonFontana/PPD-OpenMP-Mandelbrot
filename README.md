# Mandelbrot em OpenMp

## Programação Paralela e Distribuída

Por: Anderson Antonio Fontana


### Compilação

```
	g++ mandelbrotParallel.cpp -o mandelbrotParallel -fopenmp -std=c++11
```


### Execução Manual

```
	./mandelbrotParallel 2 1024 768 18000   // Para execução com 2 threads
	./mandelbrotParallel 4 1024 768 18000   // Para execução com 4 threads
	./mandelbrotParallel 8 1024 768 18000   // Para execução com 8 threads
	./mandelbrotParallel 16 1024 768 18000  // Para execução com 16 threads
```


### Execução Automática

```
	python3 autoMandel.py
```


Porém é preciso abrir o script e configurar algumas variáveis, como mostrado abaixo:

```
	##  Variáveis  ##############################################

	THRDs = [2, 4, 8, 16] 				// Quais threads serão utilizadas nos testes
	MAX_ROWs    = [50, 200, 500, 1024]	// Numeros de Linhas a serem usadas
	MAX_COLUMNs = [60, 300, 400, 768]	// Numeros de Colunas a serem usadas
	MAX_Ns = [1000, 10000, 18000]		// Tamanho do N nas iterações
	timesToRun = 5

	pSequent = "mandelbrot"				// Nome do programa Sequencial a ser usado (sem o .cpp)
	pParallel = "mandelbrotParallel"	// Nome do programa Paralelo a ser usado (sem o .cpp)
```
Além do resultado em tempo de execução o script *autoMandel.py* mostra uma saída com algumas estatísticas no arquivo "tempos".
