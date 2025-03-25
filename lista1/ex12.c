#include<stdio.h>
int main() {int rm;printf("Digite o rm: ");scanf("%d", &rm);int soma = 0;int resto = rm % 10;
    soma = soma + resto;
    rm = rm / 10;

    resto = rm % 10;
    soma = soma + resto;
    rm = rm / 10;

    resto = rm % 10;
    soma = soma + resto;
    rm = rm / 10;

    printf("A soma vale %d", soma)
}