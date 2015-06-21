balance = 999999
annualInterestRate = 0.18

minPayment = round(balance / 12, 2)
maxPayment = round(balance * (1 + annualInterestRate/12.0)**12.0/12.0,2)
epsilon = 0.05
b = 1
while b > 0 or b < -epsilon:
    b = balance
    p = (maxPayment + minPayment)/2.0
    for i in range(12):
        b -= p
        b *= 1 + annualInterestRate/12
    if b > 0:
        minPayment = p
    elif b < -epsilon:
        maxPayment = p
print 'Lowest Payment:', round(p, 2)
