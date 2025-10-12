# # Understand: 
#     #input: map[name : str, criteria : [str]], str: criteria
#     #sustainable brand: meets criterion
#     # map[name : str, criteria : [str]]
#     #return all brands that meet criteria
#     #output: [str]
#     #constraint: NA
# # Plan:
# # 


#     #criterion_set = set(criterion)
#     #output = []
#     # for brand in brands:
#         # if criterion in brand['criteria']:
#             #output.append(brand['name'])
#     #return output
#     #O(# companies * maxlen of criterion for each company)
# from collections import defaultdict
# def filter_sustainable_brands(brands, criterion):
#     output = []
#     for brand in brands:
#         if criterion in brand['criteria']:
#             output.append(brand['name'])
#     return output

#     #O(# brands * # criteria * len(criterion)) 
#     #O(n) space cuz output array

# brands = [
#     {"name": "EcoWear", "criteria": ["eco-friendly", "ethical labor"]},
#     {"name": "FastFashion", "criteria": ["cheap materials", "fast production"]},
#     {"name": "GreenThreads", "criteria": ["eco-friendly", "carbon-neutral"]},
#     {"name": "TrendyStyle", "criteria": ["trendy designs"]}
# ]

# brands_2 = [
#     {"name": "Earthly", "criteria": ["ethical labor", "fair wages"]},
#     {"name": "FastStyle", "criteria": ["mass production"]},
#     {"name": "NatureWear", "criteria": ["eco-friendly"]},
#     {"name": "GreenFit", "criteria": ["recycled materials", "eco-friendly"]}
# ]

# brands_3 = [
#     {"name": "OrganicThreads", "criteria": ["organic cotton", "fair trade"]},
#     {"name": "GreenLife", "criteria": ["recycled materials", "carbon-neutral"]},
#     {"name": "FastCloth", "criteria": ["cheap production"]}
# ]

# # print(filter_sustainable_brands(brands, "eco-friendly"))
# # print(filter_sustainable_brands(brands_2, "ethical labor"))
# # print(filter_sustainable_brands(brands_3, "carbon-neutral"))

# #problem 2:

# #input: { name : str, materials : list[str]}
#     #track which mats used by brands and how many times each material appears
#     #return mat names and # times each material appears
# #output: { str : int * _}
# #constraint: NA

# # Plan:
# #from collections import defaultdict
# # initialize a dict
# # for brand in brands:
# #  for mat in materials
#     #dict[mat] +=1
# #return dict

# def count_material_usage(brands):
#     output = defaultdict(int)
#     for brand in brands:
#         for mat in brand['materials']:
#             output[mat]+=1
#     return output

# brands = [
#     {"name": "EcoWear", "materials": ["organic cotton", "recycled polyester"]},
#     {"name": "GreenThreads", "materials": ["organic cotton", "bamboo"]},
#     {"name": "SustainableStyle", "materials": ["bamboo", "recycled polyester"]}
# ]

# brands_2 = [
#     {"name": "NatureWear", "materials": ["hemp", "linen"]},
#     {"name": "Earthly", "materials": ["organic cotton", "hemp"]},
#     {"name": "GreenFit", "materials": ["linen", "recycled wool"]}
# ]

# brands_3 = [
#     {"name": "OrganicThreads", "materials": ["organic cotton"]},
#     {"name": "EcoFashion", "materials": ["recycled polyester", "hemp"]},
#     {"name": "GreenLife", "materials": ["recycled polyester", "bamboo"]}
# ]

# # print(count_material_usage(brands))
# # print(count_material_usage(brands_2))
# # print(count_material_usage(brands_3))

# #problem 3:

# #input: { name : str, materials : [str]}
#     #return trending materials:
#         #appear > 1
# #output: [str]
# #constraint:

# def find_trending_materials(brands):
#     material_freq = defaultdict(int)
#     result = []
#     for brand in brands:
#         for material in brand['materials']:
#             material_freq[material] += 1
#             if material_freq[material] == 2:
#                 result.append(material)
#     return result
    
# brands = [
#     {"name": "EcoWear", "materials": ["organic cotton", "recycled polyester"]},
#     {"name": "GreenThreads", "materials": ["organic cotton", "bamboo"]},
#     {"name": "SustainableStyle", "materials": ["bamboo", "recycled polyester"]}
# ]

# brands_2 = [
#     {"name": "NatureWear", "materials": ["hemp", "linen"]},
#     {"name": "Earthly", "materials": ["organic cotton", "hemp"]},
#     {"name": "GreenFit", "materials": ["linen", "recycled wool"]}
# ]

# brands_3 = [
#     {"name": "OrganicThreads", "materials": ["organic cotton"]},
#     {"name": "EcoFashion", "materials": ["recycled polyester", "hemp"]},
#     {"name": "GreenLife", "materials": ["recycled polyester", "bamboo"]}
# ]

# print(find_trending_materials(brands))
# print(find_trending_materials(brands_2))
# print(find_trending_materials(brands_3))

#problem 4:
#input: [(str, int)] fabrics, int budget
    #closest to budget without exceeding it
#output: int
#constraint: NA

#O(N log N) time + O(1) mem

# Plan: 
# best_fabrics = tuple()
# min_difference = float('inf')
# sort list of tuples
# left_pointer = 0
# right_pointer = len(list) - 1
# while left < right:
# compute sum of cost
# if sum <= budget:
    # sum < min_difference:
        # min_difference = sum
        # best_fabrics = (fabrics[left], fabrics[right])
    # left += 1
# else:
# right -= 1

def find_best_fabric_pair(fabrics, budget):
    best_fabrics = tuple()
    min_difference = float('inf')
    sorted_fabrics = sorted(fabrics, key=lambda x: x[1])
    left = 0
    right = len(sorted_fabrics) - 1
    while left < right:
        sum = sorted_fabrics[left][1] + sorted_fabrics[right][1]
        if sum <= budget:
            if sum < min_difference:
                min_difference = sum
                best_fabrics = (fabrics[left][0], fabrics[right][0])
            left += 1
        else:
            right -= 1
    return best_fabrics

fabrics = [("Organic Cotton", 30), ("Recycled Polyester", 20), ("Bamboo", 25), ("Hemp", 15)]
fabrics_2 = [("Linen", 50), ("Recycled Wool", 40), ("Tencel", 30), ("Organic Cotton", 60)]
fabrics_3 = [("Linen", 40), ("Hemp", 35), ("Recycled Polyester", 25), ("Bamboo", 20)]

print(find_best_fabric_pair(fabrics, 45))
print(find_best_fabric_pair(fabrics_2, 70))
print(find_best_fabric_pair(fabrics_3, 60))