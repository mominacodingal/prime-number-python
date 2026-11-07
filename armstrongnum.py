n = int(input("Enter number: "))
temp, p, total = n, len(str(n)), 0
while temp > 0:
   total += (temp % 10) ** p
   temp //= 10
print("Armstrong" if total == n else "Not Armstrong")