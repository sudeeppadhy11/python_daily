import operators

def count_of_digit(num):
    count=0
    while num:
        count=operators.add(count,1)
        num=operators.remove_last_digit(num)
    return count
