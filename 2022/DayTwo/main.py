'''
Rock, Paper, Scissor
A, B, C;
X, Y, Z
1, 2, 3
lose, draw, win
0, 3, 6
'''

DIGIT_SCORE = {
    'X':1, 'Y':2, 'Z':3
}
X = { 'A': 3, 'B' : 0, 'C' : 6}
Y = { 'A': 6, 'B' : 3, 'C' : 0}
Z = { 'A': 0, 'B' : 6, 'C' : 3}

## Change of strategy, now x, y, z are lose draw, win

DIGIT_SCORE_2 = {
    'X':0, 'Y':3, 'Z':6
}
X_2 = { 'A': 3, 'B' : 1, 'C' : 2}
Y_2 = { 'A': 1, 'B' : 2, 'C' : 3}
Z_2 = { 'A': 2, 'B' : 3, 'C' : 1}

def score(opponent, me):
    result = DIGIT_SCORE_2[me]
    if me == 'X':
        result += X_2[opponent]
    elif me == 'Y':
        result += Y_2[opponent]
    elif me == 'Z':
        result += Z_2[opponent]
    return result

def final_score(f_name):
    with open(f_name, 'r') as f:
        result = 0
        for item in f:
            game = item.strip("\n").split(" ")
            # print(game)
            assert len(game) == 2, f'The length of the split list is {len(game)}'
            oppo, me = game[0], game[-1]
            assert type(oppo) == str and type(me) == str, 'The type of data is wrong.'
            result += score(oppo, me)
    return result



if __name__ == '__main__':
    filename = 'data.txt'
    print(final_score(filename))
    # print(score("A", "Y"))
