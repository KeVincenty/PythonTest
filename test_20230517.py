jim = 'jimmy'
group1 = {'john': 1, 'doe': 2, 'tom': 6}
group2 = [{'kevin': 4, 'tom': 9}, {jim: 16}]
group3 = {'sara': 25, 'lisa': 36, 'anna':49, 'young':64, 'james':81, 'elizabeth':100, 'harry':144, 'dizzy':121}

for info in group2:
    for key in info.keys():
        group1[key] = info[key]

# What will group1 and group2 become after executing this program? Please write them down in the following lines (without actually running this program).
# group1: 
# group2: 

# Then you want to write all the keys and the square root of their corresponding values in group3 into the 1-th dictionary of group2 (e.g. if there is a key ’tom’ whose value is 4, then you need to write a key ‘tom’ whose value is the square root of 4 into group2). Write your codes to achieve this. 
# Write your codes below: