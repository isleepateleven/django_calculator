from django.test import TestCase
from django.urls import reverse
from .forms import CalculatorForm


# Home Page Testing
class TestHomePage(TestCase):
    def test_home_page_loads(self):
        """Test if the home page loads correctly and uses the correct template."""
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'calculator/home.html')
        self.assertEqual(response.status_code, 200)

    def test_home_page_contains_form(self):
        """Test if the form is rendered properly on the home page."""
        response = self.client.get(reverse('home'))
        self.assertContains(response, '<form')
        self.assertContains(response, 'name="number1"') # Input field for number1
        self.assertContains(response, 'name="number2"') # Input field for number2
        self.assertContains(response, 'name="operation" value="add"')  # Add button
        self.assertContains(response, 'name="operation" value="subtract"')  # Subtract button
        self.assertContains(response, 'name="operation" value="multiply"')  # Multiply button
        self.assertContains(response, 'name="operation" value="divide"')  # Divide button


# Result Page Testing 
class ResultPageTesting(TestCase):
    def test_result_page_loads(self):
        """Test if the result page loads correctly and uses the correct template."""
        response = self.client.get(reverse('result'))
        self.assertTemplateUsed(response, 'calculator/result.html')
        self.assertEqual(response.status_code, 200)


# Operations Testing
class OperationsTest(TestCase):
    def test_addition_operation(self):
        """Test the addition operation."""
        response = self.client.get(reverse('result'),{
            "number1": -2,
            "number2": 5,
            "operation": "add",
        })
        self.assertContains(response, '3')
    
    def test_subtraction_operation(self):
        """Test the subtraction operation."""
        response = self.client.get(reverse('result'),{
            "number1": 8,
            "number2": 2,
            "operation": "subtract",
        })
        self.assertContains(response, '6')

    def test_multiplication_operation(self):
        """Test the multiplication operation."""
        response = self.client.get(reverse('result'),{
            "number1": 5,
            "number2": 7,
            "operation": "multiply",
        })
        self.assertContains(response, '35')

    def test_division_operation(self):
        """Test the division operation."""
        response = self.client.get(reverse('result'),{
            "number1": 45,
            "number2": 5,
            "operation": "divide",
        })
        self.assertContains(response, '9')

    def test_division_by_zero(self):
        """Test division by zero."""
        response = self.client.get(reverse('result'),{
            "number1": 4,
            "number2": 0,
            "operation": "divide",
        })
        self.assertContains(response, 'Error: Cannot divide by zero.')


# Input Validation Testing  
class InputValidationTest(TestCase):
    def setUp(self):
        self.form = CalculatorForm

    def test_invalid_input(self):
        """Test form rejects invalid inputs."""
        form = self.form({'number1': 'abc', 'number2': 'xyz'})
        self.assertFalse(form.is_valid())  
        self.assertIn('number1', form.errors)  # Check that 'number1' has an error
        self.assertIn('number2', form.errors)  # Check that 'number2' has an error

    def test_missing_input(self):
        """Test form rejects missing inputs."""
        form = self.form({'number1': '', 'number2': ''})
        self.assertFalse(form.is_valid()) 
        self.assertIn('number1', form.errors)  # Check that 'number1' has an error
        self.assertIn('number2', form.errors)  # Check that 'number2' has an error

    def test_valid_input(self):
        """Test that the form validates with correct data."""
        form = self.form({'number1': 5, 'number2': 3})
        self.assertTrue(form.is_valid()) 
