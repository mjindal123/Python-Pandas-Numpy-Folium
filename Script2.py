print(1)
def currency_converter(rate,euros):
    dollars=euros*rate
    return dollars
r=input("enter rate: ")
e=input("enter euros: ")
print(currency_converter(float(r),float(e)))

functions=[currency_converter(100,1000),currency_converter(100,2000)]
print(functions)
