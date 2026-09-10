
## List of Radiator Springs townees in diecast collection ##

RS_townees_in_diecast = [
    {"name": "lightning mcqueen", "status": "owned" },
    {"name": "mater", "status": "owned" },
    {"name": "sally", "status": "owned"},
    {"name": "doc hudson", "status": "not owned"},
    {"name": "luigi", "status": "not owned"},
    {"name": "guido", "status": "not owned"},
    {"name": "fillmore", "status": "not owned"},
    {"name": "sheriff", "status": "owned"},
    {"name": "ramone", "status": "owned"},
    {"name": "sarge", "status": "owned"},
    # error found here:{"name": "sarge", "status": "owned"}
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    {"name": "flow", "status": "not owned"},
    {"name": "Red", "status": "not owned"},
    #{"name": "frencesco", "status": "not owned"},
    ##used the wrong character in the dictionary list
]
#if frencesco was included, this would happened:

##another bug found, missing commas in the last two entries
#{"name": "flow", "status": "not owned"}
#{"name": "frencesco", "status": "not owned"}

#if frencesco were in this list, this would happen:

#list of the radiator spring townees i owned in diecast
#lightning mcqueen - owned
#mater - owned
#sally - owned
#doc hudson - not owned
#luigi - not owned
#guido - not owned
#fillmore - not owned
#sheriff - owned
#ramone - owned
#sarge - owned
#flow - not owned
#frencesco - not owned

#note: frencesco is a world grand prix racer and not a radiator springs townee

print("list of the radiator spring townees i owned in diecast:")

for townee in RS_townees_in_diecast:
    print(f"{townee['name']} - {townee['status']}")
    #missing end-quotation within the f-string
    # print(f"{townee['name']}" - {townee['status']})
    #~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~
    
    