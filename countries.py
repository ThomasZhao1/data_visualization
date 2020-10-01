from pygal.maps.world import COUNTRIES

'''
for country_code in sorted(COUNTRIES.keys()):
	print(country_code, COUNTRIES[country_code])
'''

def get_country_code(country_name):
	"""Return the 2-digit code for a country"""
	for code, name in COUNTRIES.items():
		if name == country_name.title():
			return code
	#Return None if no country found
	return None
