# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import pandas as pd

df = pd.read_csv("output.csv")
df['Category'] = 'na'


def search_keyword_name(keyword, filename):
    for index, row in filename.iterrows():
        if keyword.lower() in str(row).lower():
            print(f'Found "{keyword}\n {row}')



def search_keyword_and_date(keyword,date, filename):
    for index, row in filename.iterrows():
        if (keyword.lower() in str(row).lower()) and (date.lower() in str(row).lower()):
            print(f'Found "{keyword}\n {row}')
        elif keyword.lower() in str(row).lower():
            print(f'Found "{keyword}\n {row}')


def search_student_or_low_income(keyword, keyword2, filename):
    for index, row in filename.iterrows():
        if (keyword.lower() in str(row).lower()):
            df.at[index, 'Category'] = 'Student'
        elif (keyword2.lower() in str(row).lower()):
            df.at[index, 'Category'] = 'Income'





# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    search_student_or_low_income("Student", "Income", df)

    user_keyword = input("Enter a keyword to search: ")


    another_input = input("Would you like to enter a date: ")


    if (another_input != ''):
        search_keyword_and_date(user_keyword, another_input, df)
    else:
        search_keyword_name(user_keyword, df)




    #for index in df.index:
        #print(df['Name'][index])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
