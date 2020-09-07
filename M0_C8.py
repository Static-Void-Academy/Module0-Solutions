# M0_C8 - Intersection
# See https://github.com/Static-Void-Academy/M0_C8/blob/master/README.md

def check_overlap(crime1, crime2):
    # Convert lists to sets
    s1 = set(crime1)
    s2 = set(crime2)

    # Get common elements between two
    output = s1.intersection(s2)

    # If either list is smaller than 3, then
    # one of them must overlap completely
    if len(s1) < 3 or len(s2) < 3:
        return output == s1 or output == s2

    # Otherwise check at least 3 overlaps
    return len(output) >= 3

# DO NOT MODIFY BELOW
if __name__ == '__main__':
    crime1_input = input("crime1: ")
    crime2_input = input("crime2: ")

    crime1 = crime1_input.split()
    crime2 = crime2_input.split()

    print(check_overlap(crime1, crime2))
