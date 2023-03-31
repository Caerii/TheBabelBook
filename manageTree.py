
from treeNode import tree
def getChoices(choices):
    s = ""
    s += "0.) Exit\n"
    n=1
    for ch in choices:
        s += str(n)+  ".) "+ ch + "\n"
        n+=1
    return s

def getInt(s):
    n = None
    try:
        n = int(s)
    except Exception as e:
        pass
    return n

def makeMenu(prompt,choices): 
    n = None
    while n == None or n < 1 or n > len(choices):
        print(getChoices(choices))
        c = input(prompt+"\n")
        n = getInt(c)
        if n == 0:
            return None
        elif n == None or n < 1 or n > len(choices):
            print("Invalid choice.\n")
    return n-1

main_menu=['create','read','update','delete']

result = makeMenu('Select Action', main_menu)
print(f"User selected: ${result}")

if result == 0: #create
    t = tree()
    d = {}
    d['ParentNodeID'] = None
    d['NodeLabel'] = 'book1'
    d['NodeData'] = 'there once was a dog'
    d['NodeLevel'] = '3'
    t.set(d)
    t.insert()
    print(t.data)

if result == 1: #read
    t = tree()
    t.getAll() # get all records
    product_index = makeMenu('Select Product', t.toList())
    print("Here is the stuff:\n")
    print(t.data[product_index]['ParentNodeID'])
    print(t.data[product_index]['NodeLabel'])
    print(t.data[product_index]['NodeData'])
    print(t.data[product_index]['NodeLevel'])

if result == 2: #update
    t = tree()
    t.getAll()
    product_index = makeMenu('Select Book', t.toList())
    print("t.data!!! :", t.data)
    p_index = t.data[product_index]['NodeID']
    print(f"product index: {product_index}")
    # for field in p.fields:
        # p.data[product_index][field] = input(f"Enter {field}: ")

    t.data[product_index]['ParentNodeID'] = None
    t.data[product_index]['NodeLabel'] = 'bookvygt6ty'
    t.data[product_index]['NodeData'] = 'this time the dog chased the cat' 
    t.data[product_index]['NodeLevel'] = '4'
    t.update(product_index)

if result == 3: #delete
    t = tree()
    t.getAll()
    product_index = makeMenu('Select Product', t.toList())
    t_index = t.data[product_index]['NodeID']
    t.deleteById(t_index) #delete record by id
    print("Deleted product with id: " + str(t_index))