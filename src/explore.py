import fire
import json
from pyvis.network import Network
import utils
import os


def make_graph(selection, file, data, hub):
    net = Network(notebook=True, cdn_resources='in_line')
    utils.add_nodes(net, selection, data)
    net.repulsion(node_distance=150, spring_length=200)
    hub_or_cue = lambda b: "hub" if b else "cue"
    html = net.generate_html()
    dest = f'graphs/{file}_{hub_or_cue(hub)}.html'
    print(dest)
    with open(dest, mode='w', encoding='utf-8') as fp:
            fp.write(html)


def filename(new_name=""):
    "shows and edits name of destination file"
    with open("config.json", "r+") as j:
        config = json.load(j)
        config["filename"] = new_name or config["filename"]
        j.seek(0)
        j.truncate(0)
        json.dump(config, j)
        print("Current filename:")
        return config['filename']


def new_graph(*selection):
    """makes a new graph, try python explore.py make play"""
    if len(selection) == 0:
        return """       __________________________________________________________________
     ||./xplor creates a network graph in the 'graphs' directory:        ||
     ||Follow the command up by words you want to be a part of the graph.||
     ||They just need to be seperated by space.                          ||
     ||To change the name of desination file, run ./rnm                  ||
      __________________________________________________________________
"""
    selection = utils.make_selection(selection)
    if not os.path.exists("graphs"):
        os.makedirs("graphs")
    file = filename()
    data = utils.unpack_data()
    colors = utils.hub_colors(selection)
    make_graph(utils.make_nodes_h(selection, data, colors), file, data, hub=True)
    make_graph(utils.make_nodes_c(selection, data, colors, hub=False), file, data, hub=False)
    utils.combine_html_files(f"{file}_hub.html",f"{file}_cue.html", f"{file}_both.html")


if __name__ == '__main__':
    fire.Fire({
        "make": new_graph,
        "name": filename,
    })
