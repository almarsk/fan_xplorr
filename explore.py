import fire
import json
from pyvis.network import Network
import utils
import os


def make_graph(selection, hub):
    data = utils.unpack_data()
    net = Network(notebook=True, cdn_resources='in_line')
    utils.add_nodes(net, selection, data)
    net.repulsion(node_distance=100, spring_length=200)
    hub_or_cue = lambda b: "hub" if b else "cue"
    if not os.path.exists("graphs"):
        os.makedirs("graphs")
    return net.show(f'graphs/{filename()}_{hub_or_cue(hub)}.html')


def filename(new_name=""):
    with open("config.json", "r+") as j:
        config = json.load(j)
        config["filename"] = new_name or config["filename"]
        j.seek(0)
        json.dump(config, j)
        print("\nTo change the destination filename, follow up this command with the desired name.")
        print("Current filename:")
        return config['filename']


def new_graph(*selection):
    if len(selection) == 0:
        return """__________________________________________________________________
Function 'make' creates a network graph in the 'graphs' directory:

        Follow the command up by words you want
        to be a part of the graph seperated by space.
__________________________________________________________________
"""
    selection = utils.make_selection(selection)
    make_graph(selection, hub=True)
    # make_graph(selection, hub=False)


if __name__ == '__main__':
    fire.Fire({
        "name": filename,
        "make": new_graph,
    })
