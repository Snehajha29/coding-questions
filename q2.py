def make_alternating(s):
    n = len(s)
    operations = 0
    for i in range(0, n, 2):
        if s[i] == s[(i+1)%n]:
            operations += 1
    for i in range(1, n, 2):
        if s[i] == s[(i+1)%n]:
            operations += 1
    if n % 2 == 0 and s[-1] == s[0]:
        operations += 1
    if operations <= n:
        return operations // 2
    else:
        return -1
    
s = "1010"
result = make_alternating(s)
print(result)    
    
  