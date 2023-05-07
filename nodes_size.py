def map_values(value, in_min, in_max, out_min, out_max):
    return int((value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)


value = 100
mapped_value = map_values(value, 1, 324, 5, 15)
print(mapped_value)
