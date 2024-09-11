layout: page
title: "WTP"
permalink: /WTP

# wild-life-analytics

Analyse wild life

Willingness to Pay (WTP) in biodiversity conservation is a measure of how much individuals or society are willing to pay to preserve or enhance biodiversity. It is a key concept in environmental economics used to estimate the value of non-market goods and services. Several methods and functions are used to calculate WTP for biodiversity, including stated preference methods (like contingent valuation and choice modeling) and revealed preference methods (like hedonic pricing and travel cost methods).

### Methods to Calculate WTP in Biodiversity

1. **Contingent Valuation Method (CVM)**
   - **Description**: This method uses surveys to ask people directly how much they would be willing to pay for specific environmental benefits or to avoid certain environmental losses.
   - **Steps**:
     1. Define the biodiversity change or conservation project.
     2. Design and distribute a survey with hypothetical scenarios.
     3. Collect responses on WTP.
     4. Analyze the data using statistical methods.

2. **Choice Modeling (CM)**
   - **Description**: This method involves presenting respondents with sets of hypothetical choices, each containing different attributes with varying levels, and asking them to choose their preferred option.
   - **Steps**:
     1. Define attributes and levels related to biodiversity.
     2. Design choice sets and distribute them in surveys.
     3. Collect responses on preferences.
     4. Use econometric models (e.g., multinomial logit models) to estimate WTP for changes in attributes.

3. **Hedonic Pricing Method (HPM)**
   - **Description**: This method infers WTP from the prices of market goods that are affected by biodiversity, such as property prices or agricultural land values.
   - **Steps**:
     1. Collect data on market prices and biodiversity attributes.
     2. Use regression analysis to isolate the effect of biodiversity on prices.
     3. Estimate the implicit price of biodiversity attributes.

4. **Travel Cost Method (TCM)**
   - **Description**: This method estimates WTP based on the costs incurred by people when they visit a site with biodiversity attributes.
   - **Steps**:
     1. Collect data on travel expenses and visitor numbers.
     2. Estimate a demand curve for visits to the site.
     3. Calculate consumer surplus as a measure of WTP.

### Functions and Models Used

1. **Contingent Valuation Analysis**
   - **Logit/Probit Models**: Used to analyze binary WTP responses (yes/no).
     ```python
     from statsmodels.discrete.discrete_model import Logit

     model = Logit(y, X)
     result = model.fit()
     wtp = -result.params['constant'] / result.params['price']
     ```
   - **Linear/Non-linear Regression**: Used to analyze continuous WTP responses.
     ```python
     from statsmodels.api import OLS

     model = OLS(y, X)
     result = model.fit()
     wtp = result.params
     ```

2. **Choice Modeling Analysis**
   - **Multinomial Logit Model**: Used to estimate WTP from choice experiment data.
     ```python
     from statsmodels.discrete.discrete_model import MNLogit

     model = MNLogit(y, X)
     result = model.fit()
     wtp = result.params
     ```

3. **Hedonic Pricing Analysis**
   - **Hedonic Regression**: Used to estimate the implicit price of biodiversity attributes.
     ```python
     from statsmodels.api import OLS

     model = OLS(property_prices, biodiversity_attributes)
     result = model.fit()
     implicit_prices = result.params
     ```

4. **Travel Cost Analysis**
   - **Zonal Travel Cost Method**: Estimates WTP by analyzing the relationship between travel costs and visit rates.
     ```python
     import numpy as np
     from scipy.optimize import curve_fit

     def demand_curve(travel_cost, a, b):
         return a * np.exp(-b * travel_cost)

     params, covariance = curve_fit(demand_curve, travel_costs, visit_rates)
     wtp = np.trapz(demand_curve(travel_costs, *params), travel_costs)
     ```

### Example Calculation

**Contingent Valuation Example:**

Assume a survey where respondents are asked if they would pay a specific amount for a biodiversity project. The responses (yes/no) and the amounts offered are analyzed using a logistic regression model.

```python
import pandas as pd
import numpy as np
import statsmodels.api as sm

# Hypothetical survey data
data = pd.DataFrame({
    'response': [1, 0, 1, 0, 1, 1, 0, 1, 0, 0],
    'amount': [10, 20, 15, 25, 10, 20, 30, 15, 25, 30]
})

# Add a constant term for the intercept
data['constant'] = 1

# Fit the logistic regression model
logit_model = sm.Logit(data['response'], data[['constant', 'amount']])
result = logit_model.fit()

# Calculate WTP
wtp = -result.params['constant'] / result.params['amount']
print(f"Estimated WTP: ${wtp:.2f}")
```

This example demonstrates the process of estimating WTP using a simple logistic regression model based on contingent valuation survey data. The actual implementation can be more complex depending on the specifics of the study and data available.






The Travel Cost Method (TCM) is a revealed preference method used to estimate the economic value of ecosystem services or recreational sites by observing the expenses incurred by visitors. It relies on the assumption that the time and travel cost expenses that people incur to visit a site represent the "price" of access to that site. Here is a more detailed look at TCM:

### Types of Travel Cost Method

