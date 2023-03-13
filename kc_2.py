import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r'C:\Users\PC\Desktop\Coding Class\kcheck\Data_1_checks\assets\Inflation.csv', encoding='ISO-8859-1')
print(df.head(10))

# Plot a scatterplot of Inflation rate for the first 30 rows
sns.scatterplot(x=df['2022'][:30],
                y=df['Country'][:30])

# Add a title to the plot
plt.title('Inflation rate in 2022 for the first 30 countries')

# Show the plot
plt.show()