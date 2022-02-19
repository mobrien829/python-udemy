
def sum_divisible():
    div_numbers = []

    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            div_numbers.append(i)

    answer = sum(div_numbers)
    print(answer)
    return answer


sum_divisible()
