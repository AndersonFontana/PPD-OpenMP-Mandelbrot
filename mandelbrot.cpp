#include <complex>
#include <iostream>
#include <cstdlib>
#include <omp.h>

using namespace std;

int main(int argc, char **argv) {
	int max_row, max_column, max_n;

	if (argc != 4) {
		cin >> max_row;
		cin >> max_column;
		cin >> max_n;
	}
	else {
		max_row    = atoi(argv[1]);
		max_column = atoi(argv[2]);
		max_n      = atoi(argv[3]);
	}

double inicio = omp_get_wtime();

	char **mat = (char**)malloc(sizeof(char*)*max_row);

	for (int i=0; i<max_row;i++)
		mat[i]=(char*)malloc(sizeof(char)*max_column);

	for(int r = 0; r < max_row; ++r) {
		for(int c = 0; c < max_column; ++c) {
			complex<float> z;
			int n = 0;
			while(abs(z) < 2 && ++n < max_n)
				z = pow(z, 2) + decltype(z)(
					(float)c * 2 / max_column - 1.5,
					(float)r * 2 / max_row - 1
				);
			mat[r][c]=(n == max_n ? '#' : '.');
		}
	}

printf("Tempo\t %lf \n", omp_get_wtime() - inicio);

	for(int r = 0; r < max_row; ++r){
		for(int c = 0; c < max_column; ++c)
			cout << mat[r][c];
		cout << '\n';
	}
}


