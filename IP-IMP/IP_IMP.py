#Name Creation
#The following section contains a Program List Python DataFrame based Dataframe Creation.

#Write a program to:

1 #Create an empty dataframe named as empty_df.

import pandas as pd

empty_df = pd.DataFrame()
print(empty_df)
#2 Create a dataframe named as students using a list of names of 5 students.

import pandas as pd
students = ["Ram","Aman","Akash","Ramesh","Virat"]
students = pd.DataFrame(students,columns=["Name"])
print(students)
#3 Write a program to create a dataframe players using a list of names and scores of the previous three matches.

#Using Nested List

import pandas as pd 
data = [["Virat",55,66,31],["Rohit",88,66,43],["Samson",99,101,68]]
players = pd.DataFrame(data, columns = ["Name","Match-1","Match-2","Match-3"])
print(players)
Using Dictionary:

import pandas as pd 
data = {"Virat":[55,66,31],"Rohit":[88,66,43],"Samson":[99,101,68]}
players = pd.DataFrame(data,columns = ["Name","Match-1","Match-2","Match-3"])
print(players)
#4 Write a program to create a dataframe salesman using the series sales_person which stored saleman names and quantity of sales of August.

import pandas as pd
sales_person = [["Ram",55],["Ajay",22],["Vijay",67],["Sachin",44]]
salesman = pd.DataFrame(sales_person,columns=["Name","Sales(August)"])
print(salesman)
#5 Write a program to create a dataframe countries using a dictionary which stored country name, capitals and populations of the country.

import pandas as pd
country_data = {"Country Name":["India","Canada","Australia"],
                "Capital": ["New Delhi","Ottawa","Canberra"],
                "Population" : ["136 Cr","10 Cr","50 Cr"]}
countries = pd.DataFrame(country_data)
print(countries)
#6 Write a program to create a dataframe df_nda ndArray that stores letters and words starting from ‘g’ to ‘p’.
#(The first column stores letter and the second column stores the words starting with that letter.)

#Program List Python DataFrame based on iterrows() and iteritems()
#7 Iterate dataframe created in question no. 3 by its rows.

import pandas as pd 

data = [["Virat",55,66,31],["Rohit",88,66,43],["Samson",99,101,68]]
players = pd.DataFrame(data, columns = ["Name","Match-1","Match-2","Match-3"])

for index, row in players.iterrows():
    print(index, row.values)

#8 Iterate dataframe created in question no. 4 by its columns.

import pandas as pd 

sales_person = [["Ram",55],["Ajay",22],["Vijay",67],["Sachin",44]]
salesman = pd.DataFrame(sales_person,columns=["Name","Sales(August)"])

for index, row in salesman.iterrows():
    print(index, row["Name"],row["Sales(August)"])

#9 Print scores of previous two matches along with their names using iterrows function. (Use dataframe created in question 3)

import pandas as pd 

data = [["Virat",55,66,31],["Rohit",88,66,43],["Samson",99,101,68]]
players = pd.DataFrame(data, columns = ["Name","Match-1","Match-2","Match-3"])

for index, row in players.iterrows():
    print(index, row["Name"],row["Match-2"],row["Match-3"])

#10 Print sales of salesman along with their index using iteritems(). (Use dataframe created in question 4)

import pandas as pd 

sales_person = [["Ram",55],["Ajay",22],["Vijay",67],["Sachin",44]]
salesman = pd.DataFrame(sales_person,columns=["Name","Sales(August)"])

for index, row in salesman.iteritems():
    print(index, row["Name"],row["Sales(August)"])
#11 Display the alternate rows using iterrows() function.


#12 Display the alternate columns using iteritems() function.


#13 Make a total of score from the dataframe players and display their rank according the their scores.

import pandas as pd 

data = [["Virat",55,66,31],["Rohit",88,66,43],["Samson",99,101,68],["Pant",77,55,21]]
players = pd.DataFrame(data, columns = ["Name","Match-1","Match-2","Match-3"])

