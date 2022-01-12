x = input("Enter your name: ")
lang = input("Enter your language: ")
def great(lang):
    if lang == 'es' :
        return "Hola"
    elif lang == 'fr' :
        return "Bonjur"
    else :
        return "Hello"
print(great(lang),x)
