#TRASFORMA APENAS A PRIMEIRA LETRA DE UMA STRING EM MAIUSCULA. 
nome = "Vinicius"
print(nome.capitalize(),"\n")

#TRANSFORMA TODAS AS LETRAS EM MINUSCULA.
nome = "VINICIUS"
print(nome.casefold(),"\n")

#CONTA O NUMERO DE VEZES QUE UM CARACTERE ESPECIFICO APARECE NA STRING.
nome = "ViniciusWilbert@gmail.com"
print(nome.count('i'),"\n")

#RETORNA TRUE (verdadeiro) OU false (falso) PARA UM TRSTE se A STRING TERMINA COM UMA STRING ESPECIFICA
nome = "ViniciusWilbert@gmail.com"
print(nome.endswith('gmail.com'),"\n")

#ENCONTA A POSIÇÃO DO TERMO PROCURADO LEMBRE-SE COMEÇA DO  zero
nome = "ViniciusWilbert@gmail.com"
print(nome.find('@'),"\n")

#VERIFICA SE O TEXTO É todo FEITO COM LETRAS.
nome ="Vinicius"
print(nome.isalpha(),"\n")

#VERIFICA SE O TEXTO É FEITO COM numeros.
nome = "123"
print(nome.isnumeric(),"\n")

#SUBSTITUI UM CARACTERE ESCOLHIDO POR OUTRO
nome = "Vinicius"
print(nome.replace('u','y'),"\n")

#SEPARA O TEXTO string  BASEADO EM ALGUM CARACTERE INDICADO.
nome = "Vinicius @ haskel Wilbert"
print(nome.split('@'),"\n")

#COLOCAR TODAS AS LETRAS INICIAIS EM maiuscula.
nome = "Vinicius Haskel Wilbert"
print(nome.title(),"\n")

#RETIRA OS CARACTERES INDEJADOS, COMO POR EXEMPLO espaços QUE NAO AGRAGAR VALOR.
nome = "  Vinicius Haskel Wilbert  "
print(nome.strip(),"\n")

#RETORNA true OU false PARA UM TESTE DE UMA STRING SE INICIA COM UM TEXTO ESPECIFICO.
nome = "Vinicius 2007"
print(nome.startswith("ser"),"\n")
print(nome.startswith("ser"),"\n")