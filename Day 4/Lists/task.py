states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# Positive Indexes
print(states_of_america[0])

# Negative Indexes
print(states_of_america[-1])

# Modifying items
states_of_america[0] = "Delaware Punch"
print(states_of_america[0])

# Adding items
states_of_america.append('Sonora')
print(states_of_america)

# Extend the list
states_of_mexico = ['Jalisco', 'Michoacan', 'Baja California Sur']
states_of_america.extend(states_of_mexico)
print(states_of_america)