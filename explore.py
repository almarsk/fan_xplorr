import fire
import json
from pyvis.network import Network
from utils import make_selection
from make_nodes import make_nodes


def add_nodes(net, selection):
    x = 1
    input_nodes = make_nodes(selection)
    for name in make_nodes(selection):
        net.add_node(x,
                     label=name,
                     color=input_nodes[name]["color"],
                     size=5,
                     shape=input_nodes[name]["shape"]),
        x += 1


def add_edges():
    print("add edges")


def make_graph(selection, hub):
    make_nodes(selection)
    # set up a network graph
    net = Network(notebook=True, cdn_resources='in_line')
    add_nodes(net, selection)
    add_edges()

    hub_or_cue = lambda b: "hub" if b else "cue"
    net.repulsion(node_distance=100, spring_length=200)
    return net.show(f'graphs/{filename()}_{hub_or_cue(hub)}.html')


def new_graph(*selection):
    selection = make_selection(selection)
    make_graph(selection, hub=True)
    # make_graph(selection, hub=False)


def filename(new_name=""):

    with open("config.json", "r") as j:
        config = json.load(j)
        config["filename"] = new_name or config["filename"]

    with open("config.json", "w") as j:
        json.dump(config, j)

        print("current filename:")
        return config['filename']


if __name__ == '__main__':
    fire.Fire({
        "new": new_graph,
        "name": filename,
    })

