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
            negativeNumbers = [];
            
            average = (numberA+numberB+numberC+numberD+numberE)/5
            isBiggerThan = average>50
            
            amountPositiveNumbers = 0
            evenNumbers = 0
            oddNumbers = 0
            numbersBiggerThanTen = []
            
            for number in numbers:
                if number >= 0:
                    amountPositiveNumbers += 1
                else:
                    negativeNumbers.append(number)
                if number > 10:
                    numbersBiggerThanTen.append(number)
                    
                if number & 1 == 0:
                    evenNumbers += 1
                else:
                    oddNumbers += 1
                    
            numbersBiggerThanTen.sort()
                
            NumbersForm.objects.create(
                input_a=numberA,
                input_b=numberB,
                input_c=numberC,
                input_d=numberD,
                input_e=numberE,
                original_list=numbers,
                sorted_list=sorted(numbers),
                negative_values=negativeNumbers,
                positive_count=amountPositiveNumbers,
                even_count=evenNumbers,
                odd_count=oddNumbers,
                greater_than_ten=numbersBiggerThanTen,
                average=average,
                average_gt_50=isBiggerThan
            )
            
            return render(request, 'numbers_result.html', {
                "numbers": numbers,
                'average': average,
                'isBiggerThan': isBiggerThan,
                'amountPositiveNumbers' : amountPositiveNumbers,
                'evenNumbers': evenNumbers,
                'oddNumbers': oddNumbers,
                'numbersBiggerThanTen': numbersBiggerThanTen,
                'negativeNumbers': negativeNumbers,
                'hasNegatives': len(negativeNumbers) > 0
            })
    else:
        form = NumbersForm()
    return render(request, 'index.html', {'form': form})
