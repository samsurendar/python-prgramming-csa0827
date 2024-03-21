def add_binary(a, b):
    result = ''
    carry = 0
    
    i = len(a) - 1
    j = len(b) - 1
    
    while i >= 0 or j >= 0 or carry:
        bit_a = int(a[i]) if i >= 0 else 0
        bit_b = int(b[j]) if j >= 0 else 0
        
        current_sum = bit_a + bit_b + carry
        
        result = str(current_sum % 2) + result
        
        carry = current_sum // 2
  
        i -= 1
        j -= 1
    
    return result

a = "1010"
b = "1011"
print("Sum:", add_binary(a, b))
