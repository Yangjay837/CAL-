def calculate_bill(customerID, customerName, unitConsumed):
    
    rate1 = 1.20
    rate2 = 1.50
    rate3 = 1.80
    surcharge = 0.15

    
    if unitConsumed <= 199:
        total_amount = unitConsumed * rate1 
    elif 200 <= unitConsumed < 400:
        total_amount = 200 * rate1 + (unitConsumed - 200) * rate2
    elif 400 <= unitConsumed < 600:
        total_amount = 200 * rate1 + 200 * rate2 + (unitConsumed - 400) * rate3
    else:
        total_amount = 200 * rate1 + 200 * rate2 + 200 * rate3 + (unitConsumed - 600) * rate3


    if total_amount > 400:
        total_amount += total_amount * surcharge

    
    total_amount = max(total_amount, 100)

    
    print(f"CustomerID: {customerID}")
    print(f"CustomerName: {customerName}")
    print(f"Units consumed: {unitConsumed}")
    print(f"Charges per unit: {rate1} for upto 199 units, {rate2} for 200-399 units, {rate3} for 400 and above units")
    print(f"Total Amount to pay: {total_amount}")


customerID = input("Enter customerID: ")
customerName = input("Enter customerName: ")
unitConsumed = int(input("Enter units consumed: "))


calculate_bill(customerID, customerName, unitConsumed)