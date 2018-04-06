#include <complex>
#include <iostream>
#include <cstdlib>
#include <omp.h>

using namespace std;

int main(int argc, char **argv) {
	int max_row, max_column, max_n;
	int i, r, c, n;
	
	if (argc != 5) {
		cout << "max_row:";    cin >> max_row;
		cout << "max_column:"; cin >> max_column;
		cout << "max_n:";      cin >> max_n;
	}
	else {
		int numThreads = atoi(argv[1]);
		if (numThreads != 2 && numThreads != 4 && numThreads != 8 && numThreads != 16) {
			cout << "Número de Threads não suportado!" << endl;
			exit(1);
		}
		omp_set_num_threads(numThreads);
		max_row    = atoi(argv[2]);
		max_column = atoi(argv[3]);
		max_n      = atoi(argv[4]);
	}

double inicio = omp_get_wtime();

	char *vet = (char *) malloc(sizeof(char) * max_row*max_column);

	#pragma omp parallel for shared(vet,max_column,max_row) private(i, r, c, n) schedule(dynamic)
	for (i = 0; i < max_row*max_column; ++i) {
		c = i % max_column;
		r = i / max_column;
		// cout << "r:" << r << " c:" << c << endl;
		n = 0;
		complex<float> z;
		while (abs(z) < 2 && ++n < max_n)
			z = pow(z, 2) + decltype(z)(
				(float)c * 2 / max_column - 1.5,
				(float)r * 2 / max_row - 1
			);
		vet[i] = (n == max_n ? '#' : '.');
	}

printf("Tempo\t %lf \n", omp_get_wtime() - inicio);

	for(i = 0; i < max_row*max_column; ++i) {
		cout << vet[i];
		if (i % max_column == max_column-1) cout << '\n';
	}
}


