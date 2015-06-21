balance = 4773
annualInterestRate = 0.2

minPayment = round(balance / 12, -1)
notEnough = True
while True:
    b = balance
    for i in range(12):
        b -= minPayment
        b *= 1 + annualInterestRate/12
    if b <= 0:
        break
    else:
        minPayment += 10
print 'Lowest Payment:', round(minPayment)
