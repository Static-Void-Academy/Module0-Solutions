# Script will start by asking for input.
# Then it will scan that input for big H and little h
# occurrences and print those out.
# See https://github.com/Static-Void-Academy/Module0-Challenges/blob/master/M0_C2.md

message = input('Input message: ')

H = 0
h = 0
for char in message:
    if char == 'H':
        H += 1
    elif char == 'h':
        h += 1

print(f'H: {H}, h: {h}')

