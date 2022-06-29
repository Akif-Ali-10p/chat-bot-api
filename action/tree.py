class Node:
  def __init__(self, text = None, reply = None, level = 0):
    if text != None:
        self.text = text
    else:
        self.text = None
    if reply != None:
        self.reply = reply
    else:
        self.reply = None
    self.nodeId = hash(self)
    self.level = level
    self.children = []

# dictionary
global_nodes = {}
def initRun():
    # make global variablles
    global tree
    # import json
    import json
    # read json file.
    file = open("dataset.json")
    dataset = json.load(file)
    # print(data)
    file.close()
    tree = makeTree(dataset, 0)
    print("Dataset loaded, Tree created.")

# make tree from json data
def makeTree(json, lvl):
    # read text and reply from json
    root = Node(text=json["text"], reply=json["reply"], level=lvl)
    global_nodes[root.nodeId] = root
    # check if it has more options/children
    if len(json["option"]) > 0:
        # iterate through options
        for child in json["option"]:
            root.children.append(makeTree(child, lvl+1))
    return root

def printTree(root):
    print(str(root.text[0]) +"==> " + root.reply +" <<= " + str(root.nodeId))
    if len(root.children) > 0:
        # iterate through options
        for child in root.children:
            print("     "*(root.level+1), end="L=>")
            printTree(child)

def getNodeData(id, text):
    print("I got "+str(id) + ", =>" + text)
    if id==-1:
        return {
            'id' : tree.nodeId,
            'reply' : tree.reply
        }
    node = global_nodes.get(id)
    # iterate through child nodes/branches
    for child in node.children:
        # iterate through keywords
        for word in child.text:
            if word in text:
                return {
                    'id' : child.nodeId,
                    'reply' : child.reply        
                }
    # Give user options
    reply = "Sorry, can't find what you're looking for.\nUse these keywords:\n"
    # iterate through child nodes/branches
    for i in range(len(node.children)):
        reply = reply + str(node.children[i].text)[1:-1] + "\n"

    return {
        'id' : id,
        'reply' : reply,
    }





