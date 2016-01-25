def longest_continuous_inc_or_dec(sequence):

    longest = 1
    up_length = 1
    down_length = 1
    
    for prev, curr in zip(sequence[:-1], sequence[1:]):

        if curr > prev:
            up_length += 1
            if up_length > longest:
                longest = up_length
        else:
            up_length = 1
            
        if curr < prev:
            down_length += 1
            if down_length > longest:
                longest = down_length
        else:
            down_length = 1
        
    return longest

if __name__ == "__main__":

    print longest_continuous_inc_or_dec([1,2,3,2])
    print longest_continuous_inc_or_dec([1,2,3,2,1,0,1])
    print longest_continuous_inc_or_dec([1,2,3])
    print longest_continuous_inc_or_dec([3,2,1,3])
