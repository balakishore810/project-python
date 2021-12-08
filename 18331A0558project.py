import random as balu

bala = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ\
             abcdefghijklmnopqrstuvwxyz\
             1234567890 !@#$%^&*(){}[]<>,.')
password = ''
for char in bala:
    password += balu.choice(bala)
    
print(password)
