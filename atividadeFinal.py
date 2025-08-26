print("#########################")
print("# Jogo final #")

comidas = ["Macarrão", "Arroz", "Feijão", "Salada", "Carne"]

print("Lista de Comidas:")
for i in range(len(comidas)):
    print(f"{i + 1} - {comidas[i]}")
posicao_sorteada = random.randint(1, 5)

palpite = input("Qual comida você acha que está na posição sorteada? ")

print("Quais os níveis de dificuldade")
print("(1)- Fácil (2)- Médio (3)- Difícil ")

nivel = int(input("Escolha um nível: "))

if(nivel = 1)
print("25 tentativas")
tentativasTotal = 25
elif (nivel = 2):
print("15 tentativas")
tentativasTotal= 15
elif(nivel = 3):
print("5 tentativas")
tentativasTotal = 5
else:
print("numero incorreto")

if palpite.capitaliz() = comida_correta:
    print("Boa!")
    print(f"A comida na posição {posicao_sorteada} era realmente {comida_correta}")
else:
    print("Incorreto")
    print("A comida na {posicao_sorteada} é {comida_correta}")
