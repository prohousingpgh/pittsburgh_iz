import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf

# Create the dataset for DID analysis
data1 = pd.DataFrame({
    'Neighborhood': ['Lawrenceville', 'Lawrenceville', 'South Side Flats', 'South Side Flats',
                     'Strip District', 'Strip District'],
    'Period': ['Pre', 'Post', 'Pre', 'Post', 'Pre', 'Post'],
    'Units': [692, 378, 612, 574, 805, 879],
    'Projects': [6, 2, 6, 3, 5, 7],
    'Treatment': [1, 1, 0, 0, 0, 0],
    'Post': [0, 1, 0, 1, 0, 1]
})

# Create interaction term for the DID
data1['Treatment_Post'] = data1['Treatment'] * data1['Post']

# Run the DID regression using Units as the outcome variable
model_units = smf.ols('Units ~ Treatment + Post + Treatment_Post', data=data1).fit()

# Run the DID regression using Projects as the outcome variable
model_projects = smf.ols('Projects ~ Treatment + Post + Treatment_Post', data=data1).fit()

# Extract the summary results
units_summary = model_units.summary()
projects_summary = model_projects.summary()

print(units_summary, projects_summary)
