import random
x = input('Enter the names seperated by comma: ')
names = x.split(',')
y = len(names)
z = random.randint(0, y-1)
person_who_will_pay = names[z]
print(person_who_will_pay + ' will pay the bil today')