#created by me
from django.http import HttpResponse
from  django.shortcuts import render

def index(request):

    return render(request,'index.html')

def analyse(request):
    djtext = request.POST.get("text", "default")
    djcheck=request.POST.get("checkbox","off")
    djextra = request.POST.get("checkextra", "off")
    newline=request.POST.get("checknew","off")
    upper=request.POST.get("upper","off")
    analysed_text=""


    if djcheck=="on":
        punc="""<,.>?/:;"'[{-_)*&^%$#@!~`"""
        analysed_text = ""
        for i in djtext:
            if i not in punc:
                analysed_text=analysed_text+i
        djtext=analysed_text


    if djextra=="on":
        analysed_text = ""
        for index ,char in enumerate(djtext):
            if not(djtext[index]==" "and djtext[index-1]==" "):
                analysed_text=analysed_text+char
        djtext = analysed_text

    if newline=="on":
        analysed_text = ""
        for char in djtext:
            if char !="\n" and char !="\r":
                analysed_text=analysed_text+char
        djtext = analysed_text

    if upper=="on":
        analysed_text = ""
        for char in djtext:
            analysed_text=analysed_text+char.upper()

    param={"name":"Analysed text","analyse":analysed_text}

    if (upper!="on" and newline!="on" and djextra!="on" and djcheck!="on" ):
        return HttpResponse("Error ")
    return render(request,"analyse.html",param)




