from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    if request.method == "POST":
        print(request.POST)
        return redirect("/result")

    if request.method == "GET":
        print(request.GET)
        return render(request, "index.html")


def result(request):
    if request.method == "POST":
        print(request.POST)
        context = {
            'name' : request.POST['name'],
            'dojo' : request.POST['dojo'],
            'comment' : request.POST['comment']
        }

        return render(request, "result.html", context)
    
    if request.method == "GET":
        return redirect("/")