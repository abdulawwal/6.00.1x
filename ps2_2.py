balance = 3329
annualInterestRate = 0.2

minPayment = round(balance / 12, -1)
notEnough = True
while True:
    for i in range(12):
        balance -= minPayment
    if balance <= 0:
        break
    else:
        minPayment += 10
    balance *= 1 + annualInterestRate/12
print('Lowest Payment:', round(minPayment))
