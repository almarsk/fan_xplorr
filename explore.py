import random
import fire
from pyvis.network import Network

destination_filename = "nodes"

def rand_color():
    random_color = str(random.randint(0, 255))
    return ['hsl(' + random_color + ', 100%, 60%)', 'hsl(' + str(random.randint(0, 255)) + ', 50%, 75%)']


def make_selection(selection):
    return [word.upper() for word in selection]


def make_nodes():
    # make dict of nodes


def add_nodes():
    # use dict of nodes to add to net


def add_edges():
    # based on data create links between nodes at hand


def make_graph(hub, selection):
    make_nodes()
    # set up a network graph
    net = Network(notebook=True, cdn_resources='in_line')
    add_nodes()
    add_edges()
    hub_or_cue = lambda b: "hub" if b else "cue"
    return net.show(f'graphs/{destination_filename}_{hub_or_cue(hub)}.html')


def new_graph(*selection):
    selection = make_selection(selection)
    make_graph(True, selection)
    make_graph(False, selection)


def config_filename(name):
    global destination_filename
    if name is not None:
        destination_filename = name
    return f"current destination filename is {destination_filename}"


if __name__ == '__main__':
    fire.Fire({
        "new": new_graph,
        "name": config_filename,
    })
