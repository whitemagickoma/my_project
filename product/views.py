from django.shortcuts import render

posts = [
    {
        'author': 'Kamron',
        'name': 'coral-mine',
        'amount': '5'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'product/index.html', context)
