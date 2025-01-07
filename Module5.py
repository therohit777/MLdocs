# FRAMING THE PROBLEM:
# Let's take an Example of Netflix:

# 1. Bussiness Problem to ML Problem i.e. 
#              mathematical problem. 
#             (Reduce Churn Rate.)

# 2. Types of Solutions feasible for a  problem: Predict customer who are going 
#                                                to leave platform.

# 3. Current available solutions: Factors to caclute 
#                                 Churn Rate.                     

# 4. Understanding and Getting Data: watch time, search but did not find, 
#                  content left in middle,etc.
#                  Data will be provided by 
#                  data Engineering team.


# 5. Online or Batch Training: Model consideration.
#                             (Online for Netflix)

# 6. Check Assumptions: i. Features decided like watch time,
#                          search but did not find, etc are 
#                          like present or not.
# 
#                       ii. Geography ke basis mai features
#                           we have considered is correct or not. 


# Note:  Churn Rate: How many active users in our platform are 
#                    leaving your platform after a certain period of
#                    of time (Monthly, Quaterly,Yearly). 






# DATA GATHERING:
#   1. CSV: (Comma Separated Values.)
#      TSV: (Tab Separated Values.)

#   PANDAS LIBRARIES:
#   1. Loading CSV from local Machine/URL:
#        Example: 
#          import panda as pd
#          df = pd.read_csv('filename.csv') // file path or URL path
#          df = pd.read_json('file.json') // working with JSON  
#          print(df) // prints all datas in their column format.
 

#   2. Sep Parameter:
#        sep default  value is ",".
#        To read tsv file
#        Example: 
#          df = pd.read_csv('filename.csv', sep'\t', names=['Name',"Roll no.","address"])  
#          //  default sep parameter changed to tab. 
#          // 'Name',"Roll no.","address" these are header names. 
 

#   3. Index_col parameter (to changes default index of pandas):
#        Example:
#           df = pd.read_csv('filename.csv,index_col="student_id") // student_id is now your index
 

#   4. Header parameter (column name confusion, if panda consider column name as 1 row of data.)
#         Example:
#           df = pd.read_csv('filename.csv,header=1) // student_id is now your index


#   5. use_cols parameter:
#         Only provides the required columns, from the entire datasets
#         Example:
#           df = pd.read_csv('filename.csv,usecols=["Student_id","Name"]) // "Student_id","Name" colums will only be extracted now.

#   6. Squeeze parameters: 
#         Generates pandas series object not a dataframe,
#         when we require only 1 column from datasets.
#         Example:
#           df = pd.read_csv('filename.csv,usecols=["Student_id",squeeze=true]) 


#   7. SkipRows/nrows Parameter:
#      Helps in skipping particular rows.
#      Example:
#          df = pd.read_csv('filename.csv,skiprows=[0,5]) // 0th and 5th row will be excluded
#          df = pd.read_csv('filename.csv,nrows=100) // displays first 100 rows only
 

#   8. Encoding Parameter:
#      utf-8 is default encoding parameter, But if different encoding parameter,
#      please change the default encoding parameter.
#      Example:
#          df = pd.read_csv('filename.csv,encoding='latin-1')


#   9. Skip Bad Lines Parameter:
#      If parser error due to extra of less data in rows, please skip those bad rows/line   
#        Example: 
#          df = pd.read_csv('filename.csv,error_bad_lines=False)


#  10. dtypes Parameter:
#        changes datatype of a column 
#        Example: 
#          df = pd.read_csv('filename.csv,dtype={'columnName':int}) // int is the datatype in which columns needs to be converted.


#  11. Handling Dates:
#        In read_csv the dates gets parsed as string but, in order to 
#        use the the date filter functionality we need to keep dates in
#        date format.
#        Example:   
#           df = pd.read_csv('filename.csv,parse_dates=['columnName']) // columnNames are columns which we want to parse as dates.  


#  12. Converters.
#        If we want to change data of a column we can do it using converters.
#        Example: 
#           df = pd.read_csv('filename.csv,converters={'columnName':functionName}) // to this particular column the changes returned from function mentioned will be made.


#  13. na_values Parameter:
#       If we want to show come particular vaules as empty values we use na_values
#       Example: 
#         df = pd.read_csv('filename.csv,na_values={'Male'}) // all places having 'Male' as values will be replaced by NaN


#  14. Loading Huge dataset in Chunks:
#       While loading a huge datasets divides datasets in smaller chunks. 
#       Example: 
#         dfs = pd.read_csv('filename.csv,chunksize=5000) // file had 15000 data
#         for chunks in dfs:
#             print(chunk.shape) 
# 
#         Output:
#           (5000,10)
#           (5000,10)
#           (5000,10)


#  15. Loading datasets from MySQL.
#          Helps in loading SQL files by bassing sql connector object and sql_query. 
#          Example:
#            import mysql.connector
#            conn = mysql.connector.connect(host='localhost',user='root',password='',database='world')
#            pd.read_sql_query('SELECT * FROM NAME WHERE MARKS=30',conn) // conn is a mysql connection object is of mysql.

# 16. Creating a DataFrame via API using Pandas:
#        Example:
#          import pandas as pd
#          import requests

#          response = requests.get('WebsiteURL') // from where we gonna get data
#          df = pd.DataFrame(response.json()['results'])

# 17. Converting a Dataframe to CSV file.
#        Example:
#             df.to_csv('csvFileName')
 





# Note: API (Application Programming Interface) are nothing 
#       data pipeline which helps to communicate a information from point A to point B.
