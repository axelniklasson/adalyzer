
def calculate_persona(throttle_position, rpm, vehicle_speed, fuel_consumption_avg):
	attributes = {'calm': 0, 'reckless': 0, 'family': 0, 'eco': 0}
	if throttle_position > 40 and rpm > 3000:
		attributes['reckless'] = attributes['reckless'] + 1

	if 0 < throttle_position < 40 and 0 < rpm < 3000:
		attributes['eco'] = attributes['eco'] + 2
		attributes['calm'] = attributes['calm'] + 1

	if vehicle_speed > 50 and rpm > 4000 and fuel_consumption_avg > 1:
		attributes['eco'] = attributes['eco'] - 1

	if throttle_position > 80:
		attributes['reckless'] = attributes['reckless'] + 2
		attributes['calm'] = attributes['calm'] -1

	return attributes

# Example usage
# print calculate_persona(81, 7000, 100, 2)
