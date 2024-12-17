from django import forms

# Pure Django Form
class CalculatorForm(forms.Form):
    number1 = forms.FloatField(
                required=True, 
                widget=forms.NumberInput(attrs={
                                            "placeholder": "Enter first number",
                                            'class': 'input-field'})
    )
    number2 = forms.FloatField(
                required=True, 
                widget=forms.NumberInput(attrs={
                                            "placeholder": "Enter second number",
                                            'class': 'input-field'})
    )