1. **Zonal Travel Cost Method (ZTCM)**
   - Uses data on the number of visits from different geographic zones around a site.
   - Calculates the average travel cost from each zone and the total number of visits.
   - Constructs a demand curve by relating the number of visits to the travel cost.

2. **Individual Travel Cost Method (ITCM)**
   - Uses survey data from individual visitors about their travel costs, time spent, and other relevant factors.
   - Constructs a demand function at the individual level.

### Steps to Implement the Travel Cost Method

1. **Define the Study Area and Sites**
   - Identify the recreational site or biodiversity area to be valued.
   - Define the geographic extent of the study area.

2. **Collect Data**
   - **Visitor Surveys**: Gather data on travel expenses, number of visits, distance traveled, time spent, socio-economic characteristics, and alternative sites.
   - **Secondary Data**: Obtain data on population, income levels, and other relevant variables for the zones around the site.

3. **Calculate Travel Costs**
   - Include transportation costs (fuel, vehicle wear and tear), time costs (value of time spent traveling), and any entry fees.
   - Travel cost formula:
     \[
     \text{Travel Cost} = \text{Transportation Cost} + \text{Value of Travel Time}
     \]
   - Value of travel time is often approximated as a fraction (e.g., 1/3) of the wage rate.

4. **Estimate the Demand Function**
   - For ZTCM: Use the number of visits from each zone and corresponding travel costs to estimate a zonal demand curve.
   - For ITCM: Use individual travel cost data to estimate a personal demand function.
   - Common models include:
     - **Linear Regression**: Relate visit rates to travel costs and other variables.
     - **Poisson or Negative Binomial Regression**: For count data models when the dependent variable is the number of visits.

5. **Calculate Consumer Surplus**
   - Integrate the area under the demand curve to estimate the total consumer surplus, representing the total WTP.
   - Consumer surplus formula for a linear demand curve:
     \[
     \text{Consumer Surplus} = \int_{0}^{Q} \left( P(Q) - C \right) dQ
     \]
   - Where \( P(Q) \) is the price (travel cost) at quantity \( Q \), and \( C \) is the current cost (typically zero for entry-free sites).

### Example Calculation

Here is a detailed example using the Individual Travel Cost Method (ITCM):

```python
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Hypothetical survey data
data = pd.DataFrame({
    'visits': [5, 2, 4, 3, 2, 5, 3, 4, 1, 2],
    'travel_cost': [10, 20, 15, 25, 10, 20, 30, 15, 25, 30],
    'income': [50, 60, 55, 70, 45, 65, 75, 50, 55, 60]  # in thousands
})

# Create a constant term for the intercept
data['constant'] = 1

# Define the independent variables
X = data[['constant', 'travel_cost', 'income']]
y = data['visits']

# Fit the regression model (using Poisson regression for count data)
poisson_model = sm.GLM(y, X, family=sm.families.Poisson()).fit()

# Display model summary
print(poisson_model.summary())

# Predict visit rates based on the model
data['predicted_visits'] = poisson_model.predict(X)

# Plot the demand curve
plt.scatter(data['travel_cost'], data['visits'], label='Actual Visits')
plt.plot(data['travel_cost'], data['predicted_visits'], color='red', label='Predicted Visits')
plt.xlabel('Travel Cost')
plt.ylabel('Number of Visits')
plt.title('Demand Curve for Recreational Site')
plt.legend()
plt.show()

# Estimate Consumer Surplus (CS)
# Integrate the area under the demand curve
# Here, we approximate using a simple numerical integration method (trapezoidal rule)
def demand_curve(travel_cost, a, b, c):
    return a + b * travel_cost + c * (travel_cost**2)

# Parameters from the regression model
a = poisson_model.params['constant']
b = poisson_model.params['travel_cost']
c = poisson_model.params['income']

# Integrate from minimum to maximum travel cost
from scipy.integrate import quad

cs, _ = quad(lambda tc: demand_curve(tc, a, b, c), data['travel_cost'].min(), data['travel_cost'].max())
print(f"Estimated Consumer Surplus: ${cs:.2f}")
```

### Considerations

- **Substitute Sites**: Account for the availability of alternative sites which might affect visit rates.
- **Multi-purpose Trips**: Some trips may have multiple purposes, complicating the allocation of travel costs.
- **Seasonality**: Visits may vary by season, affecting the estimation of demand.
- **Income and Demographics**: Include socio-economic variables to capture differences in WTP.

### Advantages and Disadvantages

**Advantages:**
- Based on actual behavior, providing a realistic measure of WTP.
- Useful for estimating the value of recreational sites and ecosystem services.

**Disadvantages:**
- Requires extensive data collection through surveys.
- Assumes travel cost is the primary factor influencing visits, which may not always be true.
- Difficult to apply to non-use values (values not related to direct use or visits).

The TCM is a valuable tool in environmental economics for valuing natural resources and recreational sites, offering insights into the economic benefits of conservation and management efforts.


Yes, you can include household income as an explanatory variable in the Travel Cost Method (TCM) to better understand how income influences the willingness to pay (WTP) for accessing a biodiversity or recreational site. Including income helps capture differences in WTP among households with different economic circumstances.

