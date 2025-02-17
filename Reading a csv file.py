import pandas as pd
names={'name':['mark','john','doe','jane'],
       'age':[23,24,67,81],
       'city':['nairobi','kisumu','eldoret','mombasa']}
df=pd.DataFrame(names)
print('data frame is:\n',df)

# We'll save the DataFrame to a CSV file using the to_csv() method.
# The index=False argument ensures that the row indices are not saved to the file.

df.to_csv('names.csv',index=False)
print('data saved to csv file')

#After running this code, a file named people.csv will be created in your working directory. 
# Open it in a text editor or Excel to see its contents:
df_read=pd.read_csv('names.csv')
print('data read from csv file is:\n',df_read)
# The read_csv() function reads the CSV file and returns a DataFrame.
