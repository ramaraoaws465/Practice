#dictionary = a collection of {key:value} pairs
#ordred and changeable, No duplicates

capitals = {"USA": "Washington D.C",
              "India" : "New Delhi",
              "China" : "Beijing",
              "Russia" : "Moscow"}

print(capitals)

##if capitals.get("Japan"):
    #print("Capital exists in the dictionary")
#else:
    #print("Capital does n't exist in the dictionary")

#keys = capitals.keys()
#for key in capitals.keys():
 #print(key)

#values = capitals.values()
#for value in capitals.values():
  #  print(value)
items = capitals.items()
for key, value in capitals.items():
    print(f"{key}: {value}")
