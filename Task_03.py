"""
Написать функцию get_mean_green_index,
которая в качестве аргумента принимает список объектов типа GreenZoneIndex и считает от них средний индекс озеленения.
"""

def get_mean_green_index(green_zones_list: list[GreenZoneIndex]) -> float:
"""
Функция, считает средний индекс озеленения
:param green_zone_list: список элементов GreenZoneIndex
:return: средний индекс всех элементов в списке"""

mean_index = 0
for element in green_zones_list
    mean_index = sum(green_zones_list)
    
    return mean_index

list_territories = [
    {"territory_name": "Пушкин", "territory_area": 28676, "green_zones": [302, 487, 420, 325, 471, 363, 404]},
    {"territory_name": "Павловск", "territory_area": 21025, "green_zones": [360, 375, 223, 258, 345, 296, 303]},
    {"territory_name": "Петергоф", "territory_area": 44274, "green_zones": [364, 447, 438, 223, 336, 431, 442]},
]

territories_green_zone = [] # новый список

for green_zone_index in list_territories:
    new_green_zone_index = GreenZoneIndex(
        green_zone_index["territory_name"], green_zone_index["territory_area"], green_zone_index["green_zones"]
    )
    territories_green_zone.append(new_green_zone_index)

print(get_mean_green_index(green_zones_list))