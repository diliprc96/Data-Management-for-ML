# Problem Formulation Document

## Business Problem

The primary business problem addressed in this project is customer churn, which occurs when existing customers stop using a company's services or purchasing its products. This issue leads to revenue declines and increased pressure on teams to compensate for the loss. The focus is on addressable churn, where intervention could prevent customer loss, as opposed to non-addressable churn due to unavoidable circumstances. Reducing customer churn is critical for maintaining revenue and competitive advantage, especially in the face of new fintech companies attracting customers away from traditional financial institutions.

## Key Business Objectives

1. **Reduce Customer Churn:** Develop strategies to retain existing customers and minimize churn rates.

2. **Enhance Predictive Analytics:** Implement a robust machine learning model to predict customer churn effectively.

3. **Optimize Revenue Streams:** By reducing churn, stabilize and potentially increase revenue.

4. **Improve Customer Retention Strategies:** Use insights from predictive models to inform retention strategies and interventions.

## Key Data Sources and Attributes

1. **Web Logs:** Capture customer interactions and behaviors on the company's website.
   - Attributes: Page views, session duration, click paths.

2. **Transactional Systems:** Record customer purchase history and transaction details.
   - Attributes: Purchase frequency, transaction amounts, product categories.

3. **Third-party APIs:** Gather additional customer data from external sources.
   - Attributes: Demographic information, social media activity, credit scores.

## Expected Outputs from the Pipeline

1. **Clean Datasets for EDA:** Provide datasets free from inconsistencies and missing values for exploratory data analysis.

2. **Transformed Features for Machine Learning:** Engineer features suitable for model training, including aggregated and derived features.

3. **Deployable Model to Predict Customer Churn:** Develop a machine learning model capable of predicting churn with high accuracy and reliability.

## Measurable Evaluation Metrics

1. **Accuracy:** Measure the percentage of correct predictions made by the model.

2. **Precision:** Evaluate the proportion of positive identifications that were actually correct.

3. **Recall:** Assess the model's ability to identify all relevant instances of churn.

4. **F1 Score:** Provide a balance between precision and recall, offering a single metric for model performance evaluation. 