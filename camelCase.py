
def camelcase(sentence):
    title_case = sentence.title()
    upper_camel_cased = title_case.replace(' ','') #remove spaces
    return upper_camel_cased[0:1].lower() + upper_camel_cased[1:]

def instructions():
    print('Enter a sentence and this program will convert it to camelcase')


def banner():
    """"This is a banner for the camelcase program"""
    message = "awesome program!"
    stars = "*"* len(message)
    print(f'\n{stars}\n{message}\n{stars}')


def thankyou():
    print('Thank you for using the program!')

def main():
    banner()
    instructions()
    sentence = input ('Enter your sentence: ')
    output = camelcase(sentence)
    print(output)
    thankyou()

if __name__ == '__main__':
    main()