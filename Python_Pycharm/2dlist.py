#2 Dimensional list

#fruits =     ["apple", "orange", "banana", "coconut"]
#vegetables = ["celery", "carrots", "Potatoes"]
#meats =      ["chicken", "fish", "turkey"]
''' list----
groceries = [["apple", "orange", "banana", "coconut"],
             ["celery", "carrots", "Potatoes"],
             ["chicken", "fish", "turkey"]] ---'''
groceries = [{"apple", "orange", "banana", "coconut"},
             {"celery", "carrots", "Potatoes"},
             {"chicken", "fish", "turkey"}]


#print(groceries[0][3])

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()