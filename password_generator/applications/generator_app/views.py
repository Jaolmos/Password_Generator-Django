from django.shortcuts import render
import random


def home(request):
    ''' Vista de la pagina principal '''
    return render(request, 'generator_app/home.html')


def password(request):
    ''' Vista donde se genera un nuevo password '''
    characters = list('abcdefghijklmnñopqrstuvwxyz')
    generated_password = ''

    lenght = int(request.GET.get('lenght'))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'))
    if request.GET.get('special-char'):
        characters.extend(list('\|@#~€¬!·$%&/()^<>'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    for i in range(lenght):
        # Se añade letras aleatorias de characters a la variable generated_password
        generated_password += random.choice(characters)

    return render(request, 'generator_app/password.html', {'password': generated_password})
