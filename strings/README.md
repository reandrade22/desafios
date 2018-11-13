# Desafio 1: Strings

O script split_and_justify.py tem como objetivo dividir um texto de entrada em N caracteres por linha e salva-lo em um arquivo de saída de forma justificada. Palavras não são quebradas e quando em um linha cabe apenas uma única palavra, a mesma será justificada à esquerda. Quando N for menor do que o comprimento da maior palavra do texto, o arquivo de saída não será gerado.

O script necessita de 3 parâmetros:
1. -i/--input   : Path para o arquivo texto de input
2. -o/--output  : Path para o local onde o arquivo deve ser salvo, assim como seu nome
3. -c/-chars    : Número máximo de carcteres em um linha do arquivo.

### Exemplo de execução:

`python split_and_justify.py -c 20 -i inputs/example_input.txt -o example_output.txt`

No exemplo acima, o texto do arquivo example_input.txt é dividido em linha de no máximo 20 caracteres e a saída justificada é salva em example_output.txt
