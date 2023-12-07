import fileinput
import os

inputFile = os.path.dirname(__file__) + os.path.sep + 'input'

sum = 0
for line in fileinput.input(inputFile):
    max_green = 0
    max_red = 0
    max_blue = 0
    eles = line.split(':')
    game_number = eles[0][5:]
    draws = eles[1].split(";")
    for draw in draws:
        balls = draw.split(',')
        for ball in balls:
            amount, color = ball.strip().split(' ')
            am = int(amount)
            match color:
                case 'blue' if am > max_blue: max_blue = am
                case 'green' if am > max_green: max_green = am
                case 'red' if am > max_red: max_red = am
    power = max_blue * max_green * max_red
    sum = sum + power

print(sum)