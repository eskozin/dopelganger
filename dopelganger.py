# имитационная модель использования личного транспорта
import numpy
import numpy as np
import matplotlib.pyplot as plt
import seaborn; seaborn.set()
import pylab
import pandas as pd

# количество дней измерений
trials = 365

# задаем периодичность ТО maintenence_periodicity
maintenence_periodicity = 1000

# создаем функцию генерации массива с нормальным распределением с медианой median, стандартным отклонением deviation и кол-вом значений number_of_gen
def array_generation(number_of_gen, median, deviation):
    array = []
    for i in range(number_of_gen):
        array.append(np.random.normal(median, deviation))
    return array

# создаем функцию показа гистограммы
def draw_hystogram(array):
    pylab.hist(array, edgecolor='white')
    pylab.show()

# создаем функцию выгрузки в excel файл
def upload_to_excel(array):
    df = pd.DataFrame(array)
    filepath = r'C:\Users\Evgeniy\desktop\{}.xlsx'.format('array')
    df.to_excel(filepath, index=False)

# создаем переменную mileage_per_year суточного пробега одного ТС в течение заданного количества trials
mileage_per_period = array_generation(trials, 20, 5)

# создаем массив с типом дорожного покрытия
road_type = array_generation(trials,3,0)

# рисуем гистограммы
draw_hystogram(mileage_per_period)
draw_hystogram(road_type)

#выгружаем массивы в файл Excel на рабочий стол
upload_to_excel(mileage_per_period)

# создаем из исходного массива массив mileage_growth с нарастающей наработкой
# для начала объявляем массив с нулями и преобразуем его в вектор-столбец
mileage_growth = (np.zeros(trials, dtype=int))[:, np.newaxis]
amount_of_maintenance = (np.zeros(trials, dtype=int))[:, np.newaxis]

maintenance_count = 1
for i in range(1, len(mileage_per_period)):
    mileage_growth[i] = mileage_per_period[i] + mileage_growth[i - 1]
    # посчитаем количество ТО за период,
    if mileage_growth[i] >= maintenence_periodicity * maintenance_count:
        maintenance_count += 1
        amount_of_maintenance[i] = 1
    else:
        amount_of_maintenance[i] = 0

# print(mileage_growth)
# print(amount_of_maintenance)
# сколько значений масива больше 0?
print(np.count_nonzero(amount_of_maintenance > 0))
# есть ли в массиве значения больше 0
print(np.any(amount_of_maintenance > 0))
# есть ли в массиве значение больше 800, но меньше 2000?
print(np.sum((mileage_growth > 800) & (mileage_growth < 2000)))

# рисуем график нарастающего пробега
# plt.plot(mileage_growth, mileage_growth)
# plt.show()
