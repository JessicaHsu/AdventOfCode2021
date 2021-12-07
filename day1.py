import itertools

sample_source= """
199
200
208
210
200
207
240
269
260
263
"""

def read_source_from(filename):
    f = open(filename, 'r')
    result = f.read().splitlines()
    f.close()
    return result

## For python 3.10, use itertools.pairwise() directly.
## You can find the pairwise funcion from https://docs.python.org/3/library/itertools.html#itertools.pairwise
def pairwise(iterable):
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)

def get_day1_part1_result(report):
    counter = 0
    for i in report:
        if int(i[0]) < int(i[1]):
            counter+=1
    return counter

def get_day1_part1_sample_solution():
    source_list = sample_source.split()
    count_sample = get_day1_part1_result(list(pairwise(source_list)))
    return count_sample

def get_day1_part1_solution1():
    full_data_counter = get_day1_part1_result(list(pairwise(read_source_from('day1_input.txt'))))
    return full_data_counter

def get_day1_part1_solution2():
    dataList = read_source_from('day1_input.txt')
    counter = 0
    for i, d in enumerate(dataList):
        left = i
        right = i + 1
        if right < (len(dataList) - 1):
            if int(dataList[left]) < int(dataList[right]):
                counter+=1
    return counter


def groupwise(iterable):
    a, b, c = itertools.tee(iterable, 3)
    next(b, None)
    next(c, None)
    next(c, None)
    return zip(a, b, c)

def get_day1_part2_result():
    groups = list(groupwise(read_source_from('day1_input.txt')))

    counter = 0
    end_idx = len(groups) - 1

    for idx, data in enumerate(groups):
        left_idx = idx
        right_idx = idx + 1

        if right_idx <= end_idx:
            left_element = groups[left_idx]
            left_sum = int(left_element[0]) + int(left_element[1]) + int(left_element[2])
            right_element = groups[right_idx]
            right_sum = int(right_element[0]) + int(right_element[1]) + int(right_element[2])

            if left_sum < right_sum:
                counter += 1
    return counter

print(get_day1_part1_sample_solution())
print(get_day1_part1_solution1())
print(get_day1_part1_solution2())
print(get_day1_part2_result())