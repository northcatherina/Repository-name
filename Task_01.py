class GreenZoneIndex:
    def __init__(self, territory_name_param: str, territory_area: int, green_zones: list[int]):
        """
        :param territory_name: Название территории
        :param territory_area: Площадь территории
        :param green_zones: Список площадей парков
        """
        self.territory_name = territory_name_param
        self.territory_area = territory_area
        self.green_zones = green_zones

        self.green_index = None

    def calculate_green_index(self):
        """
        Метод для вычисления индекса озеленения.

        Индекс рассчитывается как отношение площади всех парков к площади территории
        """
        green_zones_sum = sum(self.green_zones)

        green_index = green_zones_sum/self.territory_area
        self.green_index = green_index
        return green_index

    def percentage(green_index):
        percentage = 100 * float(territory_1)
        return float(percentage) + "%"
    green_index = round(1)
    print(green_index)
    print(type(green_index))

territory_name_1 = "Пушкин"
territory_area = 28676
green_zones = [302, 487, 420, 325, 471, 363, 404]
territory_1 = GreenZoneIndex(territory_name_1, territory_area, green_zones)

print(territory_1.green_index)
print(territory_1.calculate_green_index())
print(territory_1.green_index)

