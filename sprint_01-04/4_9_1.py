import pandas as pd

atlas = [
    ['Франция', 'Париж', 23],
    ['Россия', 'Москва', 34],
    ['Китай',  'Пекин', 354],
    ['Мексика', 'Мехико', 23],
    ['Египет', 'Каир', 44],
]
geography = ['country', 'capital', 'popul']

world_map = pd.DataFrame(data=atlas, columns=geography)

print(world_map)
print(world_map.shape)
world_map.info()