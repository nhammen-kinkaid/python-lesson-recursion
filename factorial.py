# This wont work!
def factorial(n):
  print("Calculating", n, "factorial")
  result = factorial(n-1) * n
  return result

factorial(4)
