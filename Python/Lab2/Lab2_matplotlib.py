# 25/2/25

# Install MatplotLib

"""Line Graph"""

from matplotlib import pyplot as plt

years = [1950,1960,1970,1980,1990,2000,2010]
gdp = [300.2,543.3,1075.9,2862.5,5979.6,10289.7,14958.7]
plt.plot(years,gdp,color="red",marker="o",linestyle="solid")
plt.show()