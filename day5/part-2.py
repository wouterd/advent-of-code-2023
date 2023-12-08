import fileinput
import os

inputFile = os.path.dirname(__file__) + os.path.sep + 'input'

seed_ranges = []
map_name = ''
seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []

def find_mapping(orig: int, mapping: list):
    return next((x for x in mapping if x[1] <= orig and orig < x[1] + x[2]), None)

def map_value(orig: int, mapping: list):
    mapping = find_mapping(orig, int)
    return orig if not mapping else orig - mapping[1] + mapping[0]

for l in fileinput.input(inputFile):
    line = l.strip()
    if line == '': continue
    
    if line.startswith('seeds: '):
        seed_info = list(map(lambda seed: int(seed), line[7:].strip().split(' ')))
        for i in range(0, len(seed_info), 2):
            seed_ranges.append((seed_info[i], seed_info[i+1]))
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

def return_ranges(start : int, length : int, mapping : list):
    last = start + length - 1
    curr = start
    while curr <= last:
        mapp = find_mapping(curr, mapping)
        if not mapp:
            next_curr = next((x for x in map(lambda y: y[0], mapping) if x > curr and x <= last), None)
            if next_curr:
                yield (curr, next_curr - curr)
                curr = next_curr
            else:
                yield (curr, last - curr + 1)
                curr = last + 1
        else:
            r_start = curr - mapp[1] + mapp[0]
            r_length = min(mapp[1] + mapp[2] - curr, last - curr + 1)
            yield(r_start, r_length)
            curr += r_length

def return_ranges_from_ranges(ranges: list, mapping: list):
    for range in ranges:
        yield from return_ranges(range[0], range[1], mapping)

def run_seed_range(rng: tuple):
    seed, length = rng
    soil_ranges = return_ranges(seed, length, seed_to_soil)
    fert_ranges = return_ranges_from_ranges(soil_ranges, soil_to_fertilizer)
    water_ranges = return_ranges_from_ranges(fert_ranges, fertilizer_to_water)
    light_ranges = return_ranges_from_ranges(water_ranges, water_to_light)
    temp_ranges = return_ranges_from_ranges(light_ranges, light_to_temperature)
    humi_ranges = return_ranges_from_ranges(temp_ranges, temperature_to_humidity)
    location_ranges = return_ranges_from_ranges(humi_ranges, humidity_to_location)

    return min(map(lambda x: x[0], location_ranges))

print(min(map(run_seed_range, seed_ranges)))
