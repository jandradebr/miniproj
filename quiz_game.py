'''
This script runs a quiz game, it can be easily edited for different questions, plus it can also add a variety of answers to each question
'''


from random import randint


question_bank = [
    { 'qu' : 'What famous scientist developed the theory of general relativity?', 'ans' : 'Albert Einstein'},
    { 'qu' : 'Which planet is known as the "Red Planet"?', 'ans' : 'Mars'},
    { 'qu' : 'Who painted the Mona Lisa?', 'ans' : 'Leonardo da Vinci'},
    { 'qu' : 'What is the largest mammal in the world?', 'ans' : 'Blue whale'},
    { 'qu' : 'In Greek mythology, who is the god of the sea??', 'ans' : 'Poseidon'},
    { 'qu' : 'What is the capital city of Japan?', 'ans' : 'Tokyo'},
    { 'qu' : 'Which famous playwright wrote Romeo and Juliet?', 'ans' : 'William Shakespeare'},
    { 'qu' : 'What is the chemical symbol for gold?', 'ans' : 'Au'},
    { 'qu' : 'What is the tallest mountain in the world?', 'ans' : 'Mount Everest'},
    { 'qu' : 'Who is the author of the Harry Potter book series?', 'ans' : 'J.K. Rowling'}
]

def main():
    
    num_q = int(input('How many questions you wanna have? (Max=10): '))
    score = 0

    q_used = []

    for i in range(0,num_q):

        q_id = randint(0,9)
        
        while q_id in q_used:
            q_id = randint(0,9)

        q_used.append(q_id)

        print(question_bank[q_id]['qu'])
        answer = input('Enter your answer: ')

        if answer == question_bank[q_id]['ans']: score += 1
    
    score_perc = int((score/num_q) * 100)

    print(f'You had {score} questions right with a {score_perc}% score')


main()