import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#function for reading csv files
def readfile(file_name):
   '''
    

    Parameters
    ----------
    file_name : STR
        takes input as string as file name and creates a dataframe.

    Returns
    -------
    df_name_new : Pandas.DataFrame
        returns the dataframe after manipulating the data.

    '''
   #reading the data file
   df_name=pd.read_csv(file_name)
   
   #changing the index to country Name
   df_name.index=df_name['Country Name']
    
   #extracting the data that is required from the dataframe
   df_name_new=df_name.loc[["China","India","Australia","Spain",
                "United States","Germany","South Africa","Finland","Brazil"],
                                ['1990','1995','2000','2005','2010','2014']]

   return df_name_new
print(readfile('electricity_per_capita.csv'))
#function for transposing the dataframe 
def trans(df_name):
    df_trans=df_name.transpose()
    lst=list(df_trans.columns)
    lst[0]='Year'
    df_trans.columns=lst
    return df_trans
    
 

#a function for creating bar-graphs 
def bar_plot(df_name,title_name):
    '''
    

    Parameters
    ----------
    df_name :  pandas.DataFrame
        a bar plot will be plotted for the given dataframe.
    title_name : STR
        graphs title name.

    
    '''
    plt.figure(figsize=(8,6))
    ax=plt.subplot()
    years=df_name.columns
    print(years)
    bar_width=0.9/len(years)
    x_ticks=df_name.index
    for i,year in enumerate(years):
        ax.bar([j+bar_width/2+bar_width*i for j in range(len(x_ticks))],
                df_name[year],
                width=bar_width,label=year)
        
    ax.set_xlabel('Country Name')
    ax.set_ylabel(title_name)
    #ax.set_title(df_name[1])

    ax.set_xticks([j+0.4 for j in range(len(x_ticks))])
    ax.set_xticklabels(x_ticks,rotation=45)
    ax.legend(bbox_to_anchor=(1,1),title='years')
    plt.title(title_name)
    plt.show()
 



# function  for correlation between columns of new dataframe 
def correlation(df_name,country_name):
    '''
    

    Parameters
    ----------
    df_name : pandas.DataFrame
        creates a new dataframe for each country with differrent columns from\
            different dataframes.
    country_name : STR
        creates a correlation for country that is given as input.

    Returns
    -------
    df_name : pandas.DataFrame
        A new dataframe is returned after performing manipulation on data.

    '''
    df_name=pd.DataFrame()
    df_name['world_pop']=total_pop.loc[country_name,:]
    df_name['electricity_per_capita']=ele_per_cap.loc[country_name,:]
    df_name['forest_sq']=forest_sq_km.loc[country_name,:]
    df_name['n_oxide']=n_oxide.loc[country_name,:]
    df_name['greenhouse_emission']=greenhouse_emission.loc[country_name,:]
    df_name['urbanpopulation']=urbanpopulation.loc[country_name,:]
    
    corr=df_name.corr().to_numpy()
    
    #corr=corr.style.background_gradient(cmap ='grey')
    plt.figure(figsize=(6,6))
    plt.imshow(df_name.corr(),cmap='coolwarm',interpolation='nearest')
      
    # Displaying a color bar to understand
    # which color represents which range of data
    plt.colorbar()
      
    # Assigning labels of x-axis 
    # according to dataframe
    plt.xticks(range(len(df_name)), df_name.columns,rotation=90)
    # Assigning labels of y-axis 
    # according to dataframe
    plt.yticks(range(len(df_name)), df_name.columns)
    for i in range(len(df_name.columns)):
        for j in range(len(df_name.columns)):
              plt.text(j, i, corr[i, j].round(2),
                            ha="center", va="center", color="w")
    # Displaying the figure
    plt.title(country_name)
    plt.show()
    return df_name
    
#using of groupby function
nitrousoxide=pd.read_csv('n_oxide.csv')
nitrousoxide_new=nitrousoxide[['Country Name','1990','1995','2000',
                               '2005','2010']]
#groupby country name and calculating mean and median of each year
gby_mean=nitrousoxide_new.groupby('Country Name').mean()
gby_median=nitrousoxide_new.groupby('Country Name').median()

#returning the dataframe
print(gby_mean)
print(gby_median)


#line plot 1

#reading data frame using readfile function
tubercolusis=pd.read_csv('tubercolusis.csv')

#dropping the columns from the dataframe
tubercolusis=tubercolusis.drop(['Country Code','Indicator Code',
                                'Indicator Name'],axis=1)

#renaming the column country name to year
tubercolusis=tubercolusis.rename(columns = {'Country Name':'year'})

#setting the column year as index 
tubercolusis=tubercolusis.set_index('year')

#transposing the dataframe using transpose function
tubercolusis=tubercolusis.transpose()

#manipulating the data of tuberculosis dataframe 
#and storing it in new dataframe
tubercolusis_new=tubercolusis.loc[['2000','2002','2004','2006','2008','2010',
                '2012','2014','2016'],["China","India","Australia","Spain",
                "United States","Germany","South Africa","Finland","Brazil"]]


#exploring dataframe using .describre method
print(tubercolusis_new.describe())

#plotting the line graph using matplotlib.pyplot as plt
plt.figure(figsize=(8,6))
plt.plot(tubercolusis_new.index,tubercolusis_new['China'],marker='o',
          label='China',linestyle='--')
plt.plot(tubercolusis_new.index,tubercolusis_new['Australia'],marker='*',
          label='Australia',linestyle='--')
plt.plot(tubercolusis_new.index,tubercolusis_new['India'],marker='^',
          label='India',linestyle='--')
