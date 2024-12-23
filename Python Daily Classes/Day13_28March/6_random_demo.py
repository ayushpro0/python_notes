import random

my_list = [100, 1, 99, 44, 22, 66]

print("Original list = ", my_list)

random.shuffle(my_list)
print("Random list = ", my_list) # Random list =  [22, 99, 66, 100, 1, 44]

print("-----------------------------------------------------")

print("random choice from a list = ", random.choice(['apple', 'pear', 'banana'])) # banana

print("-----------------------------------------------------")

print("Random float number = ", random.random())  # Random float number =  0.258156852492736

print("-----------------------------------------------------")

print(random.randrange(4)) # 1