# from django.views.generic import TemplateView

# class login(TemplateView):
#     template_name='login.html'


# class register(TemplateView):
#     template_name = 'register.html'




from django.shortcuts import render


person = {'name': 'Alireza'}

def login(request):
    return render(request,'login.html',context=person)


def register(request):
    return render(request,'register.html')