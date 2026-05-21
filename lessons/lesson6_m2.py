# import requests
#
# response = requests.get('https://google.com')
# print(response.text)


def binary_search(array, target):
    left, right = 0, len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        print(f'index mind{mid}')
        if array[mid] == target:
            return print('Найден!!')
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return print("Не нашли!!")

# my_list = [1,2,3,4,5,6,7,8,9,10,11]
#
# binary_search(my_list, 11)
nums = [2,7,11,15]
my_target = 9


def two_sum(array, target):
    num_map = {
        # 2:0
    }
    for index, item in enumerate(array):
        complement = target - item
        if complement in num_map:
            return [num_map[complement], index]
        num_map[item] = index
    return []
print(two_sum(nums, my_target))