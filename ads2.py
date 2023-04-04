import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#function for reading csv files
def readfile(df_name,file_name):
    df_name=pd.read_csv(file_name)
    df_name.index=df_name['Country Name']
    
    df_name_new=df_name.loc[["China","India","Australia","Spain",
                "United States","Germany","South Africa","Finland","Brazil"],
                                ['1990','1995','2000','2005','2010','2014']]

    return df_name_new

# #reading the data-world-bank csv files using above function 
ele_per_cap=readfile('ele_per_cap','electricity_per_capita.csv')
print(ele_per_cap)
# forest_sq_km=readfile('forest_sq_km','forest_sq.csv')
# total_pop=readfile('world_pop','total_pop.csv')
# n_oxide=readfile('n_oxide','n_oxide.csv')
# greenhouse_emission=readfile('greenhouse_emission','greenhouse.csv')
# urbanpopulation=readfile('urban_population','urbanpopulation.csv')

# #a function for creating bar-graphs 
# def bar_plot(df_name,title_name):
#     plt.figure(figsize=(8,6))
#     ax=plt.subplot()
#     years=df_name.columns
#     print(years)
#     bar_width=0.9/len(years)
#     x_ticks=df_name.index
#     for i,year in enumerate(years):
#         ax.bar([j+bar_width/2+bar_width*i for j in range(len(x_ticks))],
#                df_name[year],
#                 width=bar_width,label=year)
        
#     ax.set_xlabel('Country Name')
#     #ax.set_ylabel(ele_per_cap_new)
#     #ax.set_title(df_name[1])

#     ax.set_xticks([j+0.4 for j in range(len(x_ticks))])
#     ax.set_xticklabels(x_ticks,rotation=45)
#     ax.legend()
#     plt.title(title_name)
#     plt.show()
    
# bar_plot(total_pop,'Total Country Population')
# bar_plot(forest_sq_km,'Forest Area in Sq Km for Each Country')
# bar_plot(ele_per_cap,'Electric power consumption (kWh per capita)')
# bar_plot(greenhouse_emission,'Total greenhouse gas emissions (kt of CO2 \
#          equivalent)')
# bar_plot(n_oxide,'Nitrous oxide emissions (thousand metric tons of CO2\
#          equivalent)')
# bar_plot(urbanpopulation,'World Wide Urban Population ')


# # function  for correlation between columns of new dataframe 
# def correlation(df_name,country_name):
#     '''
    

#     Parameters
#     ----------
#     df_name : pandas.DataFrame
#         DESCRIPTION.
#     country_name : TYPE
#         DESCRIPTION.

#     Returns
#     -------
#     df_name : TYPE
#         DESCRIPTION.

#     '''
#     df_name=pd.DataFrame()
#     df_name['world_pop']=total_pop.loc[country_name,:]
#     df_name['electricity_per_capita']=ele_per_cap.loc[country_name,:]
#     df_name['forest_sq']=forest_sq_km.loc[country_name,:]
#     df_name['n_oxide']=n_oxide.loc[country_name,:]
#     df_name['greenhouse_emission']=greenhouse_emission.loc[country_name,:]
#     df_name['urbanpopulation']=urbanpopulation.loc[country_name,:]
    
#     corr=df_name.corr().to_numpy()
    
#     #corr=corr.style.background_gradient(cmap ='grey')
#     plt.figure(figsize=(6,6))
#     plt.imshow(df_name.corr(),cmap='coolwarm',interpolation='nearest')
      
#     # Displaying a color bar to understand
#     # which color represents which range of data
#     plt.colorbar()
      
#     # Assigning labels of x-axis 
#     # according to dataframe
#     plt.xticks(range(len(df_name)), df_name.columns,rotation=90)
#     # Assigning labels of y-axis 
#     # according to dataframe
#     plt.yticks(range(len(df_name)), df_name.columns)
#     for i in range(len(df_name.columns)):
#         for j in range(len(df_name.columns)):
#              plt.text(j, i, corr[i, j].round(2),
#                             ha="center", va="center", color="w")
#     # Displaying the figure
#     plt.show()
#     return df_name
    
# USA=correlation('USA','United States')
# India=correlation('India','India')
# Spain=correlation('Spain','Spain')
# Germany=correlation('Germany','Germany')
# Finland=correlation('Finland','Finland')
# print(USA,India,Finland,Germany,Spain)

# #line plots
# tubercolusis=pd.read_csv('tubercolusis.csv')
# tubercolusis=tubercolusis.drop(['Country Code','Indicator Code',
#                                 'Indicator Name'],axis=1)
# tubercolusis=tubercolusis.rename(columns = {'Country Name':'year'})
# tubercolusis=tubercolusis.set_index('year')

# tubercolusis=tubercolusis.transpose()

# tubercolusis_new=tubercolusis.loc[['2000','2002','2004','2006','2008','2010',
#                                    '2012','2014','2016'],
# ["China","India","Albania","Argentina","Ethiopia","Germany","South Africa",
#  "Finland","Iceland","Afghanistan",'Dominica','Pakistan']]

# #exploring dataframe using .describre method
# print(tubercolusis_new.describe())

# plt.figure(figsize=(8,6))
# plt.plot(tubercolusis_new.index,tubercolusis_new['China'],marker='o',
#          label='China',linestyle='--')
# plt.plot(tubercolusis_new.index,tubercolusis_new['Afghanistan'],marker='*',
#          label='Afghanistan',linestyle='--')
# plt.plot(tubercolusis_new.index,tubercolusis_new['India'],marker='^',
#          label='India',linestyle='--')
# plt.plot(tubercolusis_new.index,tubercolusis_new['Dominica'],
#          label='Dominica',marker='p',linestyle='--')
# plt.plot(tubercolusis_new.index,tubercolusis_new['Ethiopia'],
#          label='Ethiopia',marker='o',linestyle='--')
# plt.plot(tubercolusis_new.index,tubercolusis_new['Pakistan'],
#          label='Pakistan',marker='+',linestyle='--')
# plt.plot(tubercolusis_new.index,tubercolusis_new['Albania'],
#          label='Albania',linestyle='--',marker='s')

# plt.title('Incidence of tuberculosis (per 100,000 people)')
# plt.legend()
# plt.show()