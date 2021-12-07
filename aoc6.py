input = [1,2,5,1,1,4,1,5,5,5,3,4,1,2,2,5,3,5,1,3,4,1,5,2,5,1,4,1,2,2,1,5,1,1,1,2,4,3,4,2,2,4,5,4,1,2,3,5,3,4,1,1,2,2,1,3,3,2,3,2,1,2,2,3,1,1,2,5,1,2,1,1,3,1,1,5,5,4,1,1,5,1,4,3,5,1,3,3,1,1,5,2,1,2,4,4,5,5,4,4,5,4,3,5,5,1,3,5,2,4,1,1,2,2,2,4,1,2,1,5,1,3,1,1,1,2,1,2,2,1,3,3,5,3,4,2,1,5,2,1,4,1,1,5,1,1,5,4,4,1,4,2,3,5,2,5,5,2,2,4,4,1,1,1,4,4,1,3,5,4,2,5,5,4,4,2,2,3,2,1,3,4,1,5,1,4,5,2,4,5,1,3,4,1,4,3,3,1,1,3,2,1,5,5,3,1,1,2,4,5,3,1,1,1,2,5,2,4,5,1,3,2,4,5,5,1,2,3,4,4,1,4,1,1,3,3,5,1,2,5,1,2,5,4,1,1,3,2,1,1,1,3,5,1,3,2,4,3,5,4,1,1,5,3,4,2,3,1,1,4,2,1,2,2,1,1,4,3,1,1,3,5,2,1,3,2,1,1,1,2,1,1,5,1,1,2,5,1,1,4]
# input = [3,4,3,1,2]

#Generates an indexed array to track the number of lanternfish, creates new spawn with a timer of 8 & resets existing ones to 6 each day
input_count = [0]*10
for i in range(0, len(input)):
    input_count[input[i]] += 1
for day_num in range(1, 257):
    input_count[9] += input_count[0]
    input_count[7] += input_count[0]
    for ctr in range(0, len(input_count)-1):
        input_count[ctr] = input_count[ctr+1]
        ctr += 1
    input_count[9] = 0
    day_num += 1
print("Number of lanternfish after", day_num-1, "days:", sum(input_count))
        
# Pt 1- Generates an indexed array to track the number of lanternfish, creates new spawn with a timer of 8 & resets existing ones to 6 each day (slow solution)
# day_num = 1
# while(day_num < 81):
#     ctr = 0
#     while(ctr < len(input)):
#         if(input[ctr] != 0):
#             input[ctr] -= 1
#         else:
#             input[ctr] = 6
#             input.append(9)
#         ctr += 1
#     day_num += 1
# print("Number of lanternfish after", day_num-1, "days:", len(input))