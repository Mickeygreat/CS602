''' list of dictionaries
'''
import pprint as pp
pp.PrettyPrinter(indent =2)

colleges = [
    {"name":"Bentley","location":"Waltham"},
    {"name":"MIT","location":"Cambridge"},
    {"name":"UMass","location":"Amherst"},
    {"name":"UCLA","location":"Los Angeles"}
    ]
print (colleges)
print()
pp.pprint(colleges)
print()

for c in colleges:
    print (f'{c["name"]:15s}\t{c["location"]}')
    
# change a value
colleges[1]["location"] = "Kendall Square"
print (colleges)    

# add a new field for everyone
for c in colleges:
    c["tuition"]="50000" 

pp.pprint(colleges)

#delete from the list
colleges.pop(0)  # bye bye Bentley 
pp.pprint(colleges)

# add a new dict to the list

wpi = {"name":"WPI","location":"Worcester", "tuition":30000}
colleges.insert(2, wpi)
pp.pprint(colleges)

#delete the tuition field for everyone

for c in colleges:
    del (c["tuition"])
pp.pprint(colleges)

# print the keys in a list

names =  list(colleges[0].keys())
pp.pprint(colleges)



