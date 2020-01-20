from django.shortcuts import render, redirect
import random

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'messages' not in request.session:
        request.session['messages'] = []
    if 'colors' not in request.session:
        request.session['colors'] = []

    context = {}
    context['gold'] = request.session['gold']
    context['messages'] = request.session['messages']

    return render(request, 'ninjaG/index.html', context)

def process_money(request):
    if request.method == 'POST':
        gold = request.session['gold']
        location = request.POST['location']

        if location == 'farm':
            gold = random.randint(10, 20)
        elif location == 'cave':
            gold = random.randint(5, 10)
        elif location == 'house':
            gold = random.randint(2, 5)
        else:
            gold = random.randint(-50, 50)

        if gold > 0:
            request.session['messages'].insert(0, 'You have earned ' + str(gold) + ' gold from the ' + location)
            request.session['colors'].insert(0, 'green')
        elif gold == 0:
            request.session['messages'].insert(0, 'You have broken even, left with ' + str(gold) + ' gold from the ' + location)
            request.session['colors'].insert(0, 'black')
        else:
            request.session['messages'].insert(0, 'You have lost ' + str(gold * -1) + ' gold from ' + location)
            request.session['colors'].insert(0, 'red')

        request.session['gold'] += gold

        return redirect('/')
