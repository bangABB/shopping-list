from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Bil Bepe',
        'class': 'PBP A - Asdos adjie Overpawer'
    }

    return render(request, "main.html", context)