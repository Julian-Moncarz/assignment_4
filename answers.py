import pandas as pd
import numpy as np

# Employees DataFrame
employee_ids = list(range(1, 101))
names = ["Employee_" + str(i) for i in employee_ids]
department_names = np.random.choice(['HR', 'Development', 'Research', 'Marketing'], 100)
salaries = np.random.randint(50000, 120000, 100)

employees_data = {
    'employee_id': employee_ids,
    'name': names,
    'department_name': department_names,
    'salary ($)': salaries
}

df_employees = pd.DataFrame(employees_data)

# Departments DataFrame
department_ids = list(range(1, 5))
department_names = ['HR', 'Development', 'Research', 'Marketing']
managers = ["Manager_" + str(i) for i in department_ids]

departments_data = {
    'department_id': department_ids,
    'department_name': department_names,
    'manager': managers
}

df_departments = pd.DataFrame(departments_data)

# Projects DataFrame
project_codes = ["P" + str(i).zfill(3) for i in range(1, 21)]
project_departments = np.random.choice(department_names, 20)
budgets = np.random.randint(10000, 50000, 20)

projects_data = {
    'project_code': project_codes,
    'department_name': project_departments,
    'budget ($)': budgets
}

df_projects = pd.DataFrame(projects_data)


# Display the first 5 rows of the df_employees DataFrame.
print(df_employees.head(5))

# How many employees are there in each department?
employees_per_department = df_employees['department_name'].value_counts()
print("Number of employees per department")
print(employees_per_department)

# What is the average salary in the company?
mean_salary = df_employees['salary ($)'].mean()
print('The mean salary is', mean_salary)

# List all employees with salaries above $100,000.
big_salary_employees = df_employees[df_employees['salary ($)'] > 100000]
print("Employees making > 100,000 $:")
print(big_salary_employees)

# Who is the manager of the 'Development' department?
development_manager = df_departments[df_departments['department_name'] == 'Development']['manager'])
print("The manager of the Development department is:")
print(development_manager)

# Merge df_employees with df_departments to include the manager's name for each employee.
merged_df = pd.merge(df_employees, df_departments, on = 'department_name', how = 'left')
print("Merged df:")
print(merged_df.head())

# Which department has the highest average salary?
average_department_salaries = df_employees.groupby('department_name')['salary ($)'].mean().sort_values(ascending=False))
print("Average salaries by department:")
print(averag_department_salaries)

# Create a new column in df_employees that categorizes salaries into 'Low', 'Medium', and 'High' (define the ranges yourself).
bins = [0, 40000, 80000, float('inf')] # This is really cool. 
# pd.cut takes a bin (between 2 values) and label and a column. It returns the label if the value in the column is in the bin!!
labels = ['low', 'medium', 'high']

df_employees['salary catagory'] = pd.cut(df_employees['salary ($)'], bins = bins, labels = labels)
print(df_employees.head())

# Find the total budget of projects for the 'Research' department.
research_project_budget = df_projects[df_projects['department_name'] == 'Reseach'].sum()
print("The total budget of reseach projects is", research_project_budget)

# How many projects does each department have?
projects_per_department = df_projects['department_name'].value_counts()
print("Projects per department")
print(projects_per_department)

# What is the total number of employees working on projects (assuming each project has an equal number of employees from the relevant department)?
# Assuming 10 employees per project
people_on_projects = 10 * df_projects['departmen_name'].count()
print('Number of employees working on projects')
print(people_on_projects)

# Find the employee with the highest salary in the 'Marketing' department. 
# Using nlargest(number, catagory)!
highest_earner_marketing = df_employees[df_employees['department_name'] == 'Marketing'].nlargest(1, 'salary ($)')
print('the highest earner in the marketing department is:')
print(highest_earner_marketing)

# Sort the df_projects DataFrame by budget in descending order and display the top 3 most expensive projects.
df_projects.sort_values(by = 'budget ($)', ascending = False, inplace = True)
print('Projects in descending order by budget')
print(df_projects.head(3))

# Merge df_projects with df_departments on department_name and display the result.
merged_df_2 = pd.merge(df_projects, df_departments, on = 'department_name', how = 'left')
print('projects and departments merged on department_name')
print(merged_df_2)

# For each department, find the project with the largest budget and list its code and budget amount.
biggest_project_each_department = df_projects.groupby('department_name').nlargest(1, 'budget ($)')
print('Project with largest budget for each department')
print(biggest_project_each_department)

# Calculate the average budget per employee in each department.


# Find the total salary expense for each department where the department manager's name starts with 'Manager_1'.
# Determine the total and average salary of employees for each project, considering only projects with budgets over $30,000.
# For each manager, find out the total number of employees and the average budget of the projects in their department.
# Create a summary table that shows, for each department, the number of projects and the average salary of employees who earn more than the average salary in their department.
