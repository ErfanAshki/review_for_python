def meaning(dict):
    dict['mean'] = 'motaham kardan'
    return dict
    
    
word = {
    'word1': 'criminate',
    'word2': 'accuse',
    'word3': 'indict'
}

print(word)
meaning(word.copy())
print(meaning(word.copy()))
print(word)

