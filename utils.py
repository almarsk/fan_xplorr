import random
import json
from typing_extensions import Counter


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
    edges = []
    for key, item in input_nodes.items():
        # print(key, item['id'])
        if item['prio'] == 'main':
            for cue in item['cues']:
                edges.append((item['id'], input_nodes[cue]['id']))
        elif item['prio'] == 'cue':
            if key in data:
                for key2 in input_nodes:
                    if key2 in data[key]:
                        edges.append((item['id'], input_nodes[key2]['id']))
    return edges


def make_nodes(selection, data):
    input_nodes = {}
    id_count = 1
    for node in selection:
        if node in data:
            cues = data[node]
            color = rand_color()
            input_nodes[node] = dict()
            input_nodes[node]['id'] = id_count
            id_count += 1
            input_nodes[node]["name"] = node
            input_nodes[node]["prio"] = "main"
            input_nodes[node]["shape"] = "dot"
            input_nodes[node]["color"] = color[0]
            input_nodes[node]["cues"] = cues

            for cue in cues:
                if cue not in input_nodes:
                    input_nodes[cue] = dict()
                    input_nodes[cue]['id'] = id_count
                    id_count += 1
                    input_nodes[cue]["name"] = cue
                    input_nodes[cue]["prio"] = "cue"
                    input_nodes[cue]["shape"] = "dot"
                    input_nodes[cue]["color"] = color[1]

    return input_nodes


def add_nodes(net, selection, data):
    input_nodes = make_nodes(selection, data)
    value = 5
    for name in input_nodes:
        if name in data:
            value = len(data[name])

        net.add_node(input_nodes[name]['id'],
                        label=name,
                        color=input_nodes[name]["color"],
                        size= map_values(value, 1, 324, 5, 60),
                        shape=input_nodes[name]["shape"]
        )
    net.add_edges(get_edges(input_nodes, data))


def map_values(value, in_min, in_max, out_min, out_max):
    return int((value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)


    """value = 100
    mapped_value = map_values(value, 1, 324, 5, 15)
    print(mapped_value)"""
