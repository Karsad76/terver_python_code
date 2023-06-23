"""
Задача 3. Исследовалось влияние препарата на уровень давления пациентов.
Сначала измерялось давление до приема препарата, потом через 10 минут.
Есть ли статистически значимые различия между измерениями давления?
В выборках не соблюдается условие нормальности.
1е измерение до приема препарата: 150, 160, 165, 145, 155
2е измерение через 10 минут: 140, 155, 150, 130, 135
"""

# Т.к. сравниваем две зависимые выборки и условие нормального распределения
# генеральной последовательности не соблюдается, применяем критерий Уилкоксона

import numpy as np
from scipy import stats

# H0: mu1 = mu2
# H1: mu1 != mu2

x_before = np.array([150, 160, 165, 145, 155])
x_10min = np.array([140, 155, 150, 130, 135])
a = 0.05

print(stats.wilcoxon(x_before, x_10min))
# OUT: WilcoxonResult(statistic=0.0, pvalue=0.0625)

# Т.к. pvalue > a, гипотеза НО не отвергается на уровне значимости 0.05
