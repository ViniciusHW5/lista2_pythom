def get_data():
    nome_usuario =input("escreva seu nome ")
    idade_usuario = int(input("Quero a sua idade? "))
    Tuple_data = (nome_usuario, idade_usuario)
    return Tuple_data
def mensagem(nome_usuario,idade_usuario):
    if idade_usuario <=10:
        print("oi",nome_usuario)
    else:
        print("Olá!", nome_usuario)
def main ():
    nome_usuario,idade_usuario = get_data()
    mensagem(nome_usuario,idade_usuario)
main()