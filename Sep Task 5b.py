import copy

# Define a function to display configuration information
def display_config(config):
    for item in config:
        print(item)

# Define the production configuration as a list
production_config = [
    'Production Server 1',
    'Production Server 2',
    'Production Server 3'
]

# Display the original production configuration
print("Original Production Configuration:")
display_config(production_config)

# Create a deep copy of the production configuration for testing purposes
test_config_deep = copy.deepcopy(production_config)

# Modify the test configuration for testing purposes
test_config_deep.append('Test Server 4')

# Display the test configuration
print("\nTest Configuration (Deep Copy - Changes Do Not Affect Original):")
display_config(test_config_deep)

# The original production configuration remains unchanged by deep copy modifications
print("\nOriginal Production Configuration (Unchanged by Deep Copy Changes):")
display_config(production_config)
