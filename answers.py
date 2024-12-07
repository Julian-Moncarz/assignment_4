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

# QUESTIONS


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
development_manager = df_departments[df_departments['department_name'] == 'Development']['manager']
print("The manager of the Development department is:")
print(development_manager)

# Merge df_employees with df_departments.
df_employees_departments = pd.merge(df_employees, df_departments, on = 'department_name', how = 'left')
print("Employees and departments merged on department name df:")
print(df_employees_departments.head())

# Which department has the highest average salary?
average_department_salaries = df_employees.groupby('department_name')['salary ($)'].mean().sort_values(ascending=False)
print("Average salaries by department:")
print(average_department_salaries)

# Create a new df_employees column that say if a salary's Low, Medium or High.
bins = [0, 40000, 80000, float('inf')]
labels = ['low', 'medium', 'high']
# pd.cut takes a bin (between 2 values) and label and a column. 
# It returns the label if the value in the column is in the bin!!

df_employees['salary catagory'] = pd.cut(df_employees['salary ($)'], bins = bins, labels = labels)
print(df_employees.head())

# Find the total budget of projects for the 'Research' department.
research_project_budget = df_projects[df_projects['department_name'] == 'Reseach'].sum()
print("The total budget of reseach projects is", research_project_budget)

# How many projects does each department have?
projects_per_department = df_projects['department_name'].value_counts()
print("Projects per department")
print(projects_per_department)

# What is the total number of employees working on projects 
# Assuming each project has 10 employees
people_on_projects = 10 * df_projects['department_name'].count()
print('Number of employees working on projects')
print(people_on_projects)

# Find the employee with the highest salary in the 'Marketing' department. 
# Using nlargest(number, catagory)!
highest_earner_marketing = df_employees[df_employees['department_name'] == 'Marketing']['salary ($)'].max()
print('the highest earner in the marketing department is:')
print(highest_earner_marketing)

# Sort the df_projects DataFrame by budget in descending order and display the top 3 most expensive projects.
df_projects.sort_values(by = 'budget ($)', ascending = False, inplace = True)
print('Projects in descending order by budget')
print(df_projects.head(3))

# Merge df_projects with df_departments on department_name and display the result.
df_projects_departments = pd.merge(df_projects, df_departments, on = 'department_name', how = 'left')
print('projects and departments merged on department_name')
print(df_projects_departments)

# For each department, find the project with the largest budget and list its code and budget amount.
biggest_project_each_department = df_projects.groupby('department_name')['budget ($)'].max()
print('Project with largest budget for each department')
print(biggest_project_each_department)

# Calculate the average budget per employee in each department.
# Budget = sum the budget of all the projects in that department and divide it by the num of employees in the department.
avrg_budget_per_employee_per_depo = df_projects.groupby('department_name')['budget ($)'].sum() / df_employees['department_name'].value_counts()

print("Average budget per employee per department")
print(avrg_budget_per_employee_per_depo)

# Find the total salary expense for each department where the department manager's name starts with 'Manager_1'.
# Use the first merged df. It has the manager name for each employee
man1_total_sals = df_employees_departments[df_employees_departments['manager'] == 'Manager_1']['salary ($)'].sum()
print("Total salary of Manager_1's employees")
print(man1_total_sals)

# Determine the total and average salary of employees for each project, considering only projects with budgets over $30,000.
# Assuming 10 employees per project, each paid average for their department.
# This means the total salary for the project will be 10x the avarage salary.
# The average salary will be the average salary for the department.
projects_salary_info = pd.merge(df_projects[df_projects['budget ($)'] > 30000], df_employees.groupby('department_name')['salary ($)'].mean(), on = 'department_name', how = 'left')
projects_salary_info['total salary ($)'] = projects_salary_info['salary ($)'] * 10
print('Project salary info')
print(projects_salary_info)

# For each manager, find out the total number of employees and the average budget of the projects in their department.
employees_per_depo_man = pd.merge(employees_per_department, df_departments, on = 'department_name', how = 'left')
manager_stats = pd.merge(employees_per_depo_man, df_projects.groupby('department_name')['budget ($)'].mean(), on = 'department_name', how = 'right')
print('Manager employee counts and total project budget')
print(manager_stats.drop(['department_name', 'department_id'], axis = 1))

# Create a summary table that shows, for each department, the number of projects and the average salary of employees who earn more than the average salary in their department.

