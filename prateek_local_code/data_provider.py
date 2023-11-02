import pandas as pd
import math

df = pd.read_csv("challenge1_data.csv", delimiter=",")


class DataProvider:
    def __init__(self):
        self.unique_compound_ids = df["compound_id"].unique()
        self.grouped_by_compound = df.groupby("compound_id")

        # Create a dictionary to store the DataFrames
        self.compound_dataframes = {}
        all_columns = df.columns.tolist()
        self.material_columns = sorted([col for col in all_columns if col[0].isupper()])

        # Iterate through the groups and store them in the dictionary
        for compound_id, compound_group in self.grouped_by_compound:
            self.compound_dataframes[compound_id] = compound_group
        self.compound_id_to_composition = {}
        for compound_id in self.unique_compound_ids:
            self.compound_id_to_composition[compound_id] = {
                x: self.compound_dataframes[compound_id].iloc[0][x]
                for x in self.material_columns
                if self.compound_dataframes[compound_id].iloc[0][x] > 0
            }
    
    def get_compound_set(self):
        self.compound_id_to_composition_map = {}
        for compound_id in self.unique_compound_ids:
            material_class_arr = []

            for x in self.material_columns:
                material_class_arr.append(self.compound_dataframes[compound_id].iloc[0][x])
            
            material_class_arr = tuple(material_class_arr)

            if material_class_arr in self.compound_id_to_composition_map:
                self.compound_id_to_composition_map[material_class_arr] += 1
            else:
                self.compound_id_to_composition_map[material_class_arr] = 1
        
        return self.compound_id_to_composition_map
