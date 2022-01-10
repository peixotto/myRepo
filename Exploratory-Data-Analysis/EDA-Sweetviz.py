# Importing libraries
import seaborn as sns
import sweetviz as sv

# Loading dataset diamonds from seaborn sample datasets
df = sns.load_dataset('diamonds')
print(df)

# Sweetviz ANALYZE function
report = sv.analyze(df)
report.show_html()

# Sweetviz COMPARE function. Compare two datasets
# training_data = df.sample(frac=0.8, random_state=1)
# testing_data = df.drop(training_data.index)
# report2 = sv.compare([training_data,'Training Data'],[testing_data, 'Testing Data'])
# report2.show_html()

# Sweetviz COMPARE intra function. Compare data within same feature
# report3 = sv.compare_intra(df, df['color'] == 'D', ['D','Other colors'])
# report3.show_html()