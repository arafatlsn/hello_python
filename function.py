# # simple function structure
# def sum(a, b):
#   return a + b;

# print(sum(5, 3))

def dontRet(a, b):
  result = a - b;
  if result >= 0:
    return a - b;
  else:
    return b - a;

print(dontRet(2,2))