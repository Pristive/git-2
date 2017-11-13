import os
import pandas as pd
os.chdir("C:\\Users\\priyanka\\Desktop\\Rank_Projects\\raw")

# Checking the current working directory
dir = os.getcwd()

## Getting the list of files in the Current working Directory
os.listdir(dir)

# Saving the list of file names in a variable
raw_list = os.listdir(dir)

''' This loop reads the csv files one by one and then appends the data in a new file by stacking it I have used 2 csv files abc.csv and def.csv . both the files have 2 columns order_date and food '''

# I create a blank list named data for appending the processed data
data =[]
data = pd.DataFrame(data) # Converted to blank Data frame
for i in range(0,len(raw_list)):
    temp = pd.read_csv(raw_list[i])
    data = data.append(temp)
    print(i)
print("writing the appended data in processed folder")




''' Now I am chaging my directory again to processed directory to store the new files based on the date wise stacking as required in the question
I have used pandas group by method to do this '''


os.chdir("C:\\Users\\priyanka\\Desktop\\Rank_Projects\\processed")
df_by_date = data.groupby("order_date")
for (date, date_df) in df_by_date:
    filename = date.replace("/", "-") + ".csv"
    date_df.to_csv(filename , index = False)



del(data)
del(i)
del(temp)
''' All my files will be stored in PROCESSED Directory with independent date wise files for entries for that day only '''
