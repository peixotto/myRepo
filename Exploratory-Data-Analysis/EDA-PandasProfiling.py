# Importing libraries
import seaborn as sns
import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport


# Loading dataset diamonds from seaborn sample datasets
df = pd.DataFrame(sns.load_dataset('diamonds'))

# Pandas PROFILEREPORT method
report = ProfileReport(df, title='Diamonds Pandas Profiling Report')

# Visualizing the report
# report.to_widgets()     
report.to_html()
