from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
#Handles the various webpages

def home_view(request, *args, **kwargs):
    print(*args, **kwargs)
    print(request.user)
    #return HttpResponse("<h1>Hello World!</h1>") #String of html code
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Contact Page")
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
    #return HttpResponse("<h1>About the User ")
    my_context = {
        "abc" : "312",
        "my_text" : "This is about me",
        "my_number" : '1231',
        "my_list" : [122, 332, 312, "Abc"]
    }
    return render(request, "about.html", my_context)

def social_view(request, *args, **kwargs):
    return HttpResponse("<h1>SOCIAL PAGE</h1>")

"""
return render(request, <template>, <context>)
"""