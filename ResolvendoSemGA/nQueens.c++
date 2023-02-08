
#include <iostream>
#include <vector>

int solucoes = 0;

void mostrarTabuleiro(std::vector<std::vector<int> > tab, int N){
	for(int i = 0; i < N; i++){
		for(int j = 0; j < N; j++)
		{
			if(tab[i][j] == 1)
				std:: cout << "R\t"; //R -> Rainhas
			else
				std:: cout << "-\t";
		}
		std:: cout << "\n\n";
	}
	std:: cout << "\n";
}

bool seguro(std::vector<std::vector<int> > tab, int N, int lin, int col){
	int i, j;

	// verifica se ocorre ataque na linha
	for(i = 0; i < N; i++) {
		if(tab[lin][i] == 1)
			return false;
	}

	//verifica se ocorre ataque na coluna
	for(i = 0; i < N; i++) {
		if(tab[i][col] == 1)
			return false;
	}

	// verifica se ocorre ataque na diagonal principal
	// acima e abaixo
	for(i = lin, j = col; i >= 0 && j >= 0; i--, j--){
		if(tab[i][j] == 1)
			return false;
	}
	for(i = lin, j = col; i < N && j < N; i++, j++){
		if(tab[i][j] == 1)
			return false;
	}

	// verifica se ocorre ataque na diagonal secundária
	// acima e abaixo
	for(i = lin, j = col; i >= 0 && j < N; i--, j++) {
		if(tab[i][j] == 1)
			return false;
	}
	for(i = lin, j = col; i < N && j >= 0; i++, j--) {
		if(tab[i][j] == 1)
			return false;
	}

	return true;
}


void executar(std::vector<std::vector<int> > tab, int N, int col){
	if(col == N){ 
		std::cout << "Solucao " << solucoes + 1 << ":\n\n" << std::endl;
		mostrarTabuleiro(tab, N);
		solucoes++;
		return;
	}

	for(int i = 0; i < N; i++){
		if(seguro(tab, N, i, col)) { 
			tab[i][col] = 1;

			executar(tab, N, col + 1);

			tab[i][col] = 0;
		}
	}
}

int main(int argc, char *argv[]){
	// número de rainhas
	int N = 8;

	// Matriz do tabuleiro
    std::vector<std::vector<int>> tab;
	// inserindo todas as linhas
	for(int i = 0; i < N; i++)
	{
		std::vector<int> linha(N);
		tab.push_back(linha);
	}

	// imprime todas as soluções
	executar(tab, N, 0);

	// imprime a quantidade de soluções
	std::cout << "\nEncontradas " << solucoes << " solucoes!\n"<<std::endl;

	return 0;
}