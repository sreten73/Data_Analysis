import pandas as pd

# 1. Read data from the csv file
df = pd.read_csv('adult_data.csv')
print(df.head)

# How many of each race are represented in this dataset?
race_counts = df['race'].value_counts()
print(race_counts)

# What is the average age of men?
age_average = df['age'].mean()
print(f'Average age of men is {age_average}')

print('\n',df.columns)
print(df['education'].count())
print(df['education'].value_counts()['Bachelors'])

percentage_bachelors = (df['education'].value_counts()['Bachelors'])*100/(df['education'].count())
percentage_bachelors1 = (df['education'].value_counts()['Bachelors'])*100/len(df['education'])
print(percentage_bachelors,'%')
print(percentage_bachelors1,'%')

#bacherlors = len(df[(df['salary'] == '>50K')&(df['education']=='Bachelors')])
#masters = len(df[(df['salary'] == '>50K')&(df['education']=='Masters')])
#doctorate = len(df[(df['salary'] == '>50K')&(df['education']=='Doctorate')])
higher_education = len(df[(df['salary'] == '>50K')&((df['education']=='Bachelors')|(df['education']=='Masters')|(df['education']=='Doctorate'))])
lower_education = len(df[(df['salary'] == '>50K')&(df['education']!='Bachelors')&(df['education']!='Masters')&(df['education']!='Doctorate')])
#print(bacherlors,masters,doctorate)
#higher_education = bacherlors + masters + doctorate
print(higher_education, lower_education)
higher_education_rich = (higher_education*100)/len(df['education'])
lower_education_rich = (lower_education*100)/len(df['education'])
print(higher_education_rich,'%')
print(lower_education_rich,'%')

min_hours_per_week = df['hours-per-week'].min()
print(min_hours_per_week)

num_min_workers = len(df[(df['salary'] == '>50K')&(df['hours-per-week']==min_hours_per_week)])
rich_percentage = (num_min_workers*100)/len(df['hours-per-week'])
print(num_min_workers,rich_percentage,'%')

highest_earning_country = df[(df['salary'] == '>50K')]['native-country'].value_counts().idxmax()
print(highest_earning_country)
highest_earning_country_percentage = (df[(df['salary'] == '>50K')]['native-country'].value_counts().max()*100)/len(df['salary'])
print(highest_earning_country_percentage,'%')

df_india_high_salary = df[(df['salary'] == '>50K') & (df['native-country'] == 'India')]
print(df_india_high_salary)
top_IN_occupation = df_india_high_salary['occupation'].value_counts().index[0]
print(top_IN_occupation)
print(df_india_high_salary['occupation'].value_counts())