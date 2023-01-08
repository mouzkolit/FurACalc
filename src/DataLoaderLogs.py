import pandas as pd 
import os 
import numpy as np 



class DataLoaderLogs:
    def __init__(self, path) -> None:
        self.path = path
        self.list_dataframes = []
        self.iterator = 0
        self.open_function_save_dataframe_tolist()
        
    def preprocess_logs(self,logs):
        """preprocess the log files to return a table with the ratios for Calcium Imaging"""
        before_string = "string"
        columns = None
        list_tables = []
        with open(self.path + "/" + logs) as file:
            lines = file.readlines()
            for line in lines:
                try: 
                    if ("Time" in line) & ("Region" in before_string):
                        data = line.split(",")
                        data = [i.replace('"', "") for i in data]
                        columns = data
                        before_string = "None"
                        
                    elif before_string == "None":
                        data = line.split(",")
                        try:
                            data = [float(i) for i in data]
                            list_tables.append(data)
                        except Exception as e:
                            print(e)
                    else:
                        before_string = line.split()[0]
                        
                except Exception as e:
                    print(e)
        print(f"Succesfully run through file {logs}")            
        return pd.DataFrame(list_tables, columns = columns).drop("Time (sec)", axis = 1)
    
    def open_function_save_dataframe_tolist(self):
        """ get the dataframe from the file and append to list"""
        analysis_files = sorted([i  for i in os.listdir(self.path) if ".LOG" in i])

        for i in analysis_files:
            dataframe = self.preprocess_logs(i)
            self.list_dataframes.append(dataframe)
        print(len(self.list_dataframes))
            
    
    def __str__(self):
        return "DataLogLoader: Active"
    
    def __iter__(self):
        return self
    
    def __next__(self):
        """Iterator: that iterates through
        """
        if self.list_dataframes:
            if self.iterator <= len(self.list_dataframes):
                return self.list_dataframes[self.iterator]
            else:
                raise StopIteration
        else:
            raise ReferenceError("List DataFrames are not loaded properly")
                
        