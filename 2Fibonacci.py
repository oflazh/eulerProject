def fib(num):

  if num <= 2:
    return 1
  return fib(num - 1) + fib(num - 2)


x = 0
for k in range(11):
      x += fib(3 + 3 * k)

print(x)
