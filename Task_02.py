"""
Дан список словарей территорий.
Сделать новый список с объектами ранее реализованного типа GreenZoneIndex
"""

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