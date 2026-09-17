# for loop without starting value and skip value
# for i in range(10):
#   print("without range skip: ",i);
# output 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9


# # for loop with range start value
# for i in range(1, 10):
#   print("with range: ",i);
# output
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9


## for loop with range start value and skip value
# for i in range(2, 10, 2):
#   print("with range skip: ",i);
# output
# 2
# 4
# 6
# 8


# # 1 to 100 all odd numbers summation
# total = 0;
# for i in range(1, 101, 2):
#   total = total + i;
# print(total)

# # WHILE LOOP
# i = 1;
# sum = 0;
# while i < 101:
#   sum = sum + i;
#   i = i+1;

# print(sum)

fruites = ['mango', 'banana', 'pineapple', 'orange', 'jackfruite'];
for fruite in range(0, len(fruites), 2):
  print(fruites[fruite])  