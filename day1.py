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

def get_result(report):
    counter = 0
    for i in report:
        if int(i[0]) < int(i[1]):
            counter+=1
    return counter

def sample_solution():
    source_list = sample_source.split()
    count_sample = get_result(list(pairwise(source_list)))
    print(count_sample)

def solution1():
    full_data_counter = get_result(list(pairwise(read_source_from('day1_input.txt'))))
    print(full_data_counter)

def solution2():
    dataList = read_source_from('day1_input.txt')
    counter = 0
    for i, d in enumerate(dataList):
        left = i
        right = i + 1
        if right < (len(dataList) - 1):
            if int(dataList[left]) < int(dataList[right]):
                counter+=1
    print(counter)

sample_solution()
solution1()
solution2()