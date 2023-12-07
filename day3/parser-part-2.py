import fileinput
import os

inputFile = os.path.dirname(__file__) + os.path.sep + 'input'

sum = 0
last_stars = []
last_numbers = []
for line in fileinput.input(inputFile):
    stars = list(map(lambda star: (star, []),filter(lambda idx: line[idx] == '*', range(len(line)))))
    i = 0
    numbers = []
    while (i < len(line)):
        if line[i].isdecimal():
            j = i
            while (j < len(line)):
                if j + 1 < len(line) and line[j + 1].isdecimal():
                    j = j + 1
                else:
                    numbers.append((i,j,int(line[i:j+1])))
                    i = j + 1
                    break
        else:
            i = i + 1
    
    # Find numbers adjacent to stars in the same line
    for number in numbers:
        for star in stars:
            # The last digit of the number is to the left of the star, or the first digit is to the right of the star
            if number[1] == star[0] - 1 or number[0] == star[0] + 1:
                # add the number to the numbers of the star
                star[1].append(number[2])

    # Find numbers in the last line adjacent to stars in this line
    for number in last_numbers:
        for star in stars:
            if star[0] in range(number[0] - 1, number[1] + 2):
                star[1].append(number[2])
        
    # Find numbers in this line adjacent to stars in the last line
    for number in numbers:
        for star in last_stars:
            if star[0] in range(number[0] - 1, number[1] + 2):
                star[1].append(number[2])
    
    gears = filter(lambda star: len(star[1]) == 2, last_stars)
    for gear in gears:
        sum = sum + gear[1][0] * gear[1][1]

    last_numbers = numbers
    last_stars = stars

gears = filter(lambda star: len(star[1]) == 2, last_stars)
for gear in gears:
    sum = sum + gear[1][0] * gear[1][1]

print(sum)