import json
from pygal.maps.world import World
from pygal.style import RotateStyle as RS, LightSolarizedStyle as LSS
from countries import get_country_code

#Load the data into a list

filename = 'gdp_json.json'
with open(filename) as f:
	gdp_data = json.load(f)

year = 2016

#Build a dict for GDP data
gdp_dict = {}

for country in gdp_data:
	if country['Year'] == year:
		country_name = country['Country Name']
		gdp = int(float(country['Value']))
		code = get_country_code(country_name)
		if code:
			gdp_dict[code] = gdp
#Sort by GDP output levels
low, mid, high = {}, {}, {}

for country, gdp in gdp_dict.items(): 
	if gdp < 10 ** 12:
		low[country] = gdp
	elif gdp > 10 ** 12 and gdp < 10 ** 13:
		mid[country] = gdp
	else:
		high[country] = gdp


wm_style = LSS()
wm = World(style = wm_style)
wm.title = 'World GDP in 2016, by country'
wm.add('low GDP', low)
wm.add('mid GDP', mid)
wm.add('high GDP', high)
wm.render_to_file('world_gdp.svg')
