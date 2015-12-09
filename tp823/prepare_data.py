'''
Created on December 6, 2015
@author: Taurean Parker
'''
import pandas as pd

def load_data(file):
    'Load CSV file into a DataFrame'
    try:
        dataframe=pd.read_csv(file, low_memory= False) 
        return dataframe
        
    except IOError:
            print 'Unable to find the file'
            
def clean_column_names(dataframe):
    "Removes trailing whitespace, convert columns to lowecase, and replace spaces with _"
    df=dataframe
    df.columns = [x.strip() for x in df.columns] # Remove trailing whitespace
    df.columns = [x.lower() for x in df.columns] # Convert column name to lowecase
    df.columns = [x.replace(' ', '_') for x in df.columns] #replace " " with "_"
       

def remove_missing_values(dataframe):
    df=dataframe
    df=df.dropna(subset=['camis', 'grade', 'grade_date'], how='any', axis=0)
    return df
    
def subset_valid_grades(dataframe):
    'Removes Invalid Grades from the DataFrame'
    valid_grades=['A', 'B', 'C']
    df=dataframe
    df=df.loc[df['grade'].isin(valid_grades)]
    return df


def get_clean_data(file):
    data=load_data(file)
    clean_column_names(data)
    clean_df=remove_missing_values(data)
    clean_df=subset_valid_grades(clean_df)
    clean_df = clean_df[clean_df.boro != 'Missing'] #Remove Invalid Borough
    return clean_df
    
    
    

#Data=load_data('nyc_restaurant_inspection_results.csv')
#rename_columns=clean_column_names(Data)
#Data=Data[Data.grade.notnull()]
#Data=Data[Data.grade_date.notnull()]
#Data=Data[Data.grade.notnull()]
#Data=Data.dropna(subset=['camis', 'grade', 'grade_date'], how='any', axis=0)
#print Data

b=get_clean_data('nyc_restaurant_inspection_results.csv')


