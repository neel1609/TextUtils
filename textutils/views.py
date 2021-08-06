from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def analyze(request):



    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    upper = request.POST.get('upper', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    spaceremove = request.POST.get('spaceremove', 'off')
    charcount = request.POST.get('charcount', 'off')

    # paras = None
    if removepunc == 'on':

        punctuation = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuation:
                analyzed = analyzed + char

        paras = {'purpose': 'without punctuation', 'result': analyzed}
        djtext = analyzed


    if upper == 'on':
        analyzed = djtext.upper()
        paras = {'purpose': 'after converting to uppercase', 'result': analyzed}
        djtext = analyzed

    if newlineremove == 'on':

        analyzed = ''
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char

        paras = {'purpose': 'After merging to single line', 'result': analyzed}
        djtext = analyzed

    if spaceremove == 'on':

        analyzed = ''

        for ind,char in enumerate(djtext):
            '''here i have not used djtext[index]!='' and djtext[index+1]!='' because this will give string out of bound error
             because if last char index is 4 then index+1 =5 which doesn't exist but since slicing doesn't give erron like that 
             because if last value is out of range in slice then it considers last value by default'''
            if not (djtext[ind:ind + 2] == "  "):
                analyzed += char
        djtext = analyzed
        paras = {'purpose': 'After removing the space', 'result': analyzed}


    if charcount == 'on':
        counter = 0

        for char in djtext:
            if char != ' ' and char != '\r' and char != '\n':
                counter += 1

        paras = {'purpose': 'characters count number', 'result': djtext + "\n No of characters: " + str(counter)}
        return render(request, 'analyze.html', paras)

    if (removepunc != 'on' and newlineremove != 'on' and upper != 'on' and spaceremove != 'on' and charcount != 'on'):
        return HttpResponse("please select any operations and try again!")

    return render(request, 'analyze.html', paras)
