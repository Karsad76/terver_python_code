"""
Задача 3. Рост дочерей 175, 167, 154, 174, 178, 148, 160, 167, 169, 170
Рост матерей 178, 165, 165, 173, 168, 155, 160, 164, 178, 175

Используя эти данные построить 95% доверительный интервал для разности среднего
роста родителей и детей.
"""

import numpy as np
from scipy import stats

# исходные данные
mothers = np.array([175, 167, 154, 174, 178, 148, 160, 167, 169, 170])
daughters = np.array([178, 165, 165, 173, 168, 155, 160, 164, 178, 175])
p = 0.95
a = 1 - p

# определяем среднюю дисперсию по 2м выборкам и S-дельта
d = ((mothers.var(ddof=1) + daughters.var(ddof=1)) / 2)
s_delta = np.sqrt(d / mothers.shape[0] + d / daughters.shape[0])

print(f"d = {d}, S-дельта = {s_delta}")

# определяем t-критерий для распределения Стьюдента
t1 = stats.t.ppf(a / 2, df=((mothers.shape[0] - 1) + (daughters.shape[0] - 1)))
t2 = stats.t.ppf(1 - a / 2,
                 df=((mothers.shape[0] - 1) + (daughters.shape[0] - 1)))
print(f"t-критерий: {t1, t2}")

# определяем границы доверительного интервала для разности среднего роста
x_left = mothers.mean() - daughters.mean() - np.abs(t1 * s_delta)
x_right = mothers.mean() - daughters.mean() + np.abs(t1 * s_delta)

print(f"Доверительный интервал для разности среднего роста родителей и детей"
      f" с надежностью 0.95: {x_left, x_right}")
