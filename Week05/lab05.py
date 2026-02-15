#Q1
def fibonachiNumber(n):
    a, b = 0,1
    if n <= 0:
        print(0)
    elif n == 1:
        print(1)
    else:
        for i in range(2, n + 1):
            a, b = b, a + b
        print(b)
#test case
#fibonachiNumber(4)

#Q2
def fizz_buzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(f"{i}")
    print(result)
#test case
#fizz_buzz(15)


#Q3 part A
def iterative_binary_search(nums, target):
    left, right = 0, len(nums) - 1  
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def recursive_binary_search(nums, target, left, right):
    if left > right: 
        return -1
    mid = (left + right) // 2
    if (nums[mid] == target): return mid
    elif target < nums[mid]:
        return recursive_binary_search(nums, target, left, mid - 1)
    else:
        return recursive_binary_search(nums, target, mid + 1 , right)

def search_recursive(nums, target):
    if len(nums) == 0:
        return -1
    return recursive_binary_search(nums, target, 0, len(nums) - 1)

#test cases
"""print("\n--- Part A: Iterative Binary Search ---")
test_cases = [
    ([-1, 0, 3, 5, 9, 12], 9),
    ([-1, 0, 3, 5, 9, 12], 2),
    ([1], 1),
    ([1, 2, 3, 4, 5], 1),
    ([1, 2, 3, 4, 5], 5),
    ([1, 2, 3, 4, 5], 3),
    ([], 5),
]

for nums, target in test_cases:
    result = iterative_binary_search(nums, target)
    print("nums=" + str(nums) + ", target=" + str(target) + " -> index: " + str(result))

print("\n--- Part B: Recursive Binary Search ---")
for nums, target in test_cases:
    result = search_recursive(nums, target)
    print("nums=" + str(nums) + ", target=" + str(target) + " -> index: " + str(result))"""