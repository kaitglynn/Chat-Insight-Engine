```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class DataAnalysis:
    def __init__(self, data):
        self.data = data

    def analyze_data(self):
        # Perform data analysis
        df = pd.DataFrame(self.data)
        summary = df.describe()
        return summary

    def visualize_data(self, column1, column2):
        # Visualize data
        df = pd.DataFrame(self.data)
        plt.figure(figsize=(10,6))
        sns.scatterplot(data=df, x=column1, y=column2)
        plt.title(f'{column1} vs {column2}')
        plt.show()

# Example usage:
# data = {'column1': [1, 2, 3, 4, 5], 'column2': [5, 4, 3, 2, 1]}
# analysis = DataAnalysis(data)
# print(analysis.analyze_data())
# analysis.visualize_data('column1', 'column2')
```