plt.plot(tubercolusis_new.index,tubercolusis_new['Spain'],
          label='Spain',marker='p',linestyle='--')
plt.plot(tubercolusis_new.index,tubercolusis_new['United States'],
          label='United States',marker='o',linestyle='--')
plt.plot(tubercolusis_new.index,tubercolusis_new['Germany'],
          label='Germany',marker='+',linestyle='--')
plt.plot(tubercolusis_new.index,tubercolusis_new['South Africa'],
          label='South Africa',linestyle='--',marker='s')
plt.plot(tubercolusis_new.index,tubercolusis_new['Finland'],
          label='Finland',linestyle='--',marker='s')
plt.plot(tubercolusis_new.index,tubercolusis_new['Brazil'],
          label='Brazil',linestyle='--',marker='s')

#labelling the x axis 
plt.xlabel('Years')
#labelling the y axis 
plt.ylabel('Incidence of tuberculosis (per 100,000 people)')
#setting the titile name
plt.title('Incidence of tuberculosis (per 100,000 people)')
#legend for labels
plt.legend(bbox_to_anchor=(1,1),title='country')
plt.show()


#line plot 2
#line plot for electricity_per_capita
#reading data frame using readfile function
ele_per_cap=pd.read_csv('electricity_per_capita.csv')

#dropping the columns from the dataframe
ele_per_cap=ele_per_cap.drop(['Country Code','Indicator Code',
                               'Indicator Name'],axis=1)
#renaming the column country name to year
ele_per_cap=ele_per_cap.rename(columns = {'Country Name':'year'})
#setting the column year as index
ele_per_cap=ele_per_cap.set_index('year')
#transposing the dataframe using transpose function
ele_per_cap=ele_per_cap.transpose()

#manipulating the data of tuberculosis dataframe 
#and storing it in new dataframe
ele_per_cap=ele_per_cap.loc[['1990','1995','2000','2005','2010','2014'],
              ["China","India","Australia","Spain",
            "United States","Germany","South Africa","Finland","Brazil"]]

#exploring dataframe using .describre method
print(ele_per_cap.describe())
#plotting the line graph using matplotlib.pyplot as plt
plt.figure(figsize=(8,6))
plt.plot(ele_per_cap.index,ele_per_cap['China'],marker='o',
          label='China',linestyle='--')
plt.plot(ele_per_cap.index,ele_per_cap['Australia'],marker='*',
          label='Australia',linestyle='--')
plt.plot(ele_per_cap.index,ele_per_cap['India'],marker='^',
          label='India',linestyle='--')
plt.plot(ele_per_cap.index,ele_per_cap['Spain'],
          label='Spain',marker='p',linestyle='--')
plt.plot(ele_per_cap.index,ele_per_cap['United States'],
          label='United States',marker='o',linestyle='--')
plt.plot(ele_per_cap.index,ele_per_cap['Germany'],
          label='Germany',marker='+',linestyle='--')
plt.plot(ele_per_cap.index,ele_per_cap['South Africa'],
          label='South Africa',linestyle='--',marker='s')
plt.plot(ele_per_cap.index,ele_per_cap['Finland'],
          label='Finland',linestyle='--',marker='s')
plt.plot(ele_per_cap.index,ele_per_cap['Brazil'],
          label='Brazil',linestyle='--',marker='s')

#labelling the x axis 
plt.xlabel('Years')
#labelling the y axis
plt.ylabel('Electric power consumption (kWh per capita)')
#setting the titile name
plt.title('Electric power consumption (kWh per capita)')
#legend for labels
plt.legend(bbox_to_anchor=(1,1),title='country')
plt.show()

#calling the above all functions

#reading the data-world-bank csv files using above function 
forest_sq_km=readfile('forest_sq.csv')
total_pop=readfile('total_pop.csv')
n_oxide=readfile('n_oxide.csv')
greenhouse_emission=readfile('greenhouse.csv')
urbanpopulation=readfile('urbanpopulation.csv')
ele_per_cap=readfile('electricity_per_capita.csv')  
print(ele_per_cap,urbanpopulation,greenhouse_emission,n_oxide,total_pop,
      forest_sq_km) 


#calling the function for plotting bar graph for different dataframes    
 
bar_plot(total_pop,'Total Country Population')
bar_plot(forest_sq_km,'Forest Area in Sq Km for Each Country')
bar_plot(ele_per_cap,'Electric power consumption (kWh per capita)')
bar_plot(greenhouse_emission,'Total greenhouse gas emissions (kt of CO2 \
          equivalent)')
bar_plot(n_oxide,'Nitrous oxide emissions (thousand metric tons of CO2\
          equivalent)')
bar_plot(urbanpopulation,'World Wide Urban Population ')

#calling the function and
#finding correlation between factors for different countries
USA=correlation('USA','United States')
India=correlation('India','India')
Spain=correlation('Spain','Spain')
Germany=correlation('Germany','Germany')
Finland=correlation('Finland','Finland')
Brazil=correlation('Brazil','Brazil')
print(USA,India,Finland,Germany,Spain)

#calling the transpose function and returns the transpose of dataframe
ele_per_cap=trans(ele_per_cap)
urbanpopulation=trans(urbanpopulation)
greenhouse_emission=trans(greenhouse_emission)
n_oxide=trans(n_oxide)
total_pop=trans(total_pop)
forest_sq_km=trans(forest_sq_km)
print(ele_per_cap,urbanpopulation,greenhouse_emission,n_oxide,total_pop,
      forest_sq_km)
