# Importing libraries
import seaborn as sns
from skimpy import skim

# Loading dataset diamonds from seaborn sample datasets
df = sns.load_dataset('diamonds')
skim(df)