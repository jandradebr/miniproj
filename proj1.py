from random import randint


def player_turn(player_score, max):

    score = 0

    while True:

        option = input('(R)oll the dice or (H)old? ')

        if option not in ('R','H','r','h'):
            print('Input not recognized... Try again')
            continue

        elif option in ('H','h'):
            print(f'Your score for this turn is {score}')
            break

        dice = randint(1,6)

        if dice==1:
            score = 0
            print('You got 1... You lose all your points for this turn :(')
            return 0

        score += dice

        print(f'You got {str(dice)}')

        print(f'Your score for this turn is {score} and your total is {score + player_score}')

        if score + player_score >= max: return score
    
    return score

def player_set():

    player_num = int(input('How many players are playing?' ))

    if player_num < 2:

        print('At least 2 players are required.')
        player_set()

    player_s = [0]*player_num
    
    return player_s, player_num

def main():

    scores, player_num = player_set()
    max = int(input("What's the score to win? "))

    while True:

        for i in range(0, player_num):

            print(f'Go ahead player {i+1}:')
            scores[i] += player_turn(scores[i],max)
            print(f'Player {i+1} your total score is {scores[i]}')

            if scores[i] >= max:
                print(f'Winner is player {i+1} with {scores[i]} points!!!')
                return 0
            
main()