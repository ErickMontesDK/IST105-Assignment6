from django.shortcuts import render
from .forms import NumbersForm

# Create your views here.

def numbers_view(request):
    if request.method == 'POST':
        form = NumbersForm(request.POST)
        if form.is_valid():
            numberA = form.cleaned_data['numberA']
            numberB = form.cleaned_data['numberB']
            numberC = form.cleaned_data['numberC']
            numberD = form.cleaned_data['numberD']
            numberE = form.cleaned_data['numberE']
            
            numbers = [numberA, numberB, numberC, numberD, numberE]
            
            average = (numberA+numberB+numberC+numberD+numberE)/5
            isBiggerThan = average>50
            
            evenNumbers = 0;
            oddNumbers = 0;
            numbersBiggerThanTen = []
            
            for number in numbers:
                if number > 10:
                    numbersBiggerThanTen.append(number)
                    numbersBiggerThanTen.sort()
                    
                if number & 1 == 0:
                    evenNumbers += 1
                else:
                    oddNumbers += 1
                    
                
            
            
            return render(request, 'numbers_result.html', {
                "numbers":numbers,
                'average': average,
                'isBiggerThan': isBiggerThan,
                'evenNumbers':evenNumbers,
                'oddNumbers':oddNumbers,
                'numbersBiggerThanTen': numbersBiggerThanTen
                })
    else:
        form = NumbersForm()
    return render(request, 'index.html', {'form': form})
