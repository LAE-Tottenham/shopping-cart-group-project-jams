import math # you'll probably need this

exchange_rates = {
    'USD': 1.13, #I.E. 1 Pound is 1.13 Dollars
    'EUR': 1.15,
    'CAD': 1.80,
    'YUAN': 9.27,
    'DIRHAM': 4.79
    }
yes = input("Would you like to convert to a a different currency? y/n: ").upper()
if yes == "Y":
    new_c = input("Pick a currency to convert to : ").upper()
clist = ['USD', 'EUR', 'CAD','YUAN', 'DIRHAM']
def check_currency_exists(new_c):
    while new_c == "USD" or 'CAD' or 'YUAN' or 'DIRHAM' or 'EUR':
            print("We can convert to that currency!!")
    else:
        print("We cannot convert to that currency.")
        new_c = input("Pick a currency to convert to : ").upper()

    return new_c
new_c = check_currency_exists()
amount = 37.00
original_c = 1 
def currency_convert(original_c, new_c, amount):
    price = amount * exchange_rates[new_c]
    print(price)
currency_convert()