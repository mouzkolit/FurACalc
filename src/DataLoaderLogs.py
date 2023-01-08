import pandas as pd 
import os 
import numpy as np 

class DataLoaderLogs:
    """Class that holds the log file data from the
    metamorph calcium imaging analysis
    """
    def __init__(self, path) -> None:
        """_summary_

        Args:
            path (_type_): _description_
        """
        self._path = path
        self.list_dataframes = []
        self.iterator = 0
        self.open_function_save_dataframe_tolist()
        
    def preprocess_logs(self,logs: str) -> pd.DataFrame:
        """Preprocess Function which runs through each line in the files
        Search for the String Time and Region to detect where the Data Starts

        Args:
            logs (str): log_file name as imported by the os module

        Returns:
            pd.DataFrame: Post processed dataframe that holds the calcium imaging data
        """
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
    
    def open_function_save_dataframe_tolist(self) -> None:
        """__summary__: Retrieves the path and opens the 
        """
        analysis_files = sorted([i  for i in os.listdir(self.path) if ".LOG" in i])
        if analysis_files:
            for i in analysis_files:
                dataframe = self.preprocess_logs(i)
                self.list_dataframes.append(dataframe)
        else:
            raise ValueError("No Analysis Files found!")
      
    @property
    def path(self) -> str:
        """ location getter"""
        return self._path
    
    @path.setter
    def path(self, path: str) -> None:
        """__summary__: location setter

        Args:
            path (str): path 
        """
        print(f"Setting path: {path} ")
        self._path = path
    
    def __str__(self) -> str:
        """ Setting the returned string by the class"""
        return "DataLogLoader: Active"
    
    def __iter__(self):
        """Iterator

        Returns:
            self: _description_
        """
        return self
    
    def __next__(self) -> None:
        """Iterator: that iterates through
        """
        if self.list_dataframes:
            if self.iterator <= len(self.list_dataframes):
                return self.list_dataframes[self.iterator]
            else:
                raise StopIteration
        else:
            raise ReferenceError("List DataFrames are not loaded properly")
                
        