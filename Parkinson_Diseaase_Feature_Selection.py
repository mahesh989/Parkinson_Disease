#Author: Maheshwor Tiwari
# Parkinson Disease: Feature Selections

"""  Data Loading """
import numpy as np
import pandas as pd
df = pd.read_csv('./po1_data.txt')


# finding number of rows and columns
df.shape
#Show first 5 rows of the dataset 
df.head()
# Display basic information about the dataset
print(df.info())
# Check for any missing values in the entire dataset
print(df.isnull().sum().sum())
# Check for duplicate rows in the dataset
duplicate_rows = df[df.duplicated()]
print("Number of duplicate rows:", duplicate_rows.shape[0])
####################################################################


"""Define the new column names"""

new_column_names = [
    "Subject_ID", "Jitter(%)", "Jitter(Abs)", "Jitter(RAP)", "Jitter(PPQ5)", 
    "Jitter(DDP)", "Shimmer(%)", "Shimmer(Abs)", "Shimmer(APQ3)", "Shimmer(APQ5)", 
    "Shimmer(APQ11)", "Shimmer(DD)", "Harmonicity", "NHR", "HNR",
    "MedianPitch", "MeanPitch", "StdDevPitch", "MinPitch", "MaxPitch",
    "NumPulses", "NumPeriods", "MeanPeriod", "StdDevPeriod",
    "FractionUnvoicedFrames", "NumVoiceBreaks", "DegreeVoiceBreaks",
    "UPDRS", "PD Indicator"
]
# Rename the columns using the new names
df.columns = new_column_names
# Display the updated column names
print(df.columns)
df.head()
####################################################################


""" Bar Diagram: PD Indicator  """
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="whitegrid")
plt.figure(figsize=(6, 4))

ax = sns.countplot(x='PD Indicator', data=df, palette=["#1f77b4", "#ff7f0e"])
plt.xlabel('PD Indicator')
plt.ylabel('Count')
plt.title('Distribution of PD Indicator')
plt.xticks([0, 1], ['Healthy', 'PD'])

# Adding integer count numbers on top of the bars
for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', fontsize=10, color='black', xytext=(0, 5),
                textcoords='offset points')

plt.show()
####################################################################


""" Divide the dataset into two groups based on PD indicator """

df1 = df[df["PD Indicator"] == 0]
df2 = df[df["PD Indicator"] == 1]
print(df1) 
print(df2)
df1.shape
df2.shape
# Calculate summary statistics for the DataFrame
df1.describe()
df2.describe()
####################################################################


"""Central Tendencies and Difference between them """
# Select the columns for comparison (excluding "Subject_ID" and "PD Indicator")
columns_to_compare = df1.columns.difference(["Subject_ID", "PD Indicator"])
# Calculate the differences between describe statistics for df2 and df1
differences = df2[columns_to_compare].describe() - df1[columns_to_compare].describe()
# Extract the desired statistics (mean, median, std, min, max) from the differences DataFrame
desired_statistics = ["mean", "50%", "std"]
differences = differences.loc[desired_statistics]
# Transpose the differences DataFrame for desired display format
differences = differences.transpose()
differences

# Display the differences
print("Differences between central tendencies of df2 and df1:")
print(differences)
# Calculate the absolute differences
absolute_differences = differences.abs()

# Sort the absolute differences DataFrame by mean values in descending order
sorted_absolute_differences = absolute_differences.sort_values(by=["mean"], ascending=False)

# Get the indices of the top 10 absolute differences
top_10_indices = sorted_absolute_differences.head(10).index

# Display the top 10 absolute differences with the original sign
print("Top 10 Absolute Differences between central tendencies \n of df2 and df1 by Mean:")
print(differences.loc[top_10_indices])
####################################################################



"""  Histograpm Plotting"""
import matplotlib.pyplot as plt
import seaborn as sns
# Select numeric columns for histograms
numeric_columns = df1.select_dtypes(include=['float64', 'int64']).columns

# Exclude specific columns
columns_to_exclude = ["Subject_ID", "PD Indicator"]
numeric_columns = numeric_columns.difference(columns_to_exclude)

# Set up the Seaborn style
sns.set(style="whitegrid")

# Define custom color palette for histograms
custom_color_palette = sns.color_palette(["#1f77b4", "#ff7f0e"])  # Blue and orange

# Define hatch patterns for healthy and unhealthy individuals
hatch_patterns = ["", "////"]  # No hatch for healthy, hatch for unhealthy

