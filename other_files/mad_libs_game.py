text_1 = 'This is a/an {adjective 1} version of a Mad Libs Game,'

text_2 = 'you can add {adjective 2} words and use them in different ways.'

text_3 = 'We encourage you to {verb 1} what your {noun 1} has to say.'

text_4 = 'If you like {color} {noun 2} I guess you should like {plural noun 1} too.'

text_5 = 'Thanks for that {noun 3}, we hope you have a/an {adjective 3} {noun 4} and {verb 2} each of your {plural noun 2}'


def insert_words(adj_1, adj_2, verb_1, noun_1, color, noun_2, plur_noun_1, noun_3, adj_3, noun_4, verb_2, plur_noun_2):
    
    print(f'This is a/an {adj_1} version of a Mad Libs Game, ')
    print(f'you can add {adj_2} words and use them in different ways. ')
    print(f'We encourage you to {verb_1} what your {noun_1} has to say.')
    print(f'If you like {color} {noun_2} I guess you should like {plur_noun_1} too.')
    print(f'Thanks for that {noun_3}. We hope you have a/an {adj_3} {noun_4} and {verb_2} each of your {plur_noun_2}')


def run():

    print(text_1, text_2, text_3, text_4, text_5)
    print('*' * 60, '\n')

    adjective_1 = input('Enter adjective 1: ')
    adjective_2 = input('Enter adjective 2: ')
    verb_1 = input('Enter verb 1: ')
    noun_1 = input('Enter noun 1: ')
    color = input('Enter color: ')
    noun_2 = input('Enter noun 2: ')
    plural_noun_1 = input('Enter plural noun 1: ')
    noun_3 = input('Enter noun 3: ')
    adjective_3 = input('Enter adjective 3: ')
    noun_4 = input('Enter noun 4: ')
    verb_2 = input('Enter verb 2: ')
    plural_noun_2 = input('Enter plural noun 2: ')

    insert_words(adjective_1, adjective_2, verb_1, noun_1, color, noun_2, plural_noun_1, noun_3, adjective_3, noun_4, verb_2, plural_noun_2)


if __name__ == '__main__':
    run()