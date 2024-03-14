print("Loan Calculator")
print()
loan = int(input("How much is the loan? "))
apr = int(input("What is the APR? "))
time = int(input("How many years is the loan? "))
print("$",loan,"over",time,"years at",apr,"% APR")
print()

for i in range(time):
  loan = loan + loan * (apr/100)
  print("Year", i+1, "is", round(loan,2))
