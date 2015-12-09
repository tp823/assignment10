'''
Created on December 6, 2015
@author: Taurean Parker
'''
import sys
import matplotlib.pyplot as plt
from grade_calculator import *
from prepare_data import *
import numpy as np


def generate_plots_borough(data,boro):
   df=data
   df=df[df.boro == boro]
   df=df.groupby(["grade_date", "grade"]).grade.count().unstack("grade")
   df.plot(figsize=(5,8), title= 'Grade Improvement'+str(boro))
   plt.savefig('grade_improvement_'+str(boro)+'.pdf')

def generate_plots_overall(data):
   df=data
   df=df.groupby(["grade_date", "grade"]).grade.count().unstack("grade")
   df.plot(figsize=(5,8))
   plt.savefig('grade_improvement_nyc.pdf')
   
def sum_restaurant_grade(data,boro):  
    df=df[df.boro == boro]
    grades=[test_restaurant_grades(df,i) for restaurant in list(df['camis'].unique())]
    
   
   
if __name__ == "__main__":
    while True:
            try:
                data=get_clean_data('nyc_restaurant_inspection_results.csv')
                
                #Generate plots for borough
                boro_list=list(data['boro'].unique()) # list of valid boros
                plots= [generate_plots_borough(data,boro) for boro in boro_list]
                plot_all_boroughs= generate_plots_overall(data)
                
                # Calculaur Grades
                grades_citywide=np.sum([test_restaurant_grades(data,i) for i in list(data['camis'].unique())])
                grades_borough= np.sum([sum_restaurant_grade(data,boro) for boro in boro_list])
                print grades_borough
                print grades_citywide


            except KeyboardInterrupt:
                print 'Keyboard Interrupt'
                
            break
            
            
        
    
    
    
