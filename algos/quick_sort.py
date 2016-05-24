##def quick_sort(numbers):
##
##    if len(numbers) <= 1:
##        return numbers
##
##    pivot = numbers[0]
##
##    return quick_sort([n for n in numbers if n < pivot]) + \
##           [n for n in numbers if n == pivot] + \
##           quick_sort([n for n in numbers if n > pivot])

def quick_sort(array, begin=0, end=None):
    
    if end is None:
        end = len(array) - 1
    if begin >= end:
        return None

    pivot = begin
    for i in xrange(begin + 1, end + 1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    
    quick_sort(array, begin, pivot - 1)
    quick_sort(array, pivot + 1, end)

if __name__ == "__main__":

    import random

    l = range(100)
    random.shuffle(l)

    quick_sort(l)
    print l
