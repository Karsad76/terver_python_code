"""
Провести дисперсионный анализ для определения того, есть ли различия среднего
роста среди взрослых футболистов, хоккеистов и штангистов. Даны значения роста
в трех группах случайно выбранных спортсменов:
Футболисты: 173, 175, 180, 178, 177, 185, 183, 182.
Хоккеисты: 177, 179, 180, 188, 177, 172, 171, 184, 180.
Штангисты: 172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170.
"""

import numpy as np
from scipy import stats

x_soccer = np.array([173, 175, 180, 178, 177, 185, 183, 182])
x_hockey = np.array([177, 179, 180, 188, 177, 172, 171, 184, 180])
x_weight = np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])
a = 0.05

# H0: mu1 = mu2 = mu3
# H1: H1.1: mu1 != mu2
#     H1.2: mu1 != mu3
#     H1.3: mu2 != mu3

# определяем F-критерий Фишера
print(stats.f_oneway(x_soccer, x_hockey, x_weight))
# OUT: F_onewayResult(statistic=5.500053450812596, pvalue=0.010482206918698693)

# Т.к. pvalue < a, H0 отвергается с вероятностью ошибки 0.05
