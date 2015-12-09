'''
Created on December 6, 2015
The grade_calculator examines the last two grades in a inspection. Thus, the time between an
inpsection determins if a restaurant is quality is increasing or descreasing.
@author: Taurean Parker
'''
import pandas as pd
import numpy as np
import itertools

def test_grades(grade_list):
    'Take a list of grades and return 1 if grades are improving , -1 if declining, 0 if no change'
    grade = {3:"A", 2:"B", 1:"C" }
    grade_num= {v:k for k,v in grade.iteritems()}
    grade_list=grade_list[-2:]
    grade_trans=[grade_num.get(item,item) for item in grade_list]
    grade_trans = [list(z) for z in itertools.izip(grade_trans,grade_trans[1:])]
    grade_trans = [1 if x[1]>x[0] else -1 if x[1]<x[0] else 0 for x in grade_trans]
    grade_trans=[item for grade in grade_trans for item in grade_trans]
    return grade_trans 

    
def test_restaurant_grades(dataframe,camis_id):
    'Take a list of restaurant data inspections and determine if grades are increasing, decreasing or stayed the same '
    df=dataframe
    df=df.sort(['camis','grade_date'])
    df=df[df.camis == camis_id]
    df=df['grade']
    df=test_grades(df)
    return df   
    

    
   
        
    
    
    

