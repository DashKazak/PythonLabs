from email import message


def camelcase(sentence):
    title_case = sentence.title()
    upper_camel_cased = title_case.replace(' ','') #remove spaces
    return upper_camel_cased[0:1].lower() + upper_camel_cased[1:]

def banner():
    """"Display program name"""
    message = "awesome program!"
    stars = "*"* len(message)
    print(f'\n{stars}\n{message}\n{stars}')


def main():
    banner()
    sentence = input ('Enter your sentence: ')
    output = camelcase(sentence)
    print(output)

if __name__ == '__main__':
    main()