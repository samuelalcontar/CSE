# Dictionaries - Made up of key: value pair

dictionary = {"name": "Lance", "age": 23, "height": 5 * 12 + 8}
# Accessing things from a dictionary
print(dictionary["name"])
print(dictionary["age"])
print(dictionary["height"])
# add a pair to a dictionary
dictionary["profession"] = "telemarketer"


large_dictionary = {
    "CA": "California",
    "AZ": "Arizona",
    "NY": "New York"
}

print(large_dictionary["NY"])

larger_dictionary = {
    "CA": ["Fresno",
          "san francisco",
          "san jose"],
    "AZ":["phoenix",
          "Tuscon"],
    "NY":[
        "New york city",
         "brooklyn",]

}
print(larger_dictionary["NY"])
print(larger_dictionary["NY"][1])
print(larger_dictionary["AZ"][0])

largest_dictionary = {
    "CA":{
        "NAME": "CALIFORNIA",
        "POPULATION": 39250000,
        "BORDER ST" : [
            "Oregon",
            "Nevada",
            "Arizona"
        ]
    },
    "AZ":{
        "NAME": "ARIZONA",
        "POPULATION": 6931000,
        "BORDER ST":[
            "California",
            "Utah",
            "Nevada",
            "New Mexico"
        ]
    },
    "NY": {
        'Name': "New York",
        'Population': 19750000,
        'BORDER ST': [
            'Vermont',
            'Massachusetts',
            'Connecticut',
            'Pennsylvania',
            'New Jersey'
        ]
    }
}
current_node = largest_dictionary["NY"]
print(current_node["Name"])
print(current_node["Population"])

