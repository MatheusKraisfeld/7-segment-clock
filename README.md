# Relógio com display de 7 segmentos

A solução foi implementada de maneira a ser simples, sem abusar de estruturas que dificultem o entendimento do raciocínio. Basicamente, cada algarismo do horário foi tratado separadamente como uma lista de strings. O objetivo disso foi no momento da impressão, conseguir imprimir linha a linha de todos os algarismos lado a lado formando o relógio. A solução foi possível devido ao tamanho ser igual para todos
 os algarismos, dada a entrada do usuário, logo ao concatenar a linha 0 de todos  os algarismos em ordem, conseguimos visualizar a linha 0 do relógio completo e assim por diante. Para tornar possível a entrada de dados em tempo de execução, foi utilizado paralelismo de forma que uma thread ficou responsável apenas pela leitura da entrada.

## Requisitos

Para o funcionamento correto, o programa deve ser executado em sistema Linux, com versão 2.7 do Python.

## Instalação e execução

Primeiramente, deve-se executar o seguinte comando no terminal:

```bash
chmod +x studio_sol.sh
```
Com a permissão de execução adicionada para o script, basta executá-lo no mesmo diretório dos demais arquivos como a seguir:

```
./studio_sol.sh
```
A entrada do programa consiste de um número inteiro entre 1 e 5, seguido de Enter. Números fora desse intervalo interrompem o programa, e qualquer caractere diferente dos citados não afeta a execução.

## Autor
Matheus Kraisfeld Benevides de Lima
 
Estudante do Curso de Ciência da Computação

PUC Minas - Coração Eucarístico

Belo Horizonte, Minas Gerais

## Suporte / Contato
E-mail: matheuskraisfeld@gmail.com

