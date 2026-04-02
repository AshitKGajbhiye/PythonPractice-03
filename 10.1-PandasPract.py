import pandas as pd
users = [
{"id": 1, "name": "Das", "social_profile": {"twitter": "@das_tech", "facebook": "fb/das"}},
{"id": 2, "name": "Raqib", "social_profile": {"twitter": "@raqib", "facebook": None}}, 
{"id": 3, "name": "Mukesh", "social_profile": {"twitter": "", "facebook": "fb/mukesh"}},
{"id": 4, "name": "Ramesh", "social_profile": {}},
{"id": 5, "name": "Ram", "social_profile": {"twitter": "@ram_dev", "facebook": "fb/ram"}}
]

df = pd.DataFrame(users)
print(f"Head \n: {df.head(2)}")
print(f"Tail \n {df.tail(2)}")

profiles = pd.json_normalize(df["social_profile"])
# print(f"Normalize: {pd.json_normalize(df["social_profile"])}")
# Extracts the keys from the nested dictionaries into standalone columns (twitter, facebook).
mask = (profiles['twitter'].notna() & (profiles['twitter'] != "") & profiles['facebook'].notna() & (profiles['facebook'] != ""))

# Apply the mask and convert back to a list of dictionaries
output_users = df[mask].to_dict(orient='records')
print(f"output_users, {output_users}")

'''
Head 
:    id   name                                  social_profile
0   1    Das  {'twitter': '@das_tech', 'facebook': 'fb/das'}
1   2  Raqib         {'twitter': '@raqib', 'facebook': None}
Tail 
    id    name                                 social_profile
3   4  Ramesh                                             {}
4   5     Ram  {'twitter': '@ram_dev', 'facebook': 'fb/ram'}
output_users, [{'id': 1, 'name': 'Das', 'social_profile': {'twitter': '@das_tech', 'facebook': 'fb/das'}}, {'id': 5, 'name': 'Ram', 'social_profile': {'twitter': '@ram_dev', 'facebook': 'fb/ram'}}]
'''