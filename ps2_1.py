balance = 4213.0
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

totalPaid = 0
for i in range(12):
    print('Month:', i+1)
    minPayment = monthlyPaymentRate * balance
    totalPaid += minPayment
    print('Minimum monthly payment: {0:.2f}'.format(minPayment))
    balance -= minPayment
    balance *= 1 + annualInterestRate/12
    print('Remaining balance: {0:.2f}'.format(balance))
print('Total paid: {0:0.2f}'.format(totalPaid))
print('Remaining balance: {0:.2f}'.format(balance))
