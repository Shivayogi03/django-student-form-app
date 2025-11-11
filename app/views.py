# from django.shortcuts import render
# from app.forms import *


# def student_Dj_form(request):
#     STDDJF=StudentDjForm()
#     d={'STDDJF':STDDJF}
#     return render(request,'student_Dj_form.html',d)

from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *

# Create your views here.
def student_Dj_form(request):
    STDDJF = StudentDjForm()  # empty form

    if request.method == 'POST':
        STDDJF = StudentDjForm(request.POST)
        if STDDJF.is_valid():
            SFDO = STDDJF.cleaned_data
            return HttpResponse(str(SFDO))
        else:
            return HttpResponse("Invalid Data")

    d = {'STDDJF': STDDJF}
    return render(request, 'student_Dj_form.html', d)


