def even_numbers(ref_func):
    def wrapper(nums):
        return [num for num in nums if num % 2 == 0]
    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers

print(get_numbers([1, 2, 3, 4, 5]))
