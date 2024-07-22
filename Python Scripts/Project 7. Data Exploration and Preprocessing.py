import pandas as pd
import sqlite3

# Loading CVS file with header
data_cvs = pd.read_cvs("percent_bachelors_degrees_women_usa.csv")
#print(data_cvs)

print(data_cvs.head(20))
