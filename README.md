# Diagnosing Parkinson's Disease using Voice Sample Data Analysis

## Project Overview

Parkinson's Disease (PD) stands as a formidable challenge in the realm of neurological disorders. A progressive movement disorder affecting the nervous system, PD manifests through debilitating symptoms such as tremors, rigidity, bradykinesia, and postural instability[^1^]. While notable figures like Muhammad Ali, Michael J. Fox, and Pope John Paul II have grappled with PD, there remains no known cure for this affliction[^2^].

Diagnosing PD presents intricate challenges due to the lack of specific diagnostic tests and the invasive nature of some existing procedures. Blood tests, laboratory assessments, and brain scans are used to exclude other potential disorders, but these approaches often involve rigorous processes that can add to the distress of those affected by PD[^1^].

This project embarks on an exploration of a non-invasive diagnostic avenue using voice sample data analysis. The aspiration is to harness distinctive features in the acoustic properties of individuals' voices to discern between those affected by PD and those who are not. By probing these acoustic markers, the project aims to contribute to the development of an accessible and reliable diagnostic tool for PD.

## Project Objective

This project focuses on leveraging voice sample data analysis as a potential non-invasive method for diagnosing PD. The goal is to identify specific acoustic markers within voice samples that can distinguish between individuals with PD and those without the condition. By analyzing a set of acoustic features extracted from voice recordings, the project aims to contribute to the development of an accessible and reliable diagnostic tool for PD.

## Dataset and Methodology

The project utilizes the `po1_data.txt` dataset, comprising voice samples collected from both PD patients and healthy individuals. Each participant recorded 26 voice samples, encompassing sustained vowels, numbers, words, and sentences. Acoustic features extracted using Praat, a free acoustic analysis software[^3^], provide the foundation for subsequent analyses.

## Key Steps and Insights

The project unfolds through a series of steps:
### 1. Data Loading and Preprocessing

The dataset was loaded and preprocessed to prepare it for analysis. It consists of 1039 entries and 29 columns, each representing different acoustic features extracted from voice recordings. The data underwent the following steps:

#### 1.1 Data Dimensions

The dataset has a shape of (1039, 29), indicating 1039 instances and 29 features.
![Image Alt Text](Dataset_columns.png)



#### 1.2 Data Information

The information about the dataset was obtained using the `.info()` method. It confirmed that the dataset contains no missing values, and all columns have either `float64` or `int64` data types.

#### 1.3 Duplicate Rows

Duplicate rows were checked using the `.duplicated()` method. No duplicate rows were found in the dataset.

#### 1.4 Column Renaming

To improve clarity, the column names were updated with more meaningful labels. The new column names provide insights into the acoustic attributes they represent.

#### 1.5 Data Division

The dataset was divided into two subsets based on the "PD Indicator" column:

- `df1`: Voice samples from individuals without PD (Healthy). It contains 520 instances and 29 features.
- `df2`: Voice samples from individuals with PD (Affected). It contains 519 instances and 29 features.

These subsets will be used for comparative analysis and visualization to explore differences between healthy and PD-affected individuals.


### 2. Descriptive Analysis
In this section, we conducted a descriptive analysis of two sub-datasets representing individuals without Parkinson's disease (PD) and those with PD.
#### 2.1 Central Tendency 
Our objective was to elucidate disparities in central tendencies and variability between the two groups. We initiated the analysis by calculating summary statistics using the .describe() function for both datasets, excluding irrelevant columns like 'subject_id'. Since there are 29 columns we may not be able to capture all the key details. To get a better glimpse, subsequently, we computed the differences in key statistics, focusing on mean, median, and standard deviation, to reveal insights into the impact of PD on these attributes. 

| Feature                 | Mean Difference | Median Difference | StdDev Difference |
|-------------------------|-----------------|-------------------|------------------|
| MaxPitch                | -33.810474      | -14.8815          | -21.029639       |
| UPDRS                   | 24.003854       | 23.0000           | 14.752265        |
| NumPeriods              | 13.980606       | 6.5000            | 65.491394        |
| NumPulses               | 12.222718       | 5.0000            | 64.193786        |
| MeanPitch               | -11.558032      | -12.0885          | -13.053128       |
| MedianPitch             | -9.447163       | -9.5840           | -16.707123       |
| StdDevPitch             | -8.851501       | -4.1670           | -4.050640        |
| MinPitch                | -5.580112       | -4.4405           | -7.840752        |
| FractionUnvoicedFrames  | -5.068937       | -6.9150           | -0.342389        |
| DegreeVoiceBreaks       | -3.803388       | -5.5395           | -2.463653        |

The project's feature selection reveals significant differences between Parkinson's disease present and absent datasets. The largest difference is in "MaxPitch," with a mean difference of 33.81 and significant deviations in median and standard deviation. The study also shows divergence in severity scores in "UPDRS," speech pattern attributes like "NumPeriods," and significant differences in mean and median in "MeanPitch," "MedianPitch," and "StdDevPitch." These findings provide insights into key differentiating features, guiding the selection of features for effective discrimination between Parkinson's disease cases and healthy subjects in the project.

#### 2.2 Histogram
![Image Alt Text](Histogram.png)







2. **Descriptive 
3. **Visual Comparison**: Visualizations, including side-by-side histograms and box plots, allowed for intuitive comparisons of feature distributions between the two groups.

4. **Mean Differences and Confidence Intervals**: By computing mean differences and confidence intervals, the project ranked features based on their differentiating potential.

5. **Hypothesis Testing**: Z-scores were leveraged for hypothesis testing to ascertain the statistical significance of mean differences.

6. **Visualizing Confidence Intervals**: The visualization of confidence intervals elucidated the practical implications of calculated mean differences.

## Implications and Future Directions

The project's analyses and visualizations unveiled notable discrepancies in acoustic features between healthy individuals and those with PD. These findings hold promise for the advancement of a non-invasive diagnostic instrument for PD, potentially enabling timelier interventions and improved patient outcomes.

Future research avenues could involve larger datasets, integration of machine learning techniques for predictive modeling, and clinical validation to assess the reliability of identified acoustic markers.

## Conclusion

In the medical landscape, this project showcases the potency of data-driven insights by harnessing voice sample data to diagnose PD. Through rigorous statistical analyses and insightful visualizations, key acoustic features were illuminated, contributing to the quest for an accurate, non-invasive, and accessible diagnostic tool for Parkinson's Disease.

## References

[^1^]: National Institute of Neurological Disorders and Stroke. (2023). Parkinson's Disease Information Page. [https://www.ninds.nih.gov/healthinformation/disorders/parkinsons-disease](https://www.ninds.nih.gov/healthinformation/disorders/parkinsons-disease)
[^2^]: Parkinson's Foundation. (2023). Notable Figures. [https://www.parkinson.org/understanding-parkinsons/statistics/notable-figures](https://www.parkinson.org/understanding-parkinsons/statistics/notable-figures)
[^3^]: Sakar, B.E. et al. (2013). [https://ieeexplore.ieee.org/abstract/document/6451090](https://ieeexplore.ieee.org/abstract/document/6451090) and [https://www.fon.hum.uva.nl/praat/](https://www.fon.hum.uva.nl/praat/)
