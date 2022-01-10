# Importing libraries
import seaborn as sns
from dataprep.eda import create_report

# Loading dataset diamonds from seaborn sample datasets
df = sns.load_dataset('diamonds')
print(df)

# Dataprep CREATE REPORT
create_report(df)

