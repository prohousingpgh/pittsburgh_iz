import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf

# Create the dataset for DID analysis
data_completed = pd.DataFrame({
    'Neighborhood': ['Lawrenceville', 'Lawrenceville', 'South Side Flats', 'South Side Flats',
                     'Strip District', 'Strip District'],
    'Period': ['Pre', 'Post', 'Pre', 'Post', 'Pre', 'Post'],
    'Units': [677, 378, 612, 574, 805, 880],
    'Projects': [9, 2, 6, 3, 5, 7],
    'Treatment': [1, 1, 0, 0, 0, 0],
    'Post': [0, 1, 0, 1, 0, 1]
})

# Create the dataset for DID analysis
data_permitted = pd.DataFrame({
    'Neighborhood': ['Lawrenceville', 'Lawrenceville', 'South Side Flats', 'South Side Flats',
                     'Strip District', 'Strip District'],
    'Period': ['Pre', 'Post', 'Pre', 'Post', 'Pre', 'Post'],
    'Units': [677, 1172, 612, 1212, 805, 3012],
    'Projects': [9, 7, 6, 6, 5, 18],
    'Treatment': [1, 1, 0, 0, 0, 0],
    'Post': [0, 1, 0, 1, 0, 1]
})

# Create interaction term for the DID
data_completed['Treatment_Post'] = data_completed['Treatment'] * data_completed['Post']
data_permitted['Treatment_Post'] = data_permitted['Treatment'] * data_permitted['Post']
# Run the DID regression using Units as the outcome variable
model_units = smf.ols('Units ~ Treatment + Post + Treatment_Post', data=data_completed).fit()
model_units_permitted = smf.ols('Units ~ Treatment + Post + Treatment_Post', data=data_permitted).fit()

# Run the DID regression using Projects as the outcome variable
model_projects = smf.ols('Projects ~ Treatment + Post + Treatment_Post', data=data_completed).fit()
model_projects_permitted = smf.ols('Projects ~ Treatment + Post + Treatment_Post', data=data_permitted).fit()

# Extract the summary results
units_summary = model_units.summary()
projects_summary = model_projects.summary()
units_summary_permitted = model_units_permitted.summary()
projects_summary_permitted = model_projects_permitted.summary()

print(units_summary, projects_summary)
print(units_summary_permitted, projects_summary_permitted)
