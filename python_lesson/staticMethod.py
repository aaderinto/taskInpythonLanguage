class addition:
    
    @staticmethod
    def sum(num1, num2):
        return num1 + num2

    
    def div(num1, num2):
        return num2/num1

print("The sum of both numbers are:", addition.sum(5,9))

addition.div = staticmethod(addition.div)
print("The division of both numbers are:", addition.div(5,9))