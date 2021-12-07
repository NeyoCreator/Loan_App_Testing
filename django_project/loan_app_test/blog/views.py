from django.shortcuts import render


#Dummy data 
posts = [
    {'author': 'Neo Sebanze',
    'title': 'Loan Application',
    'content': 'Need 700',
    'date_posted': 'August 27,2018'

    },

     {'author': 'Karabo Masemula',
    'title': 'Loan Application',
    'content': 'Need 200',
    'date_posted': 'August 30,2018'

    }

]


def home(request):
    context = {
        "posts":posts
        }
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html' )
       