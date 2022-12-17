programmer = {
    "name" : "Mahfuz Islam Khan Jabed",
    "age"  : 22,
    "Programming language" : "Python"
}
print(type(programmer))
print(programmer)
print(programmer["name"])
print(programmer["age"])
print(programmer["Programming language"])
#print(programmer["country"])  #traceback error
print(programmer.get("Home Country"))
print(programmer.get("country", "USA"))
programmer["subject"] = ["Computer Science"]
print(programmer["subject"])