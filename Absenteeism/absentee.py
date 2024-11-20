#%%
import pandas as pd
import pandas as pd2
#%%
raw_csv_data = pd.read_csv(r'C:\Users\alexb\PycharmProjects\DataScience-SQL-Tableau\data\Absenteeism_data.csv')
#%%
raw_csv_data
#%%
df = raw_csv_data.copy()
df.info()
#%%
df = df.drop(['ID'], axis = 1)
#dropped
#%%
df
#%%
df["Reason for Absence"]
#%%
df["Reason for Absence"].min()
#%%
df["Reason for Absence"].max()
#%%
pd.unique((df['Reason for Absence']))

#%%
sorted(df['Reason for Absence'].unique())
#%%
reason_columns = pd.get_dummies(df['Reason for Absence'])
#%%
reason_columns
#%%
reason_columns['check'] = reason_columns.sum(axis = 1)
reason_columns
#%%
reason_columns['check'].sum(axis = 0)
#%%
reason_columns = reason_columns.drop(['check'], axis = 1)
reason_columns
#%%
reason_columns = pd.get_dummies(df['Reason for Absence'],drop_first = True)
reason_columns
#%%
df = df.drop(['Reason for Absence'], axis = 1)
#%%
df
#%%
reason_type_1 = reason_columns.loc[:, '1':'14'].max(axis = 1)
reason_type_2 = reason_columns.loc[:, '15':'17'].max(axis = 1)
reason_type_3 = reason_columns.loc[:, '18':'21'].max(axis = 1)
reason_type_4 = reason_columns.loc[:, '22':].max(axis = 1)
#%%
reason_type_2
#%%
df = pd.concat([df, reason_type_1, reason_type_2, reason_type_3, reason_type_4], axis = 1)
df
#%%
df.columns.values
#%%
column_names = ['Date', 'Transportation Expense', 'Distance to Work', 'Age',
       'Daily Work Load Average', 'Body Mass Index', 'Education',
       'Children', 'Pets', 'Absenteeism Time in Hours', 'Reason_1', 'Reason_2', 'Reason_3', 'Reason_4']
#%%
df.columns = column_names
#%%
df.head()
#%%
column_names_reordered = ['Reason_1', 'Reason_2', 'Reason_3', 'Reason_4', 'Date', 'Transportation Expense', 'Distance to Work', 'Age', 'Daily Work Load Average', 'Body Mass Index', 'Education', 'Children', 'Pets', 'Absenteeism Time in Hours']
#%%
df = df[column_names_reordered]
#%%
df.head()
#%%
df_reason_mod = df.copy()
df_reason_mod
#%%
age_dummies = pd.get_dummies(df['Age'])
age_dummies['check'] = age_dummies.sum(axis = 1)
age_dummies
#%%
df_concatenated = pd.concat([df, age_dummies], axis = 1)
df_concatenated
#%%
df_concatenated.columns.values
#%%
concat_column_names_reor = ['Reason_1', 'Reason_2', 'Reason_3', 'Reason_4', 'Date',
       'Transportation Expense', 'Distance to Work', 'Age',
       'Daily Work Load Average', 'Body Mass Index', 'Education',
       'Children', 'Pets', 27, 28, 29, 30,
       31, 32, 33, 34, 36, 37, 38, 39, 40, 41, 43, 46, 47, 48, 49, 50, 58,
       'check', 'Absenteeism Time in Hours']
#%%
df_concatenated = df_concatenated[concat_column_names_reor]
df_concatenated
#%%
df_concatenated_checkpoint_1 = df_concatenated.copy()
#%%
type(df_reason_mod['Date'][0])
#%%
df_reason_mod['Date'] = pd.to_datetime(df_reason_mod['Date'], format='%d/%m/%Y')
#%%
df_reason_mod['Date']
#%%
df_reason_mod['Date'][0].month
#%%
list_months = []
#%%
df_reason_mod.shape
#%%
for i in range(700):
    list_months.append(df_reason_mod['Date'][i].month)
#%%
len(list_months)
#%%
df_reason_mod['Month'] = list_months
#%%
df_reason_mod.head(20)
#%%
df_reason_mod['Date'][699].weekday()
#%%
def date_to_weekday(date):
    return date.weekday()
#%%
df_reason_mod['Day of the Week'] =  df_reason_mod['Date'].apply(date_to_weekday)
#%%
df_reason_mod.head()
#%%
df_reason_mod = df_reason_mod.drop(["Date"], axis = 1)
#%%
df_reason_mod.head()
#%%
df_reason_mod.columns.values
#%%
df_reason_mod_reorder =  ['Reason_1', 'Reason_2', 'Reason_3', 'Reason_4', 'Month',
       'Day of the Week',
       'Transportation Expense', 'Distance to Work', 'Age',
       'Daily Work Load Average', 'Body Mass Index', 'Education',
       'Children', 'Pets', 'Absenteeism Time in Hours']
#%%
df_reason_mod = df_reason_mod[df_reason_mod_reorder]
#%%
df_reason_mod
#%%
df_reason_date_mod_checkpoint = df_reason_mod.copy()
#%%
df_reason_date_mod_checkpoint.head()
#%%
df_reason_date_mod_checkpoint["Education"].unique()
#%%
df_reason_date_mod_checkpoint["Education"].value_counts()
#%%
df_reason_date_mod_checkpoint['Education'] = df_reason_date_mod_checkpoint['Education'].map({1:0, 2:1, 3:1, 4:1})
#%%
df_reason_date_mod_checkpoint['Education'].value_counts()
#%%
df_reason_date_mod_checkpoint
#%%
df_preprocessed = df_reason_date_mod_checkpoint.copy()
#%%
df_preprocessed.to_csv(r'C:\Users\alexb\PycharmProjects\DataScience-SQL-Tableau\data\Absenteeism_Preprocessed.csv', index = False)