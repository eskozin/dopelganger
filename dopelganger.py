#имитационная модель использования личного транспорта
import numpy as np
import matplotlib.pyplot as plt
import seaborn; seaborn.set()

#задаем периодичность ТО maintenence_periodicity
maintenence_periodicity = 1000

#создаем переменную mileage_per_year суточного пробега одного ТС в течение года типа вертикальный numpy массив
#нормальное распределение, 20 км/сут - медиана, 5 - стандартное отклонение, 365 - кол-во строк, 1 - кол-во столбцов
mileage_per_year = np.random.normal(20,5,(365,1))

#создаем из исходного массива массив mileage_growth с нарастающей наработкой
#для начала объявляем массив с нулями и преобразуем его в вектор-столбец
mileage_growth = (np.zeros(365,dtype=int))[:,np.newaxis]
amount_of_maintenance = (np.zeros(365,dtype=int))[:,np.newaxis]

maintenance_count = 1
for i in range(1,len(mileage_per_year)):
    mileage_growth[i]= mileage_per_year[i]+mileage_growth[i-1]
    # посчитаем количество ТО за период,
    if mileage_growth[i] >= maintenence_periodicity * maintenance_count:
        maintenance_count += 1
        amount_of_maintenance[i] = 1
    else:
        amount_of_maintenance[i] = 0

print(mileage_growth)
print(amount_of_maintenance)

#рисуем график нарастающего пробега
plt.plot(mileage_growth, mileage_growth)
plt.show()


