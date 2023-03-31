
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
    p = product()
    p.getAll() # get all records
    product_index = makeMenu('Select Product', p.toList())
    print("Here is the stuff:\n")
    print(p.data[product_index]['ProductName'])
    print(p.data[product_index]['ProductDescription'])
    print(p.data[product_index]['ProductPrice'])
    print(p.data[product_index]['ProductStock'])

if result == 2: #update
    p = product()
    p.getAll()
    product_index = makeMenu('Select Product', p.toList())
    p_index = p.data[product_index]['ProductID']
    print(f"product index: {product_index}")
    # for field in p.fields:
        # p.data[product_index][field] = input(f"Enter {field}: ")

    p.data[product_index]['ProductName'] = input('Enter Product Name: ')
    p.data[product_index]['ProductDescription'] = input('Enter Product Description: ')
    p.data[product_index]['ProductPrice'] = input('Enter Product Price: ')
    p.data[product_index]['ProductStock'] = input('Enter Product Stock: ')
    p.update(product_index)

if result == 3: #delete
    p = product()
    p.getAll()
    product_index = makeMenu('Select Product', p.toList())
    p_index = p.data[product_index]['ProductID']
    p.deleteById(p_index) #delete record by id
    print("Deleted product with id: " + str(p_index))