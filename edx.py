balance = 320000; annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate/12
lowerBound = balance/12
upperBound = (balance * (1+annualInterestRate/12)**12)/12
originalBalance = balance

while abs(balance) > .02:
    balance = originalBalance
    payment = (upperBound - lowerBound)/2 + lowerBound
    for month in range(12):
        balance -=payment
        balance *= 1+monthlyInterestRate
        
    if balance > 0:
        lowerBound = payment
    else:
        upperBound = payment
print ("Lowest Payment:", round(payment, 2))