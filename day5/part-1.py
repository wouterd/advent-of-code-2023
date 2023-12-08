import fileinput
import os
from collections import defaultdict

inputFile = os.path.dirname(__file__) + os.path.sep + 'input'

seeds = []
map_name = ''
seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []

def map_value(orig: int, mapping: list):
    mapping = next((x for x in mapping if x[1] <= orig and orig < x[1] + x[2]), None)
    return orig if not mapping else orig - mapping[1] + mapping[0]

for l in fileinput.input(inputFile):
    line = l.strip()
    if line == '': continue
    
    if line.startswith('seeds: '):
        seeds = list(map(lambda seed: int(seed), line[7:].strip().split(' ')))
        continue
    
    if line.endswith('map:'):
        map_name = line.split(' ')[0]
        continue

    map_info = tuple(map(lambda x: int(x), line.split(' ')))
    match map_name:
        case 'seed-to-soil':
            seed_to_soil.append(map_info)
        case 'soil-to-fertilizer':
            soil_to_fertilizer.append(map_info)
        case 'fertilizer-to-water':
            fertilizer_to_water.append(map_info)
        case 'water-to-light':
            water_to_light.append(map_info)
        case 'light-to-temperature':
            light_to_temperature.append(map_info)
        case 'temperature-to-humidity':
            temperature_to_humidity.append(map_info)
        case 'humidity-to-location':
            humidity_to_location.append(map_info)

locations = []

print(humidity_to_location)

for seed in seeds:
    soil = map_value(seed, seed_to_soil)
    fert = map_value(soil, soil_to_fertilizer)
    water = map_value(fert, fertilizer_to_water)
    light = map_value(water, water_to_light)
    temp = map_value(light, light_to_temperature)
    humidity = map_value(temp, temperature_to_humidity)
    location = map_value(humidity, humidity_to_location)
    locations.append(location)
    
    print((seed, soil, fert, water, light, temp, humidity, location))

print(locations)
print(min(locations))