# Function to plot side-by-side histograms with hatch patterns
def plot_side_by_side_histograms(dataframe1, dataframe2, title):
    plt.figure(figsize=(40, 30))
    for i, column in enumerate(numeric_columns, start=1):
        plt.subplot(6, 5, i)
        sns.histplot(dataframe1[column], bins=10, kde=True, color=custom_color_palette[0], hatch=hatch_patterns[0])
        sns.histplot(dataframe2[column], bins=10, kde=True, color=custom_color_palette[1], hatch=hatch_patterns[1])
        plt.title(column, fontsize=25)  # Set individual histogram title font size
        plt.xlabel("Value", fontsize=25)
        plt.ylabel("Frequency", fontsize=25)
        plt.legend(labels=["Healthy", "Unhealthy"])

    plt.tight_layout()
    plt.suptitle(f"Histogram Comparison for {title}", fontsize=30)
    plt.subplots_adjust(top=0.92)
    plt.show()

# Plot side-by-side histograms for df1 (healthy) and df2 (unhealthy)
plot_side_by_side_histograms(df1, df2, "Healthy vs Unhealthy")
####################################################################


"""  Box Plotting """
import matplotlib.pyplot as plt
import seaborn as sns

# Select numeric columns for box plots
numeric_columns = df1.select_dtypes(include=['float64', 'int64']).columns

# Exclude specific columns
columns_to_exclude = ["Subject_ID", "PD Indicator"]
numeric_columns = numeric_columns.difference(columns_to_exclude)

# Set up the Seaborn style
sns.set(style="whitegrid")

# Create a 6 by 5 grid of axes for the box plots
fig, axes = plt.subplots(6, 5, figsize=(40, 30))
axes = axes.flatten()

# Create a box plot for each numeric column in df1 and df2
for i, column in enumerate(numeric_columns):
    sns.boxplot(data=df1, x="PD Indicator", y=column, ax=axes[i], color="blue")
    sns.boxplot(data=df2, x="PD Indicator", y=column, ax=axes[i], color="orange")
    
    # Add hatches for the boxes
    for patch in axes[i].artists:
        patch.set_hatch('//')

    axes[i].set_title(column, fontsize=20)
    axes[i].set_xlabel("PD Indicator", fontsize=15)
    axes[i].set_ylabel("Value", fontsize=15)
    axes[i].tick_params(axis="both", labelsize=12)

plt.tight_layout()
plt.suptitle("Box Plot Comparison for Healthy and Unhealthy Individuals", fontsize=30)
plt.subplots_adjust(top=0.92)
plt.legend(labels=["Healthy", "Unhealthy"])
plt.show()
####################################################################


"""  Confidence Interval """
import pandas as pd
import numpy as np
from scipy.stats import t
# List of features/columns in your dataset
features = df1.columns.difference(["Subject_ID", "PD Indicator"])

# Initialize empty lists to store results
selected_features = []
mean_differences = []
confidence_intervals = []
absolute_mean_differences = []  # New list to store absolute mean differences

# Loop through each feature
for feature in features:
    # Calculate mean and standard error for each group
    mean_healthy = df1[feature].mean()
    mean_unhealthy = df2[feature].mean()
    std_error_healthy = df1[feature].std() / np.sqrt(len(df1))
    std_error_unhealthy = df2[feature].std() / np.sqrt(len(df2))
    
    # Calculate the t-statistic
    t_statistic = (mean_unhealthy - mean_healthy) / np.sqrt(std_error_healthy**2 + std_error_unhealthy**2)
    
    # Calculate degrees of freedom for the t-distribution
    dof = len(df1) + len(df2) - 2
    
    # Calculate the critical value for the t-distribution
    t_critical = t.ppf(0.975, dof)  # 95% confidence level
    
    # Calculate the margin of error
    margin_of_error = t_critical * np.sqrt((std_error_healthy**2 + std_error_unhealthy**2) / 2)
    
    # Calculate the confidence interval
    ci_lower = (mean_unhealthy - mean_healthy) - margin_of_error
    ci_upper = (mean_unhealthy - mean_healthy) + margin_of_error
    
    # Check if confidence intervals do not overlap
    if ci_lower > 0 or ci_upper < 0:
        selected_features.append(feature)
        mean_difference = mean_unhealthy - mean_healthy
        mean_differences.append(mean_difference)
        confidence_intervals.append((ci_lower, ci_upper))
        absolute_mean_differences.append(abs(mean_difference))  # Add the absolute mean difference

