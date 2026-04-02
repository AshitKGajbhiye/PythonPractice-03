# 1. Handling Mixed Nested Data (The "Explode" Problem)
import pandas as pd

# Problem: Some users have a list of 'projects' in a single field.
data = [
    {"user": "Das", "projects": ["Alpha", "Beta"]},
    {"user": "Raqib", "projects": ["Gamma"]},
    {"user": "Ram", "projects": []}
]
df = pd.DataFrame(data)

# CHALLENGE: Create a DataFrame where each project has its own row.
# Hint: Use df.explode('projects')
print(df.explode('projects'))


'''
    user projects
0    Das    Alpha
0    Das     Beta
1  Raqib    Gamma
2    Ram      NaN

'''