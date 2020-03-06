#Find the first letter not repeated inside a given word

def find_letter(word):
    letters_list = list(word)
    #print(letters_list)
    repeated_letters = []
    letters_counter = []


    for letter in letters_list:
        for i in range(len(letters_list)):
            if letter == letters_list[i] and letter not in repeated_letters:
                repeated_letters.append(letter)


    for repeated_letter in repeated_letters:
        counter = 0
        for letter in letters_list:
            if repeated_letter == letter:
                counter += 1
        letters_counter.append(counter)

    #print(letters_counter)
    #print(repeated_letters)


    for index, n in enumerate(letters_counter):
        if n == 1:
            return repeated_letters[index]


def select_option():
    print("""\nSelect one option:
    F) Find the first non repeated letter in one word
    E) EXIT""")

    option = None
    while not option:
        option = input('Enter your choise: ')
    return option


def main():

    while True:

        op = select_option()

        if op.upper() == 'F':

            word = input('Enter a word: ')
            letter = find_letter(word)
            if letter:
                print('\n{} is the first letter not repeated in the word\n'.format(letter.upper()))
            else:
                print('\nAll letters appears at least two times in the word\n')

        elif op.upper() == 'E':
            break

        else:
            print('\nPlease, select a valid option!\n')

if __name__ == '__main__':
    main()
