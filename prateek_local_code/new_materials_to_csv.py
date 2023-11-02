from material_selector import ms
import ast

with open("generated_materials.txt") as f:
    material_lines = f.readlines()

materials = [ast.literal_eval(line) for line in material_lines]

print(materials)


valid_mats = []
for item in materials:
    if ms.is_valid(item):
        valid_mats.append(item)
    else:
        print("Error, Error, Error -- Detected an invalid material")
        print(item)

ms.write_compositions_csv(materials, "model_generated_mats.csv")
