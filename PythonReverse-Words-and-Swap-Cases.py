def reverse_words_order_and_swap_cases(sentence):
    # Write your code here
    s = ''
    for i in sentence.split(' '):
        s += i [::-1] + ' '
    return s[-2::-1].swapcase()