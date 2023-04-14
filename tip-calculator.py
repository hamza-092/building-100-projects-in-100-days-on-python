print('Welcome to the tip calculator :)')
total_bill = float(input('what is the total bill ? '))
tip = float(input('what percentage of tip (10%, 12%, 15%, etc) would you like to give ? '))
x = (tip/100)*total_bill
sum = x + total_bill
split_bill = int(input('Between ho many people you want to split the bill ? '))
t = (sum/split_bill)
final = round(t,2)
print(f'each person should pay {final} ')
