#Even sum with range
target = int(input("Enter a number between 0 and 1000")) # Enter a number between 0 and 1000
even_sum = 0
for number in range(2,target+1,2):
  even_sum = even_sum + number

print(even_sum)
