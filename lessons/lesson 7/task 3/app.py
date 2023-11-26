def find_fathest_orbit(orbits):
    filtered_orbits = list(filter(lambda x: x[0] != x[1], orbits))
    return max(filtered_orbits, key=lambda x: x[0] * x[1])


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
result = find_fathest_orbit(orbits)
print(result)
