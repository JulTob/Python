'''
Calculates time, liters of gas used,
and cost of gasoline for a trip.

-- Julio Toboso
'''

distance = 600  # km
# BMW Serie 3 (E46)
ltr_100km = 8.9
km_h = 100
prize = 1.455 # €/l

time = distance /km_h
gas_liters = ( distance * ltr_100km ) / 100
prize = gas_liters * prize

print( time, gas_liters, prize)