players['Total_score'] = players['Match-1'] + players['Match-2'] + players["Match-3"]
players['Rank'] = players['Total_score'].rank(ascending=0)
print(players)
Program List Python DataFrame based on insert rows and columns
#14 Insert three new rows in dataframe students created by question 2.

import pandas as pd

students = ["Ram","Aman","Akash","Ramesh","Virat"]

students = pd.DataFrame(students,columns=["Name"])
print("---------- Original Dataframe --------------")
print(students)

values = ["Ajay","Vijay","Sanju"]
for val in values:
    temp = {"Name":val}
    students = students.append(temp,ignore_index=True)
print("----------- Updated DataFrame -------------")
print(students)
#15 Insert two columns at the last of dataframe salesman named city and state using insert function.

import pandas as pd 

sales_person = [["Ram",55],["Ajay",22],["Vijay",67],["Sachin",44]]
salesman = pd.DataFrame(sales_person,columns=["Name","Sales(August)"])

salesman.insert(2,"City",["Mumbai","Baroda","Udaipur","Banglore"])
salesman.insert(3,"State",["Maharashtra","Gujarat","Rajasthan","Karnataka"])
print(salesman)
#Some questions given in Assignments

#Programs based on Select and Access data
#Consider following data and write a program to do the following:
'''
SNO	Batsman	Test	ODI	T20
1	Virat Kohli	3543	2245	1925
2	Ajinkya Rehane	2578	2165	1853
3	Rohit Sharma	2280	2080	1522
4	Shikhar Dhawan	2158	1957	1020
5	Hardik Pandya	1879	1856	980
'''
#16 Print the batsman name along with runs scored in Test and T20 using column names and dot notation.

import pandas as pd 

# Creating the Data
player_data = {"Name":["Virat Kohli","Ajinkya Rahane","Rohit Sharma","Shikhar Dhawan","Hardik Pandya"],
                "Test" : [3543,2578,2280,2158,1879],
                "ODI" : [2245,2165,2080,1957,1856],
                "T20" : [1925,1853,1522,1020,980]}

data = pd.DataFrame(player_data)
# The following line is used to start the index from 1
data.index = data.index + 1

# ---------------------

print(data.Name)
print(data.Test)
print(data.T20)
#17 Display the Batsman name along with runs scored in ODI using loc.

import pandas as pd 

# Creating the Data
player_data = {"Name":["Virat Kohli","Ajinkya Rahane","Rohit Sharma","Shikhar Dhawan","Hardik Pandya"],
                "Test" : [3543,2578,2280,2158,1879],
                "ODI" : [2245,2165,2080,1957,1856],
                "T20" : [1925,1853,1522,1020,980]}

data = pd.DataFrame(player_data)
# The following line is used to start the index from 1
data.index = data.index + 1

# ---------------------
print(data.loc[:,('Name','ODI')])
#18 Display the batsman details who scored runs more than :

#More than 2000 in ODI
#Less than 2500 in Test
#More than 1500 in T20
import pandas as pd 

# Creating the Data
player_data = {"Name":["Virat Kohli","Ajinkya Rahane","Rohit Sharma","Shikhar Dhawan","Hardik Pandya"],
                "Test" : [3543,2578,2280,2158,1879],
                "ODI" : [2245,2165,2080,1957,1856],
                "T20" : [1925,1853,1522,1020,980]}

data = pd.DataFrame(player_data)
# The following line is used to start the index from 1
data.index = data.index + 1

# runs more than 2500 in ODI
print("---- Runs greater than 2500 in ODI ---------")
print(data.loc[data['ODI']>2500, ['Name']])

# Less than 2500 runs in test
print("---- Runs less than 2500 in Test ---------")
print(data.loc[data['Test']<2500, ['Name']])

# More than 1500 runs in T20
print("---- Runs more than 1500 in T20 ---------")
print(data.loc[data['T20']>1500, ['Name']])
#19 Display the columns using column index number like 0, 2, 4.

import pandas as pd 

