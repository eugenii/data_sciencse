import pandas as pd

measurements = [['Солнце',146,152], # Измерения хранятся в списке списков 
              ['Луна',0.36, 0.41], # measurements (англ. «измерения»).
              ['Меркурий',82, 217], 
              ['Венера',38, 261],
              ['Марс',56,401],
              ['Юпитер',588, 968],
              ['Сатурн',1195, 1660],
              ['Уран',2750, 3150],
              ['Нептун', 4300, 4700],
              ['Комета Галлея', 6, 5400]]

# Названия столбцов хранятся в переменной header.
header = ['Небесные тела ','MIN', 'MAX'] 

# Сохраним структуру данных в переменной celestial (англ. «небесный»).
celestial = pd.DataFrame(data=measurements, columns=header)

print(celestial.columns)
celestial = celestial.rename(columns={'Небесные тела ': 'celestial_bodies', 'MIN': 'min_distance', 'MAX': 'max_distance'})
print(celestial.columns)
