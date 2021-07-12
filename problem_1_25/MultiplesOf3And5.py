def multiplesof3or5(number):
    multiples_list = []
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            multiples_list.append(i)
    return sum(multiples_list)


print(multiplesof3or5(1000))
