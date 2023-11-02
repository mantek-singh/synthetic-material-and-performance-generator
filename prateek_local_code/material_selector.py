import pandas as pd
import math
from data_provider import DataProvider

dp = DataProvider()

# print(dp.compound_id_to_composition["17937-100"])
INPUT_MATERIALS = ['A_1', 'A_2', 'A_3', 'A_4', 'A_5', 'A_6', 'B_1', 'B_10', 'B_11', 'B_12', 'B_13', 'B_14', 'B_15', 'B_16', 'B_17', 'B_18', 'B_19', 'B_2', 'B_20', 'B_21', 'B_22', 'B_23', 'B_24', 'B_3', 'B_4', 'B_5', 'B_6', 'B_7', 'B_8', 'B_9', 'C_1', 'C_2', 'C_3', 'C_4', 'C_5', 'C_6', 'D_1', 'E_1', 'E_10', 'E_11', 'E_2', 'E_3', 'E_4', 'E_5', 'E_6', 'E_7', 'E_8', 'E_9', 'F_1', 'F_10', 'F_11', 'F_12', 'F_2', 'F_3', 'F_4', 'F_5', 'F_6', 'F_7', 'F_8', 'F_9']


class MaterialSelector:
    # MATERIAL_CLASSES = ["A", "B", "C", "D", "E", "F"]
    def __init__(self):
        pass
   
    def is_valid(self, composition):
        material_classes = ["A", "B", "C", "D", "E", "F"]
        bounds = {
            "A": [0, 12],
            "B": [1, 30],
            "C": [0, 18],
            "D": [0.4, 1],
            "E": [45, 92],
            "F": [3, 27],
        }

        amounts = {mc: 0 for mc in material_classes}
        for material, value in composition.items():
            material_class = material.split("_")[0]
            amounts[material_class] += value
        
        if (abs(sum(amounts.values()) - 100) > 1e-10):
            print(f"Diff from 100 is {sum(amounts.values()) - 100}")
            return False

        for material_class in material_classes:
            if (
                amounts[material_class] < bounds[material_class][0]
                or amounts[material_class] > bounds[material_class][1]
            ): 
                print(material_class, amounts[material_class], bounds[material_class], composition)
                return False
        
        return True

    def reduce_to_categories(self, composition):
        reduced_composition = {
            "A": 0,
            "B": 0,
            "C": 0,
            "D": 0,
            "E": 0,
            "F": 0
        }
        for mat, val in composition.items():
            reduced_composition[mat[0]] += val
        return reduced_composition
    
    def get_seperated_by_categories(self, composition):
        dict_of_categories = {}
        for mat, val in composition.items():
            category = mat[0]
            if category not in dict_of_categories:
                dict_of_categories[category] = {}
            dict_of_categories[category][mat] = val
        return dict_of_categories

    def euclidean_distance(self, composition1, composition2):
        all_keys = set(list(composition1.keys()) + list(composition2.keys()))
        sum_of_squares = 0
        for single_key in all_keys:
            diff = composition1.get(single_key, 0) - composition2.get(single_key, 0)
            sum_of_squares += diff * diff
        return math.sqrt(sum_of_squares)

    def get_composition_distance(self, c1, c2):
        reduced_c1 = self.reduce_to_categories(c1)
        reduced_c2 = self.reduce_to_categories(c2)
        distance1 = self.euclidean_distance(reduced_c1, reduced_c2)

        categorized_c1 = self.get_seperated_by_categories(c1)
        categorized_c2 = self.get_seperated_by_categories(c2)

        distance2 = 0
        all_categorized_keys = set(list(categorized_c1.keys()) + list(categorized_c2.keys()))
        for single_key in all_categorized_keys:
            distance2 += self.euclidean_distance(categorized_c1.get(single_key, {}), categorized_c2.get(single_key, {}))

        return distance1 + (distance2 / 2)

    def get_composition_distance_with_chemical(self, chemical_id, composition):
        existing_composition =  dp.compound_id_to_composition[chemical_id]
        return self.get_composition_distance(existing_composition, composition)

    def get_existing_materials_with_min_distance(self, composition):
        compound_ids = dp.compound_id_to_composition.keys()
        distances = []
        for compound_id in compound_ids:
            distances.append((self.get_composition_distance_with_chemical(compound_id,composition), compound_id))
        
        distances.sort()
        return distances[0:10]

    def write_compositions_csv(self, compositions, file_name, include_compound_ids=False):
        csv_str = ",".join(INPUT_MATERIALS)

        if include_compound_ids:
            csv_str += ",compound_id"
        csv_str += "\n"
        for composition in compositions:
            for mat in INPUT_MATERIALS:
                csv_str += str(composition.get(mat, 0)) + ", "
            csv_str = csv_str[:-2]
            if include_compound_ids:
                csv_str += "," + composition["compound_id"]
            csv_str += "\n"
        with open(file_name, 'w') as f:
            f.write(csv_str)
    
    def write_existing_compositions_csv(self):
        compound_ids = list(dp.compound_id_to_composition.keys())
        compositions = [dp.compound_id_to_composition[compound_id] for compound_id in compound_ids]
        for idx in range(len(compound_ids)):
            compositions[idx]["compound_id"] = compound_ids[idx]
        self.write_compositions_csv(compositions, "existing_compositions.csv", True)

ms = MaterialSelector()
com = {'A_6': 5, 'B_19': 7.0, 'B_21': 2.0, 'B_23': 8.0, 'C_1': 5.0, 'D_1': 0.8, 'E_1': 7.5, 'E_5': 23.2, 'E_6': 30.1, 'E_7': 1.4, 'F_9': 10.0}

# print(ms.get_existing_materials_with_min_distance(com))
