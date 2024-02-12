def myArea(height):
    # option O(n) solution O(1) memory
    highest_value_idx = 1
    second_highest_value_indx = 0 
    distance = 1
    second_highest_value = height[second_highest_value_indx] 
    highest_value = height[highest_value_idx]
    for idx in range(2, len(height)):
        if second_highest_value < height[idx] and highest_value < height[idx]:
            second_highest_value = highest_value
            highest_value = height[idx]
            second_highest_value = highest_value_idx
            highest_value_idx = idx
            distance = highest_value_idx - second_highest_value
        elif second_highest_value < height[idx] and height[idx] != highest_value:
            second_highest_value = height[idx]
            distance = idx - highest_value_idx
    return second_highest_value * distance

height = [1,8,6,2,5,4,8,3,7]
sum = myArea(height)
print(sum)
