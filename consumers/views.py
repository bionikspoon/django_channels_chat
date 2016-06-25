from django.shortcuts import render


def index(request):
    # request.session['session_key'] = 'abcd'
    return render(request, 'index.html')
