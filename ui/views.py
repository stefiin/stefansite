from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "index.html")
def ibm(request):
    return render(request, "ibm.html")
def atomic(request):
    return render(request, "atomic.html")
def csip(request):
    return render(request, "csip.html")
def soccer(request):
    return render(request, "soccer.html")
def centivizer(request):
    return render(request, "centivizer.html")
def mentor(request):
    return render(request, "mentor.html")
def app(request):
    return render(request, "app.html")
def raven(request):
    return render(request, "raven.html")
def etec(request):
    return render(request, "etec.html")
def laneway(request):
    return render(request, "laneway.html")
def snowboard(request):
    return render(request, "snowboard.html")
def taxi(request):
    return render(request, "taxi.html")
def finance(request):
    return render(request, "finance.html")
def papers(request):
    return render(request, "papers.html")

