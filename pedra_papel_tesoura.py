import random

win_user = 0
win_computador = 0

opcoes = ['pedra', 'papel', 'tesoura']


while True:
    user_input = input('Escolha Pedra/Papel/Tesoura ou S para sair: ').lower()
    
    if user_input == 's':
        break
    
    if user_input not in opcoes:
        continue

    num_random = random.randint(0, 2)
    # Pedra: 0, Papel: 1, Tesoura: 2
    guess_computador = opcoes[num_random]
    print('O computador escolheu', guess_computador + ".")

    if user_input == 'pedra' and guess_computador == 'tesoura':
        print('Você ganhou!')
        win_user += 1

    elif user_input == 'pedra' and guess_computador == 'pedra':
        print('Empate! Jogue novamente')
        win_user += 0
      
    elif user_input == 'papel' and guess_computador == 'pedra':
        print('Você ganhou!')
        win_user += 1

    elif user_input == 'papel' and guess_computador == 'papel':
        print('Empate! Jogue novamente')
        win_user += 0
     
    elif user_input == 'tesoura' and guess_computador == 'papel':
        print('Você ganhou!')
        win_user += 1
        
    elif user_input == 'tesoura' and guess_computador == 'tesoura':
        print('Empate! Jogue novamente')
        win_user += 0
        
    else:
        print('Você perdeu!')
        win_computador += 1

print('Você ganhou', win_user, 'vezes.')
print('O computador ganhou', win_computador, 'vezes.')
print('Até mais!')
