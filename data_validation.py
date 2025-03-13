#We can combine multiple files using Customer ID as primary key
#first read all the tables dataframes
df = pd.read_csv(base_dir + "Telco_customer_churn.csv")

#There are two ways "Customer ID" is written in column names: one with and one without space 
#fix column name to "Customer ID" in "Telco_customer_churn.csv" file
df = df.rename(columns = {'CustomerID':'Customer ID'})

list_of_csvs = ['CustomerChurn.csv', 'Telco_customer_churn_demographics.csv',
                'Telco_customer_churn_location.csv', 'Telco_customer_churn_population.csv',
                'Telco_customer_churn_services.csv', 'Telco_customer_churn_status.csv']

for file in list_of_csvs:
    temp = pd.read_csv(base_dir + file)

    if "Customer ID" in temp.columns.tolist():
        df = pd.merge(df, temp, on = "Customer ID", how = "left", suffixes=('', '_remove'))
    else:
        df = pd.merge(df, temp, on = "Zip Code", how = "left", suffixes=('', '_remove'))
            
# remove the duplicate columns
df.drop([i for i in df.columns if 'remove' in i], axis = 1, inplace = True)