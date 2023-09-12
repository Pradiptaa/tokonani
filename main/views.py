from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'App Name': 'tokonani',
        'Name': 'Pradipta Arya Pramudita',
        'Class': 'PBP F'
    }

    return render(request, "main.html", context)