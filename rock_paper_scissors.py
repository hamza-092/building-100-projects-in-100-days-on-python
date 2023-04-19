import random
user_choice = int(input('select 0 for rock, 1 for paper, 2 for scissors ? '))
computer_choice = random.randint(0,2)
print(f'you chose {user_choice} and computer chose {computer_choice}')
if user_choice == computer_choice:
    print('Its a Draw ! ')
elif user_choice == 0 and computer_choice == 1:
    print('You lose ! ')
elif user_choice == 0 and computer_choice ==2:
    print('You Win ! ')
elif user_choice == 1 and computer_choice == 2:
    print('You Lose ! ')
elif user_choice == 1 and computer_choice == 0:
    print('You Win ! ')
elif user_choice == 2 and computer_choice == 0:
    print('You Lose ! ')
elif user_choice == 2 and computer_choice == 1:
    print('You Win ! ')
else:
    print('Incorrect number. Try again ! ')