Here's a detailed guide on how to include household income in calculating WTP using both the Individual Travel Cost Method (ITCM) and the Zonal Travel Cost Method (ZTCM).

### Individual Travel Cost Method (ITCM) with Household Income

1. **Data Collection:**
   - Collect survey data from visitors, including:
     - Number of visits to the site.
     - Travel costs incurred.
     - Household income.
     - Other relevant socio-economic variables (age, education, etc.).

2. **Data Preparation:**
   - Create a dataframe with the collected data.

3. **Regression Model:**
   - Use a regression model to estimate the relationship between the number of visits and travel costs, including household income as an explanatory variable.

4. **Consumer Surplus Calculation:**
   - Integrate the area under the estimated demand curve to calculate consumer surplus, which represents the total WTP.

Here is an example using Python and the `statsmodels` library:

```python
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Hypothetical survey data
data = pd.DataFrame({
    'visits': [5, 2, 4, 3, 2, 5, 3, 4, 1, 2],
    'travel_cost': [10, 20, 15, 25, 10, 20, 30, 15, 25, 30],
    'income': [50, 60, 55, 70, 45, 65, 75, 50, 55, 60]  # in thousands
})

# Create a constant term for the intercept
data['constant'] = 1

# Define the independent variables
X = data[['constant', 'travel_cost', 'income']]
y = data['visits']

# Fit the regression model (using Poisson regression for count data)
poisson_model = sm.GLM(y, X, family=sm.families.Poisson()).fit()

# Display model summary
print(poisson_model.summary())

# Predict visit rates based on the model
data['predicted_visits'] = poisson_model.predict(X)

# Plot the demand curve
plt.scatter(data['travel_cost'], data['visits'], label='Actual Visits')
plt.plot(data['travel_cost'], data['predicted_visits'], color='red', label='Predicted Visits')
plt.xlabel('Travel Cost')
plt.ylabel('Number of Visits')
plt.title('Demand Curve for Recreational Site')
plt.legend()
plt.show()

# Estimate Consumer Surplus (CS)
# Integrate the area under the demand curve
# Here, we approximate using a simple numerical integration method (trapezoidal rule)
def demand_curve(travel_cost, constant, travel_cost_coef, income_coef, income_level):
    return constant + travel_cost_coef * travel_cost + income_coef * income_level

# Parameters from the regression model
constant = poisson_model.params['constant']
travel_cost_coef = poisson_model.params['travel_cost']
income_coef = poisson_model.params['income']

# Average income level
average_income = data['income'].mean()

# Integrate from minimum to maximum travel cost
cs, _ = quad(lambda tc: demand_curve(tc, constant, travel_cost_coef, income_coef, average_income), data['travel_cost'].min(), data['travel_cost'].max())
print(f"Estimated Consumer Surplus: ${cs:.2f}")
```

### Zonal Travel Cost Method (ZTCM) with Household Income

1. **Data Collection:**
   - Collect data on the number of visits from different geographic zones, average travel costs, and average household incomes in those zones.

2. **Data Preparation:**
   - Create a dataframe with zonal data.

3. **Regression Model:**
   - Use a regression model to estimate the relationship between the number of visits from each zone and the travel costs, including average household income as an explanatory variable.

4. **Demand Function Estimation:**
   - Estimate the demand function and calculate consumer surplus.

Here is an example:

```python
import pandas as pd
import statsmodels.api as sm
from scipy.integrate import quad

# Hypothetical zonal data
data = pd.DataFrame({
    'zone': ['A', 'B', 'C', 'D', 'E'],
    'visits': [100, 150, 200, 80, 120],
    'travel_cost': [10, 20, 15, 25, 30],
    'income': [50, 55, 60, 65, 70]  # in thousands
})

# Create a constant term for the intercept
data['constant'] = 1

# Define the independent variables
X = data[['constant', 'travel_cost', 'income']]
y = data['visits']

# Fit the regression model (using OLS for zonal data)
ols_model = sm.OLS(y, X).fit()

# Display model summary
print(ols_model.summary())

# Estimate the demand function
def demand_curve(travel_cost, constant, travel_cost_coef, income_coef, income_level):
    return constant + travel_cost_coef * travel_cost + income_coef * income_level

# Parameters from the regression model
constant = ols_model.params['constant']
travel_cost_coef = ols_model.params['travel_cost']
income_coef = ols_model.params['income']

# Average income level
average_income = data['income'].mean()

# Integrate the demand curve to find consumer surplus
cs, _ = quad(lambda tc: demand_curve(tc, constant, travel_cost_coef, income_coef, average_income), data['travel_cost'].min(), data['travel_cost'].max())
print(f"Estimated Consumer Surplus: ${cs:.2f}")
```

### Considerations

- **Model Selection**: Choose an appropriate regression model based on the nature of your data (e.g., Poisson for count data, OLS for zonal data).
- **Income Interaction**: You may consider interaction terms between income and travel cost to capture non-linear effects.
- **Data Quality**: Ensure the accuracy and reliability of the collected data, as errors can significantly impact the results.

Including household income in the TCM helps provide a more nuanced estimate of WTP, reflecting the influence of economic factors on visitors' decisions.