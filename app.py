import pandas

filepath = 'data\\VIB_ATSH.csv'
df = pandas.read_csv(filepath)

df['GD_THOA_DK'] = df['GD_THOA_DK'].apply(lambda x: x.replace("x", "9").replace("X", "9").replace(",", ""))
df['GD_THOA_DK'] = df['GD_THOA_DK'].fillna(0)
df['GD_THOA_DK'] = pandas.to_numeric(df['GD_THOA_DK'], errors='coerce')
df['LAST_NAME'] = df['CLIENT_NAME'].apply(lambda x: x.split(' ')[-1])

total_member = len(df)
total_amount = df['GD_THOA_DK'].sum()
avg_amount = df['GD_THOA_DK'].mean()
rewards = df['TICKET_TYPE'].value_counts()
last_names = df['LAST_NAME'].value_counts()

print(f"{total_member:,}")
print(f"{total_amount:,}")
print(f"{avg_amount:,}")
for reward_type, count in rewards.items():
    print(f"{reward_type}: {count:,}")
for last_name, count in last_names.items():
    print(f"{last_name}: {count:,}")
    
df = df[df['GD_THOA_DK'] > 0]

total_member = len(df)
total_amount = df['GD_THOA_DK'].sum()
avg_amount = df['GD_THOA_DK'].mean()
rewards = df['TICKET_TYPE'].value_counts()
last_names = df['LAST_NAME'].value_counts()

print(f"{total_member:,}")
print(f"{total_amount:,}")
print(f"{avg_amount:,}")
for reward_type, count in rewards.items():
    print(f"{reward_type}: {count:,}")
for last_name, count in last_names.items():
    print(f"{last_name}: {count:,}")
    

print("===============================")
total_transactions = df.groupby('LAST_NAME')['GD_THOA_DK'].sum().reset_index()
total_transactions.columns = ['LAST_NAME', 'TOTAL_GD_THOA_DK']
total_transactions = total_transactions.sort_values(by='TOTAL_GD_THOA_DK', ascending=False)

for index, row in total_transactions.iterrows():
    print(f"{row['LAST_NAME']}: {row['TOTAL_GD_THOA_DK']:,}")

print("DONE")