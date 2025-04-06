class Factorial:
    def __init__(self, number):
        self.number = number

    def calculate(self):
        if self.number < 0:
            raise ValueError("Factorial is not defined for -ve number")
        return self._factorial(self.number)
    
    def _factorial(self, n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * self._factorial(n-1)
        
if __name__ == "__main__":
    number = -5
    calculator = Factorial(number)
    try: 
        result = calculator.calculate()
        print(f"the factorial of {number} is : {result}")
    except ValueError as e:
        print(e)