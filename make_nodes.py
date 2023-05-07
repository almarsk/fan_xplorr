from utils import rand_color
import json

with open("data/UCLFAN_just_words.json", "r") as raw_data:
    data = json.load(raw_data)

    def make_nodes(selection):
        input_nodes = {}

        for node in selection:
            if node in data:
                color = rand_color()
                cues = list(data[node])
                input_nodes[node] = dict()
                input_nodes[node]["name"] = node
                input_nodes[node]["main"] = "main"
                input_nodes[node]["shape"] = "dot"
                input_nodes[node]["color"] = color[0]

                # define cue nodes
                for cue in cues:
                    if cue not in input_nodes:
                        input_nodes[cue] = dict()
                        input_nodes[cue]["name"] = cue
                        input_nodes[cue]["main"] = "cue"
                        input_nodes[cue]["shape"] = "dot"
                        input_nodes[cue]["color"] = color[1]

        return input_nodes