# Creating the Data
player_data = {"Name":["Virat Kohli","Ajinkya Rahane","Rohit Sharma","Shikhar Dhawan","Hardik Pandya"],
                "Test" : [3543,2578,2280,2158,1879],
                "ODI" : [2245,2165,2080,1957,1856],
                "T20" : [1925,1853,1522,1020,980]}

data = pd.DataFrame(player_data)
# The following line is used to start the index from 1
data.index = data.index + 1

# =======================
print(data[data.columns[0]])
print(data[data.columns[2]])
#20 Display the alternated rows using at() function.

import pandas as pd 

# Creating the Data
player_data = {"Name":["Virat Kohli","Ajinkya Rahane","Rohit Sharma","Shikhar Dhawan","Hardik Pandya"],
                "Test" : [3543,2578,2280,2158,1879],
                "ODI" : [2245,2165,2080,1957,1856],
                "T20" : [1925,1853,1522,1020,980]}

data = pd.DataFrame(player_data)
# The following line is used to start the index from 1
data.index = data.index + 1

# ==============
print(data.at[1,])
#21 Reindex the dataframe created above with batsman name and delete data of Hardik Pandya and Shikhar Dhawan by their index from original dataframe.

import pandas as pd 
# Creating the Data
player_data = {"Name":["Virat Kohli","Ajinkya Rahane","Rohit Sharma","Shikhar Dhawan","Hardik Pandya"],
                "Test" : [3543,2578,2280,2158,1879],
                "ODI" : [2245,2165,2080,1957,1856],
                "T20" : [1925,1853,1522,1020,980]}
data = pd.DataFrame(player_data)
# The following line is used to start the index from 1
data.index = data.index + 1
# ----------------------
data = data.set_index('Name')
print(data)
# Now deleting records
print("Records after Deleting the values:")
data = data.drop(['Shikhar Dhawan','Hardik Pandya'])
print(data)
#22 Insert 2 rows in the dataframe and delete rows whose index is 1 and 4.

import pandas as pd 
# Creating the Data
player_data = {"Name":["Virat Kohli","Ajinkya Rahane","Rohit Sharma","Shikhar Dhawan","Hardik Pandya"],
                "Test" : [3543,2578,2280,2158,1879],
                "ODI" : [2245,2165,2080,1957,1856],
                "T20" : [1925,1853,1522,1020,980]}

data = pd.DataFrame(player_data)
# ----------------------
values = {'Name':['Rishabh Pant','Shreyas Iyer'],'Test':[1500,1459],'ODI':[1980,1342],'T20':[2300,1988]}
data = data.append(pd.DataFrame(values), ignore_index=True)
print(data)

# -----
print("Data after deleting index 1 and 4")
data = data.drop([1,4])
print(data)
#23 Delete a column Test, add one more column at last (next to T20 column), make total of ODI and T20 runs in that column.

import pandas as pd 
# Creating the Data
player_data = {"Name":["Virat Kohli","Ajinkya Rahane","Rohit Sharma","Shikhar Dhawan","Hardik Pandya"],
                "Test" : [3543,2578,2280,2158,1879],
                "ODI" : [2245,2165,2080,1957,1856],
                "T20" : [1925,1853,1522,1020,980]}
data = pd.DataFrame(player_data)
# The following line is used to start the index from 1
data.index = data.index + 1
# ----------------------
data = data.drop('Test', axis = 1)
print(data)
# ---------------
total = data['ODI'] + data["T20"]
data['Total'] = total
print(data)
#24 Delete columns using T20 and total using columns parameter in drop() function.

import pandas as pd 

# Creating the Data
player_data = {"Name":["Virat Kohli","Ajinkya Rahane","Rohit Sharma","Shikhar Dhawan","Hardik Pandya"],
                "Test" : [3543,2578,2280,2158,1879],
                "ODI" : [2245,2165,2080,1957,1856],
                "T20" : [1925,1853,1522,1020,980]}

data = pd.DataFrame(player_data)
# The following line is used to start the index from 1
data.index = data.index + 1
# ---------------
total = data['ODI'] + data["T20"]
data['Total'] = total

