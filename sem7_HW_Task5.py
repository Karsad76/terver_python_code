"""
Задача 5. Заявляется, что партия изготавливается со средним арифметическим
2,5 см. Проверить данную гипотезу, если известно, что размеры изделий
подчинены нормальному закону распределения.
Объем выборки 10, уровень статистической значимости 5%
2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34
"""
import numpy as np
from scipy import stats

# Т.к. СКО генеральной последовательности неизвестно и условие нормального
# распределения ГП соблюдается, используем t-критерий распределения Стьюдента

# H0: mu = 2.5, H1: mu != 2.5

# исходные данные
df = np.array([2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34])
mu = 2.5
a = 0.05

std = np.std(df, ddof=1)
n = len(df)
x_mean = np.mean(df)
print(f"M = {x_mean}, СКО = {std}")
# OUT: M = 2.5279999999999996, СКО = 0.1572542173961923

# определяем t-критерий для выборки
t_x = (x_mean - mu) / (std / np.sqrt(n))
print(f"t-критерий для выборки = {t_x}")
# OUT: t-критерий для выборки = 0.5630613661802959

# определяем t для ЛКО и ПКО
t_left = stats.t.ppf(a / 2, df=n - 1)
t_right = stats.t.ppf(1 - a / 2, df=n - 1)
print(f"t(ЛКО) = {t_left}, t(ПКО) = {t_right}")
# OUT: t(ЛКО) = -2.262157162740992, t(ПКО) = 2.2621571627409915

# Т.к. t(ЛКО) < t_x < t(ПКО), t-критерий выборки не принадлежит критической
# зоне и гипотеза Н0 не отвергается на уровне значимости 0,05
