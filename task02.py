import random

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or quantity < min or quantity > max or min > max:
        return "Paramaters are not valid"
    
    unique_nums = set()

    while len(unique_nums) < quantity:
        random_num = random.randint(min, max)
        unique_nums.add(random_num)

    return sorted(unique_nums)





lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
