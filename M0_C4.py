# M0_C4 - Max Volume
# See https://github.com/Static-Void-Academy/Module0-Challenges/blob/master/M0_C4.md

def get_loudest_second(volumes):
    # We have separate variables tracking current maximum volume so far and its index.
    # -73 and -1 starting values because they fall outside expected range.
    max_volume = -73
    max_second = -1

    # Iterate through volumes list
    for x in range(0, len(volumes)):
        # If volume below -72 or above 10, per prompt, invalid.
        # Can immediately exit function and return "Invalid"
        if volumes[x] < -72 or volumes[x] > 10:
            return "Invalid"

        # Otherwise, check if current volume > max_volume
        # and set new maximum and new index if yes.
        if volumes[x] > max_volume:
            max_volume = volumes[x]
            max_second = x

    return max_second
