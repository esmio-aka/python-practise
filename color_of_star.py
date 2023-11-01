stars_dict = {
    "Sun": 5778,  # Surface temperature of the Sun in Kelvin
    "Sirius": 9940,
    "Vega": 9602,
    "Altair": 7530,
    "Betelgeuse": 3500,
    "Rigel": 12100,
    "Proxima Centauri": 3040,
    "Alpha Centauri A": 5790,
    "Alpha Centauri B": 5260,
    "Arcturus": 4286,
    "Antares": 3600,
    "Deneb": 8525,
    "Spica": 22500,
    "Pollux": 4830,
    "Fomalhaut": 8590
}

def which_color_is_star(dict):
    
    color_stars_dict = {
        'Blue': [],
        'White': [],
        'Yellow': [],
        'Orange': [],
        'Red': []
        }

    for i in dict.items():
        str, temp = i
        if temp in range(2000, 3600+1):
            color_stars_dict['Red'].append(str)
        elif temp in range(3600, 5000+1):
            color_stars_dict['Orange'].append(str)
        elif temp in range(5000, 6000+1):
            color_stars_dict['Yellow'].append(str)
        elif temp in range(7500, 11000+1):
            color_stars_dict['White'].append(str)
        elif temp in range(11000, 28000+1):
            color_stars_dict['Blue'].append(str)

    return color_stars_dict 


def print_color_stars(dict):

    for i in dict.items():
        color, str_list = i
        print(f'{color} stars: {", ".join(str_list)}')

color_stars_dict = which_color_is_star(stars_dict)

print_color_stars(color_stars_dict)