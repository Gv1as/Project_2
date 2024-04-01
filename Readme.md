# Vanguard Digital Experiment Analysis
## Introduction:

This project delves into the evaluation of Vanguard's digital experiment conducted to enhance customer experience through UI enhancement. The primary focus is to assess the impact of a redesigned digital interface on user engagement and process completion rates. By analyzing data from an A/B test, we aim to uncover insights that inform Vanguard's digital strategy and drive improvements in customer satisfaction.

## Data Used:

Client Profiles: Demographic data providing insights into client characteristics and preferences.
Digital Footprints: Detailed records of client interactions with Vanguard's online platform, facilitating behavior analysis.
Experiment Roster: Information on clients participating in the A/B test, enabling comparison between control and test groups.

## EDA & Data Cleaning:

After the initial dataset exploration, it was observed that there were NaN values in the "variation" column of the Experiment Roster dataset, where Test and Control groups were identified. It was decided to drop these values as they would not be needed for the KPI calculation. After this cleaning and merging the three datasets into a new one, we were left with 50,500 unique client IDs, which we used for further analysis in this project.

### Client Behavior Analysis:

Next, demographics were examined to identify the primary clients using the online process, including Age, Tenure, and Balance. By binning these demographics into groups, it was concluded that similar trends were observed for both the test and control groups:
- Age: The groups aged 30 to 49 and 50 to 69 had the most clients engaging in the online process.
- Balance: Clients with a balance between 10k and 50k were the most active participants.
- Tenure: Clients with a tenure between 6 and 10 years showed the highest level of activity.

These insights provide valuable information about the demographics of clients interacting with the online process, aiding in further analysis and decision-making processes.

### Performance Metrics

#### Success Indicators:

To determine the success of the new design, we have identified key performance indicators (KPIs) as follows:

- **Completion Rate:** The proportion of users who reach the final 'confirm' step.
- **Time Spent on Each Step:** The average duration users spend on each step.
- **Error Rates:** The percentage of sessions in which users encounter errors, indicating confusion or mistakes during the process.

#### Redesign Outcome:

Based on the chosen KPIs, the performance of the new design compared to the old one is as follows:

- **Completion Rate:**
  - Test Group: 69.29%
  - Control Group: 65.57%

- **Time Spent on Each Step (Test Group):**
  - Total Time: 323.6 seconds
  - Step 1: 30.57 seconds
  - Step 2: 36.36 seconds
  - Step 3: 86.60 seconds
  - Confirm Step: 104.83 seconds

- **Time Spent on Each Step (Control Group):**
  - Total Time: 333.1 seconds
  - Step 1: 36.8 seconds
  - Step 2: 32.9 seconds
  - Step 3: 86.2 seconds
  - Confirm Step: 127.1 seconds

- **Error Rate:**
  - Test Group: 26.96%
  - Control Group: 20.44%

These metrics provide insights into the effectiveness of the new design compared to the old one, helping to evaluate its performance and identify areas for improvement.

## Hypothesis Testing

As part of the analysis, hypothesis testing was conducted to make data-driven conclusions about the effectiveness of the redesign. The following hypotheses were tested:

### Completion Rate
One interesting hypothesis tested was related to the completion rate between the Test and Control groups. Given that the new design (Test group) exhibited a higher completion rate compared to the old design (Control group), it was necessary to confirm if this difference was statistically significant.

#### Hypotheses:
- **Null Hypothesis (H0):** There is no difference in completion rates between the Test and Control groups.
- **Alternative Hypothesis (H1):** There is a difference in completion rates between the Test and Control groups.

The statistical analysis revealed the following results:
- **Z-score:** 8.8927
- **P-value:** 0.0000

**Outcome:** The null hypothesis was rejected, indicating a significant difference in completion rates between the Test and Control groups.

### Completion Rate with a Cost-Effectiveness Threshold
Another analysis was conducted to ensure that the observed increase in completion rate from the A/B test met or exceeded Vanguard's 5% threshold for cost-effectiveness.

