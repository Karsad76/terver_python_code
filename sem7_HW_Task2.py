"""
Задача 2. Исследовалось влияние препарата на уровень давления пациентов.
Сначала измерялось давление до приема препарата, потом через 10 минут и
через 30 минут. Есть ли статистически значимые различия между измерениями
давления? В выборках не соблюдается условие нормальности.
1е измерение до приема препарата: 150, 160, 165, 145, 155
2е измерение через 10 минут: 140, 155, 150, 130, 135
3е измерение через 30 минут: 130, 130, 120, 130, 125
"""

# Т.к. сравниваем более двух зависимых выборок  и  условие нормального
# распределения генеральной последовательности не соблюдается, применяем
# критерий Фридмана

import numpy as np
from scipy import stats

# H0: mu1 = mu2 = mu3,
# H1: mu1 != mu2 != mu3

x_before = np.array([150, 160, 165, 145, 155])
x_10min = np.array([140, 155, 150, 130, 135])
x_30min = np.array([130, 130, 120, 130, 125])
a = 0.05

print(stats.friedmanchisquare(x_before, x_10min, x_30min))
# OUT: FriedmanchisquareResult(statistic=9.578947368421062,
# pvalue=0.00831683351100441)

# Т.к. pvalue < a, гипотеза НО отвергается с вероятностью ошибки 0.05
