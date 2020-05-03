# M0_C5 - Mean, Median
# See https://github.com/Static-Void-Academy/M0_C5/blob/master/README.md

def mean(scores):
    """Returns the average of only valid scores in the given list [0,100]"""
    total = 0
    count = 0
    for score in scores:
        if not(score < 0 or score > 100):
            total += score
            count += 1

    if count == 0:
        return -1

    return total / count

def median(scores):
    """Returns the median of only valid scores in the given list [0,100]"""

    # Checks and adds valid scores to valid_scores
    valid_scores = []
    for score in scores:
        if not(score < 0 or score > 100):
            valid_scores.append(score)

    if len(valid_scores) == 0:
        return -1

    half = len(valid_scores) // 2
    # Return avg of 2 middle scores if even
    if len(valid_scores) % 2 == 0:
        return (valid_scores[half] + valid_scores[half - 1]) / 2

    # Otherwise return middle score for odd
    return valid_scores[half]

if __name__ == '__main__':
    scores = input("Input list of test scores, space-separated: ")
    scores_list = [int(i) for i in scores.split()]

    mean = mean(scores_list)
    median = median(scores_list)

    print(f"Mean: {mean}")
    print(f"Median: {median}")
