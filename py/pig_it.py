from string import punctuation


def pig_it(text):
    tmp = text.split()
    result = []
    for i in tmp:
        if i in punctuation:
            result.append(i)
            continue
        result.append(f'{i[1::]}{i[0]}ay')
    return ' '.join(result)



pig_it('Quis custodiet ipsos custodes ?')


'''Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool')  igPay atinlay siay oolcay
pig_it('Hello world !')      elloHay orldway !'''