data = data.drop(['T20','Total'], axis = 1)
print(data)
#25 Rename column T20 with “T20I Runs”.

import pandas as pd 

# Creating the Data
player_data = {"Name":["Virat Kohli","Ajinkya Rahane","Rohit Sharma","Shikhar Dhawan","Hardik Pandya"],
                "Test" : [3543,2578,2280,2158,1879],
                "ODI" : [2245,2165,2080,1957,1856],
                "T20" : [1925,1853,1522,1020,980]}

data = pd.DataFrame(player_data)
# The following line is used to start the index from 1
data.index = data.index + 1

# ----------------------
data.rename(columns={'T20':'T20I runs'}, inplace = True)
print(data)
#26 Rename all the columns of dataframe with your choice of column names.

import pandas as pd 

# Creating the Data
player_data = {"Name":["Virat Kohli","Ajinkya Rahane","Rohit Sharma","Shikhar Dhawan","Hardik Pandya"],
                "Test" : [3543,2578,2280,2158,1879],
                "ODI" : [2245,2165,2080,1957,1856],
                "T20" : [1925,1853,1522,1020,980]}

data = pd.DataFrame(player_data)
# The following line is used to start the index from 1
data.index = data.index + 1

# ----------------------
data.rename(columns={'T20':'T20I runs','Name':'Player Name','Test':'Test Runs','ODI':'ODI Runs'}, inplace = True)
print(data)
#27 Rename the index with prefix IND and number like 001 and So on.

import pandas as pd 

# Creating the Data
player_data = {"Name":["Virat Kohli","Ajinkya Rahane","Rohit Sharma","Shikhar Dhawan","Hardik Pandya"],
                "Test" : [3543,2578,2280,2158,1879],
                "ODI" : [2245,2165,2080,1957,1856],
                "T20" : [1925,1853,1522,1020,980]}

data = pd.DataFrame(player_data)
# The following line is used to start the index from 1
data.index = data.index + 1

# ----------------------
index = pd.Index(["001","002","003","004","005"])
data = pd.DataFrame(player_data,index)
data = data.rename_axis('IND')
print(data)
#28 Display the first two rows and last two rows.

import pandas as pd 

# Creating the Data
player_data = {"Name":["Virat Kohli","Ajinkya Rahane","Rohit Sharma","Shikhar Dhawan","Hardik Pandya"],
                "Test" : [3543,2578,2280,2158,1879],
                "ODI" : [2245,2165,2080,1957,1856],
                "T20" : [1925,1853,1522,1020,980]}

data = pd.DataFrame(player_data)
# The following line is used to start the index from 1
data.index = data.index + 1

# ----------------------
print(data.head(2))
print(data.tail(2))
#29 Count the total number of rows and columns of the dataframe.

import pandas as pd 

# Creating the Data
player_data = {"Name":["Virat Kohli","Ajinkya Rahane","Rohit Sharma","Shikhar Dhawan","Hardik Pandya"],
                "Test" : [3543,2578,2280,2158,1879],
                "ODI" : [2245,2165,2080,1957,1856],
                "T20" : [1925,1853,1522,1020,980]
}

data = pd.DataFrame(player_data)
# The following line is used to start the index from 1
data.index = data.index + 1

# ----------------------
total_rows = len(data.axes[0])
total_col = len(data.axes[1])

print("Total Rows: " + str(total_rows))
print("Total Columns: " + str(total_col))
#30 Print the dataframe without headers. Go for the multiple options.

import pandas as pd 

# Creating the Data
player_data = {"Name":["Virat Kohli","Ajinkya Rahane","Rohit Sharma","Shikhar Dhawan","Hardik Pandya"],
                "Test" : [3543,2578,2280,2158,1879],
                "ODI" : [2245,2165,2080,1957,1856],
                "T20" : [1925,1853,1522,1020,980]
}

data = pd.DataFrame(player_data)
# The following line is used to start the index from 1
data.index = data.index + 1

# ----------------------
print(data.to_csv(header=None,index=False))
