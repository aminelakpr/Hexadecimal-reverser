#Subscribe to ADDEROS

hexx = input("Enter hex")
decc = int(hexx, base=16)
print('Decimal :', decc)

def reverseBits(num,bitSize):
    binary = bin(num)
    reverse = binary[-1:1:-1]
    reverse = reverse + (bitSize - len(reverse))*'0'
    return (int(reverse,2))

# choose a binary size which we want to reverse
size = 32

print((str(hex(reverseBits(decc,size)))).upper())
