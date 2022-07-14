""""
Read state data
"""
import pprint as pp

f= open ("state_data.txt", "r")

state_data = f.read().strip().split("\n")

pp.pprint(state_data)

dict_states = {}
first_row = True
for state in state_data:
    if first_row:
        first_row = False
        continue
    data = state.split(",")


    state_name = data[0]
    capital = data[1]
    latitude = data[2]
    longitude = data[3]
    dict_states[state_name] = [capital, latitude, longitude]

pp.pprint(dict_states)

done = False
while not done:
    state_name = input("Enter a state name: ")
    if state_name in dict_states.keys():
        result = dict_states[state_name]
        print ("Capital:  " , result[0])
        print ("Latitude: ", result[1])
        print ("Longitude:", result[2])
    elif state_name == "quit":
        done = True
    else:
        print("State not found.")
print("End of program.")
