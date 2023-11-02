import csv
from material_selector import ms

def read_csv_to_dict(filename):
    with open(filename, 'r') as csvfile:
        # Use DictReader to read the CSV file into a list of dictionaries
        csvreader = csv.DictReader(csvfile)
        
        # Create an empty list to store the dictionaries
        list_of_dicts = []
        
        # Iterate through the rows in the CSV file
        for row in csvreader:
            list_of_dicts.append(row)
            
    return list_of_dicts

# List of file names
files = [
    'fully_constrained_new_chemical_compositions_10_more_3.csv',
    'fully_constrained_new_chemical_compositions_10_more.csv',
    'fully_constrained_new_chemical_compositions_v8.csv'
]

# Create an empty dictionary to hold the list of dictionaries for each file
all_data = {}

# Read each file and store its contents in the all_data dictionary
for file in files:
    all_data[file] = read_csv_to_dict(file)

# Now all_data contains the list of dictionaries for each file

all_materials = []
for file in files:
    all_materials += list(all_data[file][0].keys())

all_materials = sorted(list(set(all_materials)))
print(all_materials)


final_item_list = []


def write_dict_to_csv(list_of_dicts, filename):
    # Open the file in write mode ('w')
    with open(filename, 'w', newline='') as csvfile:
        # Extract the field names (keys of the dictionary)
        fieldnames = list_of_dicts[0].keys()
        
        # Initialize DictWriter object
        csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # Write the header (field names)
        csvwriter.writeheader()
        
        # Write the rows
        for row in list_of_dicts:
            csvwriter.writerow(row)

for file in files:
    file_data = all_data[file]
    for row in file_data:
        row_final_data = {}
        for material in all_materials:
            row_final_data[material] = float(row.get(material, 0))
        composition = {}
        for material, value in row.items():
            float_val = float(value)
            if float_val > 0:
                composition[material] = float_val
        nearest = ms.get_existing_materials_with_min_distance(composition)
        neighbours = [item[1] for item in nearest]
        row_final_data["neighbours"] = "$".join(neighbours)
        final_item_list.append(row_final_data)

write_dict_to_csv(final_item_list, "materials_with_neighbours.csv")
