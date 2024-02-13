def myArea(height):
    highest_index = 0
    lowest_index = 1
    distance = 1
    for idx in range(2, len(height)):
        if height[idx] > height[highest_index]:
            new_distance = (idx - highest_index) - lowest_index
            highest_index = idx 
            if height[highest_index] > height[lowest_index]:
                area = new_distance * height[lowest_index]
            else:
                area = new_distance * height[highest_index]
        elif height[idx] > height[lowest_index]:
            new_distance = highest_index - idx
            lowest_index = idx
            if height[highest_index] > height[lowest_index]:
                area = new_distance * height[lowest_index]
            else:
                area = new_distance * height[highest_index]
        distance += 1
    return area 
    

height = [1,8,6,2,5,4,8,3,7]
area = myArea(height)
print(area)