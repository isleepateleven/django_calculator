from django.shortcuts import render
from .forms import CalculatorForm


# Create your views here.
def home (request):
    form = CalculatorForm()
    context = {
        "form": form
    }
    return render(request,'calculator/home.html',context)


def result(request):
    form = CalculatorForm(request.GET or None)  # Bind the form if data is submitted
    result = None  # Initialize result as None

    if form.is_valid():
        num1 = form.cleaned_data['number1']
        num2 = form.cleaned_data['number2']
        operation = request.GET.get('operation')

        # Perform the calculation
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 != 0:
                result = num1 / num2
            else:
                form.add_error(None, "Error: Cannot divide by zero.")

    context = {
        "result": result,
        "form": form
    }
    return render(request,'calculator/result.html', context)