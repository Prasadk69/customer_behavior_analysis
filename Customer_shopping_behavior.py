from gettext import install

import pandas as pd
from numpy.ma.extras import median
from pandas.core.common import fill_missing_names

df = pd.read_csv(r'C:\Users\Prasad\PycharmProjects\PythonProject\customer_shopping_behavior.csv')
print(df.head())
print(df.info())
print(df.describe(include='all'))
print(df.isnull().sum())
df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))
print(df.isnull().sum())
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ','_')
df = df.rename(columns={'purchase_amount_(usd)':'purchase_amount'})
print(df.columns)
age_group = [ 'teen', 'adult', 'middle aged', 'senior' ]
df['age_group'] = pd.qcut(df['age'], q = 4, labels = age_group)
print(df[['age','age_group']].head(10))
period_of_purchases= {
    'Fortnightly' : 14,
    'Weekly' : 7,
    'Monthly' : 30,
    'Quarterly' : 90,
    'Bi-Weekly' : 14,
    'Annually' : 365,
    'Every 3 Months' : 90
}
df['period'] = df['frequency_of_purchases'].map(period_of_purchases)
print(df[['frequency_of_purchases','period']])
print(df[['discount_applied','promo_code_used']].head(10))
print((df['discount_applied'] == df['promo_code_used']).all())
del df['promo_code_used']
print(df.head())
print(df.columns)
import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL Connection

username = "postgres"
password = "prxsql12345"
host = "localhost"
port = "5432"
database = "customer_behavior"
engine = create_engine(f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}")

# Insert into PostgreSQL

table_name = "customer"
df.to_sql(table_name, engine, if_exists="replace", index=False)
print(f"Data successfully loaded into table '{table_name}' in database '{database}'.")