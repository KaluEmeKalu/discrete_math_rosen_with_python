for num in integers:
    if num > current_max:
        current_max = num
        position = index
    index += 1

print(current_max)
print("At position " + str(position) + ". ")




