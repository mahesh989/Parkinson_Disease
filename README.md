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

1. **Data Exploration and Wrangling**: The dataset underwent initial examination, including dimensions, missing values, and duplicates. Basic statistics were obtained to inform subsequent analyses.

2. **Descriptive and Inferential Analysis**: To discern meaningful features, descriptive statistics were calculated for healthy and PD-affected groups. Inferential analyses, notably t-tests, facilitated the identification of statistically significant differences.

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
