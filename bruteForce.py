def action(line): # put whatever you want to do with brute force in here
    print(line)

charList = [chr(i) for i in range(32, 127)] # this line auto genorates all keyboard printable characters
maxLength = 100 # this vaariable controls max length
startingLength = 0 # change this to change starting length

base = len(charList)
input(f"Summary of program:\rList of characters: '{''.join(charList)}'\nTotal characters: {base}\nMaximum length: {maxLength}\n\nPress enter to begin ")
print(f"\n{'='*30}\n")
for length in range(startingLength-1, maxLength):
    length += 1
    for number in range(len(charList)**length):
        lis = []
        if number == 0: digits = [0]
        else:
            digits = []
            while number:
                digits.append(int(number % base))
                number //= base
        lis = digits[::-1]
        action(''.join([charList[i] for i in [0]*(length-len(lis)) + lis]))