#### Hypotheses:
- **Null Hypothesis (H0):** The increase in completion rate does not meet or exceed the 5% threshold.
- **Alternative Hypothesis (H1):** The increase in completion rate meets or exceeds the 5% threshold.

**Outcome:** The analysis supported the rejection of the null hypothesis, indicating that the increase in completion rate met or exceeded Vanguard's 5% threshold for cost-effectiveness.

These findings provide valuable insights into the effectiveness of the redesign, both statistically and from a cost-effectiveness perspective.

## Hypothesis Testing: Analysis of Variations in average age between Test and Control Groups

**H0:** The average age of clients engaging with the new process is not significantly greater than or equal to the average age of those engaging with the old process.

**H1:** The average age of clients engaging with the new process is significantly greater than the average age of those engaging with the old process.

One-Sided T-Test Results:
- T-statistic: -2.4161
- P-value: 0.9922

**Outcome:** Fail to reject the null hypothesis: There is not enough evidence to suggest that the average age of clients engaging with the new process is significantly greater than those engaging with the old process.

## Hypothesis Testing: Analysis of Variations in Tenure between Test and Control Groups

**H0:** The average tenure of clients engaging with the new process is not significantly greater than or equal to the average tenure of those engaging with the old process.

**H1:** The average tenure of clients engaging with the new process is significantly greater than or equal to the average tenure of those engaging with the old process.

One-Sided T-Test Results:
- T-statistic: -1.6540
- P-value: 0.9509

**Outcome:** Fail to reject the null hypothesis: There is not enough evidence to suggest that the average tenure of clients engaging with the new process is significantly greater than those engaging with the old process.

## Hypothesis Testing: Analysis of Variations in Gender between Test and Control Groups


**H0:** The proportion of males engaging with the new process is not significantly greater than or equal to the proportion of males engaging with the old process.

**H1:** The proportion of males engaging with the new process is significantly greater than or equal to the proportion of males engaging with the old process.

Chi-Square Test Results:
- Chi-square statistic: 1.3238
- P-value: 0.2499

**Outcome:** Fail to reject the null hypothesis: There is no significant association between gender and group.

## Experiment Evaluation

### Design Effectiveness
- The experiment was well-structured, with clear divisions between the Test and Control groups.
- Clients were randomly assigned to either the old or new design, ensuring an unbiased distribution.

### Duration Assessment
- The timeframe of the experiment, spanning from 3/15/2017 to 6/20/2017, provided a substantial duration for gathering meaningful data and insights.
- Sufficient time was allocated to observe client behavior and assess the impact of the design changes.

### Additional Data Needs
- Including user feedback or surveys could offer qualitative insights into client perceptions and preferences.
- Tracking user interactions beyond the experiment period could provide insights into long-term behavior changes.
- Incorporating demographic data or segmentation could enable a deeper understanding of client preferences and behaviors.

Conclusion
The analysis of the digital experiment conducted by Vanguard has yielded insightful findings regarding the effectiveness of the new design and its impact on client behavior. Key highlights of the analysis include:

Completion Rate Improvement: The completion rate in the Test group surpassed that of the Control group. Moreover, the increase in completion rate exceeded the 5% threshold set by Vanguard for cost-effectiveness.

Time Efficiency: While there was an improvement in the total time spent on the process, further examination revealed potential areas for enhancement. Specifically, the time spent on steps 2 and 3 of the process could be optimized to streamline the user experience and reduce friction.

Error Rates: A notable observation was the higher error rates in the Test group compared to the Control group. This discrepancy warrants further investigation to identify underlying factors contributing to the differences and to implement corrective measures accordingly.

In conclusion, the digital experiment has shown promising results with a notable improvement in completion rate exceeding the set threshold. However, there remains room for refinement, particularly in optimizing step-specific time durations and addressing discrepancies in error rates. Further analysis and improvements are essential to enhance the overall user experience and ensure the success of the redesigned digital platform.


## Url presentation slides : https://www.canva.com/design/DAGA0iB61-0/uszGLnKzHXS1Qv9q7tkmIw/edit?utm_content=DAGA0iB61-0&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton