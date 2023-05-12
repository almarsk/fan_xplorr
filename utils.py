import random
import json


def rand_color():
    rc = str(random.randint(0, 255))
    return ['hsl(' + rc + ', 100%, 60%)', 'hsl(' + rc + ', 50%, 75%)']


def make_selection(selection):
    return [word.upper() for word in selection]


def unpack_data():
    with open("data/UCLFAN_just_words.json", "r") as raw_data:
        data = json.load(raw_data)
    return data


def get_edges(input_nodes, data):
    for key, item in input_nodes.items():
        print(item)
        """# set up edges main
        edges = []
        for index_item, item in enumerate(names):
            self_standing_nodes = []
            if item in data_dict:
                self_standing_nodes.append(item)

            for node in self_standing_nodes:
                if node in data_dict:
                    cues = list(data_dict[node]["associations"].keys())

            for cue in cues:
                if cue in input_nodes:
                    edges.append((list(input_nodes.keys()).index(cue)+1,list(input_nodes.keys()).index(item)+1))
        net.add_edges(edges)"""
    return input_nodes


def make_nodes(selection, data):
    input_nodes = {}
    for node in selection:
        if node in data:
            cues = data[node]
            color = rand_color()
            input_nodes[node] = dict()
            input_nodes[node]["name"] = node
            input_nodes[node]["main"] = "main"
            input_nodes[node]["shape"] = "dot"
            input_nodes[node]["color"] = color[0]
            input_nodes[node]["cues"] = cues

            for cue in cues:
                if cue not in input_nodes:
                    input_nodes[cue] = dict()
                    input_nodes[cue]["name"] = cue
                    input_nodes[cue]["main"] = "cue"
                    input_nodes[cue]["shape"] = "dot"
                    input_nodes[cue]["color"] = color[1]

    return input_nodes


def add_nodes(net, selection, data):
    x = 1
    input_nodes = make_nodes(selection, data)
    for name in input_nodes:
        net.add_node(x,
                        label=name,
                        color=input_nodes[name]["color"],
                        size=5,
                        shape=input_nodes[name]["shape"]
        )
        x += 1


    print(input_nodes)
    # net.add_edges(get_edges(input_nodes, data))
