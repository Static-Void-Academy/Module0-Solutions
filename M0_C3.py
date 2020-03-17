# M0.C3 - Max Volume

def get_loudest_second(volumes):
    max_volume = -73
    max_second = -1
    for x in range(0, len(volumes)):
        if volumes[x] < -72 or volumes[x] > 10:
            return "Invalid"

        if volumes[x] > max_volume:
            max_volume = volumes[x]
            max_second = x

    return max_second
