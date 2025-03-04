'''Write a Python program using a lambda function to convert temperatures from Celsius to Kelvin,
store the data in a tabular format using pandas, and visualize the data using a plot.'''

import pandas as pd
import matplotlib.pyplot as plt

print('''Name: Sidhanta Barik, RegNo: 2241002049
-----------------------------------------''')
C = [0, 10, 20, 30, 36, 40, 50, 60, 70, 80, 90, 100]
K = list(map(lambda x : x + 273.15, C))
df = pd.DataFrame({'Celsius': C, 'Kelvin': K})
print(df)

plt.plot(df['Celsius'], df['Kelvin'], 'r')
plt.xlabel('Celsius')
plt.ylabel('Kelvin')
plt.title('Celsius vs Kelvin')
plt.show()

# Name: Sidhanta Barik, RegNo: 2241002049
# -----------------------------------------
#     Celsius  Kelvin
# 0         0  273.15
# 1        10  283.15
# 2        20  293.15
# 3        30  303.15
# 4        36  309.15
# 5        40  313.15
# 6        50  323.15
# 7        60  333.15
# 8        70  343.15
# 9        80  353.15
# 10       90  363.15
# 11      100  373.15

# The data is stored in a tabular format using pandas and visualized using a plot.
