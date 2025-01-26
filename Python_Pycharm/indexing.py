#indexing = accessing elements of a sequence using[] (indexing operator)
              # [start : end : step]
credit_card_number = "1234-5678-9012-3456"

#print(credit_card_number[0])
#print(credit_card_number[:4])
#print(credit_card_number[5:9])
#print(credit_card_number[-1]) # negative indexing

#print(credit_card_number[::3])

last_digits = credit_card_number[::-1]
print(last_digits)
#last_digits = credit_card_number[-4:]
#print(f"XXXX-XXXX-XXXX-{last_digits}")