# Create a DataFrame to store the results
feature_selection_results = pd.DataFrame({
    'Feature': selected_features,
    'Mean Difference': mean_differences,
    'Confidence Interval': confidence_intervals,
    'Absolute Mean Difference': absolute_mean_differences  # Add the absolute mean difference column
})

# Sort features based on larger absolute mean differences and narrower CIs
sorted_results = feature_selection_results.sort_values(by=['Absolute Mean Difference', 'Confidence Interval'], ascending=[False, True])

# Drop the "Absolute Mean Difference" column
sorted_results = sorted_results.drop(columns='Absolute Mean Difference')

# Print the sorted results with formatting
pd.options.display.float_format = '{:.3f}'.format
print(sorted_results.to_string(index=False))


# Define the file path where you want to save the top 10 results
output_file_path = 'sorted_results.csv'

# Save the top 10 rows of the sorted results to a CSV file
top_10_sorted_results = sorted_results.head(10)
top_10_sorted_results.to_csv(output_file_path, index=False)

print("Top 10 results saved to", output_file_path)
####################################################################




"""  Hypothesis Testing """
import numpy as np
from scipy.stats import norm
# List of features/columns in your dataset
features = df1.columns.difference(["Subject_ID", "PD Indicator"])
# Set the significance level
alpha = 0.05
# Initialize empty lists to store results
reject_results = []
fail_to_reject_results = []
# Loop through each feature
for feature in features:
    # Calculate sample means and standard deviations
    mean_healthy = df1[feature].mean()
    mean_unhealthy = df2[feature].mean()
    std_healthy = df1[feature].std()
    std_unhealthy = df2[feature].std()
    n_healthy = len(df1)
    n_unhealthy = len(df2)
    # Calculate the pooled standard error
    pooled_std = np.sqrt((std_healthy**2 / n_healthy) + (std_unhealthy**2 / n_unhealthy))
    # Calculate the z-score
    z_score = (mean_unhealthy - mean_healthy) / pooled_std
    # Calculate the critical z-value for two-tailed test
    critical_z = norm.ppf(1 - alpha / 2)
    # Perform the hypothesis test
    result_dict = {
        "Feature": feature,
        "Z-Score": z_score,
        "Critical Z-Value": critical_z,
        "Result": "Reject H0" if np.abs(z_score) > critical_z else "Fail to reject H0"
    }
    # Store the results in the appropriate list
    if result_dict["Result"] == "Reject H0":
        reject_results.append(result_dict)
    else:
        fail_to_reject_results.append(result_dict)
# Create DataFrames for the results
reject_results_df = pd.DataFrame(reject_results)
fail_to_reject_results_df = pd.DataFrame(fail_to_reject_results)

# Display the results for "Reject H0"
print("Reject H0:")
print(reject_results_df)

# Display the results for "Fail to reject H0"
print("\nFail to reject H0:")
print(fail_to_reject_results_df)


# Create DataFrames for the results
reject_results_df = pd.DataFrame(reject_results)
fail_to_reject_results_df = pd.DataFrame(fail_to_reject_results)

# Define the file paths for saving the results
reject_output_file_path = 'reject_results.csv'
fail_to_reject_output_file_path = 'fail_to_reject_results.csv'

# Save the results to CSV files
reject_results_df.to_csv(reject_output_file_path, index=False)
fail_to_reject_results_df.to_csv(fail_to_reject_output_file_path, index=False)

print("Rejected results saved to", reject_output_file_path)
####################################################################


"""  Plot of confidence Interval and Mean differences """

import matplotlib.pyplot as plt
# Extract confidence interval lower and upper bounds
sorted_results['CI_Lower'] = sorted_results['Confidence Interval'].apply(lambda x: x[0])
sorted_results['CI_Upper'] = sorted_results['Confidence Interval'].apply(lambda x: x[1])

# Plot mean differences with confidence intervals
plt.figure(figsize=(10, 6))
plt.errorbar(sorted_results['Feature'], sorted_results['Mean Difference'], yerr=[sorted_results['Mean Difference'] - sorted_results['CI_Lower'], sorted_results['CI_Upper'] - sorted_results['Mean Difference']], fmt='o')
plt.xlabel('Feature')
plt.ylabel('Mean Difference')
plt.title('Mean Differences with Confidence Intervals')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
####################################################################

""" Saving the data for Null Hypothesis and sorted mean differences """
df3 = pd.read_csv('./reject_results.csv')
df4 = pd.read_csv('./sorted_results.csv')
common_features = np.intersect1d(df3['Feature'], df4['Feature'])
print("Common features:")
print(common_features)

selected_df1 = df1[common_features]
selected_df2 = df2[common_features]
common_features












