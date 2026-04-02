# 2. Advanced Aggregation (The "Group & Agg" Problem)
# Problem: Calculate the total salary and the count of employees per department.
employees = [
    {"dept": "Tech", "name": "Das", "salary": 5000},
    {"dept": "Tech", "name": "Ram", "salary": 7000},
    {"dept": "HR", "name": "Alice", "salary": 4500},
    {"dept": "Tech", "name": "Bob", "salary": 6000},
    {"dept": "HR", "name": "Eve", "salary": 4800}
]
df_emp = pd.DataFrame(employees)

# CHALLENGE: Create a summary table showing 'Total Salary' and 'Staff Count' by dept.
# Hint: df_emp.groupby('dept').agg({'salary': ['sum', 'count']})

'''Output:
total_salary:      salary      
        sum count
dept             
HR     9300     2
Tech  18000     3
'''