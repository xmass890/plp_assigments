#this is the assiment on functions 

def calculate_discount(price, discount_percent=0):
    if (discount_percent):
        float(discount_percent)
        new_price = price - ((discount_percent / 100 ) * price)
        return f"thanks for choosing us the new price is {new_price}"

    else:
        return f"you have no any discount! your original price is {price}"
    

price = float(input('please enter the original price: '))
discount_percent = input('please enter the discount percent you want eg, 30: ')



result = calculate_discount(price, discount_percent)

print(result)

