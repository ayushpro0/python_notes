def even_odd_sum(n):
    odd_sum = 0
    even_sum = 0

    str_n = str(n)

    for i in str_n:
        if int(i) % 2 == 0:
            even_sum += int(i)
        else:
            odd_sum += int(i)
    return even_sum, odd_sum