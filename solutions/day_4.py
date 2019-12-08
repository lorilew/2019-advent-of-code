import re

password_range = (138307, 654504)

count = 0
for password in password_range:
    input = str(password)
    for i in range(5, len(input)):
        substr = input[i-5:i+1]
        sorted_substr = ''.join(sorted(substr))
        if sorted_substr == substr:
            m = re.findall(r'(.)\1{1}', substr)
            if len(m) > 0:
                count += 1




print(count)