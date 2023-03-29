import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def readfile(df_name,file_name):
    df_name=pd.read_csv(file_name)
    df_name.index=df_name['Country Name']
    df_name=df_name.drop(columns='Country Name')
    df_name_new=df_name.loc[["China","India","Australia","Spain","United States","Germany","South Africa","Finland","Brazil"],
                                    ['1990','1995','2000','2005','2010']]

    return df_name_new

ele_per_cap=readfile('ele_per_cap','electricity_per_capita.csv')
forest_sq_km=readfile('forest_sq_km','forest_sq.csv')
total_pop=readfile('world_pop','total_pop.csv')
n_oxide=readfile('n_oxide','n_oxide.csv')
greenhouse_emission=readfile('greenhouse_emission','greenhouse.csv')


#print(ele_per_cap,forest_sq_km,world_pop,n_oxide)

#ele_per_cap_new=ele_per_cap_new.transpose()

def bar_plot(df_name):
    plt.figure()
    ax=plt.subplot()
    years=df_name.columns
    print(years)
    bar_width=0.9/len(years)
    x_ticks=df_name.index
    for i,year in enumerate(years):
        ax.bar([j+bar_width/2+bar_width*i for j in range(len(x_ticks))],df_name[year],
               width=bar_width,label=year)
        
    ax.set_xlabel('Country Name')
    #ax.set_ylabel(ele_per_cap_new)
    #ax.set_title(df_name[1])

    ax.set_xticks([j+0.4 for j in range(len(x_ticks))])
    ax.set_xticklabels(x_ticks,rotation=45)
    ax.legend()
    plt.show()
    
bar_plot(total_pop)
bar_plot(forest_sq_km)
bar_plot(ele_per_cap)
bar_plot(n_oxide)


#correlation of united states
USA=pd.DataFrame()
USA['world_pop']=total_pop.loc['United States',:]
USA['electricity_per_capita']=ele_per_cap.loc['United States',:]
USA['forest_sq']=forest_sq_km.loc['United States',:]
USA['n_oxide']=n_oxide.loc['United States',:]
USA['greenhouse_emission']=greenhouse_emission.loc['United States',:]


corr=USA.corr().to_numpy()
print(corr)

#corr=corr.style.background_gradient(cmap ='grey')
plt.figure(figsize=(6,6))
plt.imshow(USA.corr(),cmap='coolwarm',interpolation='nearest')
  
# Displaying a color bar to understand
# which color represents which range of data
plt.colorbar()
  
# Assigning labels of x-axis 
# according to dataframe
plt.xticks(range(len(USA)), USA.columns,rotation=90)
# Assigning labels of y-axis 
# according to dataframe
plt.yticks(range(len(USA)), USA.columns)
for i in range(len(USA.columns)):
    for j in range(len(USA.columns)):
        text = plt.text(j, i, corr[i, j].round(2),
                       ha="center", va="center", color="w")
# Displaying the figure
plt.show()



