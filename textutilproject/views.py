from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'home.html')

def analyze(request):
    # POST the text
    djtext = request.POST.get('text', 'default')

    # Check Checkbox values
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    lowercase=request.POST.get('lowercase','off')
    newlineremover=request.POST.get('newlineremover','off')
    capfirst=request.POST.get('capfirst','off')
    removespace=request.POST.get('removespace','off')
    charcount=request.POST.get('charcount','off')
    removenum=request.POST.get('removenum','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')

    # Remove Punctuation
    if removepunc == 'on':
        analyzed = ''
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': "Removing Punctuations", 'analyzed_text': analyzed,}
        # return render(request, 'analyze.html', params)
        djtext=analyzed
    # Upper Case Letter
    if fullcaps == 'on':
        analyzed = ''
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': "Upper Case", 'analyzed_text': analyzed, }
        # return render(request, 'analyze.html', params)
        djtext=analyzed

    # lower case
    if lowercase == 'on':
        analyzed = ''
        for char in djtext:
            analyzed = analyzed + char.lower()
        params = {'purpose': "Lower Case", 'analyzed_text': analyzed, }
        # return render(request, 'analyze.html', params)
        djtext=analyzed


    # newlineremover
    if newlineremover == 'on':
        analyzed = ''
        for char in djtext:
            if char != '\n' and char!='\r':
                analyzed = analyzed + char
        params = {'purpose': "Removed New Line", 'analyzed_text': analyzed, }
        # return render(request, 'analyze.html', params)
        djtext=analyzed


    # capfirst
    if capfirst == 'on':
        analyzed = djtext.title()
        params = {'purpose': "Capital First Character", 'analyzed_text': analyzed, }
        # return render(request, 'analyze.html', params)
        djtext=analyzed

    # removespace
    if removespace == 'on':
    # if removespace == 'on':
        analyzed = ''
        for char in djtext:
            if char != ' ':
                analyzed = analyzed + char
        params = {'purpose': "Remove Space", 'analyzed_text': analyzed, }
        # return render(request, 'analyze.html', params)
        djtext=analyzed

    # Count character
    if charcount == 'on':
        analyzed = len(djtext)
        params = {'purpose': "Count Characters", 'analyzed_text': analyzed, }
        # return render(request, 'analyze.html', params)
        djtext=analyzed


    # Remove Number
    if (removenum == 'on'):
        analyzed = ''
        for char in range(len(djtext)):
            if djtext[char].isdigit():
                pass
            else:
                analyzed = analyzed + djtext[char]
        params = {'purpose': "Count Characters", 'analyzed_text': analyzed, }
        # return render(request, 'analyze.html', params)
        djtext=analyzed

    # Remove Extra Space
    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index + 1] == " ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'Remove Extra Space', 'analyzed_text': analyzed}


    if(extraspaceremover!='on' and removenum!='on' and charcount!='on' and removespace!='on' and capfirst!='on' and
    newlineremover!='on' and lowercase != 'on' and fullcaps != 'on' and removepunc != 'on'):

        return HttpResponse("Please select atleast one option")
    # Analyze the text
    return render(request, 'analyze.html', params)






