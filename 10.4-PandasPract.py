# 3. Cleaning & Mapping Data (The "Cleanup" Problem)

# Problem: Clean 'status' to be only 'Active' or 'Inactive'.
# Values like 'active ', 'ACTIVE', and None should be fixed.
import pandas as pd

raw_data = {
    'name': ['A', 'B', 'C', 'D'],
    'status': ['active ', 'ACTIVE', None, 'inactive']
}
df_clean = pd.DataFrame(raw_data)

# 1. Strip trailing spaces
# 2. Capitalize (e.g., 'ACTIVE' -> 'Active')
# 3. Fill None/NaN values with 'Unknown'
df_clean['status'] = (
    df_clean['status']
    .str.strip()
    .str.capitalize()
    .fillna('Unknown')
)

print(df_clean)
