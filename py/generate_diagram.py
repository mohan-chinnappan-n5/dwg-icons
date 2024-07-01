# generate_diagram.py

import argparse
from diagrams import Diagram, Cluster
from icon_definitions import get_icons
import os

def parse_connections(connections, icons):
    for connection in connections:
        nodes = connection.split(' >> ')
        for i in range(len(nodes) - 1):
            icons[nodes[i]] >> icons[nodes[i + 1]]

def main(output_filename, direction, title, cluster_name, connections):
    outformat = os.path.splitext(output_filename)[1][1:]  # Extract the file extension without the dot
    
    if not outformat:
        raise ValueError("Output filename must have an extension indicating the format (e.g., 'diagram.png').")

    with Diagram(title, show=False, filename=os.path.splitext(output_filename)[0], direction=direction, outformat=outformat):
        sf_st, sf_sit, sf_uat, sf_staging, sf_PROD, dev_int, QA_int, PROD_int = get_icons()
        
        icons = {
            "sf_st": sf_st,
            "sf_sit": sf_sit,
            "sf_uat": sf_uat,
            "sf_staging": sf_staging,
            "sf_PROD": sf_PROD,
            "dev_int": dev_int,
            "QA_int": QA_int,
            "PROD_int": PROD_int
        }

        with Cluster(cluster_name):
            parse_connections(connections, icons)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a diagram with custom icons")
    parser.add_argument("--output_filename", type=str, required=True, help="The output filename with extension (e.g., 'diagram.png')")
    parser.add_argument("--direction", type=str, default="LR", choices=["LR", "TB", "BT", "RL"], help="The direction of the diagram (LR: Left to Right, TB: Top to Bottom, BT: Bottom to Top, RL: Right to Left)")
    parser.add_argument("--title", type=str, default="Environment", help="The title of the diagram")
    parser.add_argument("--cluster_name", type=str, default="CRM", help="The name of the cluster")
    parser.add_argument("--connections", type=str, nargs='+', help="The connections between nodes")

    args = parser.parse_args()
    main(args.output_filename, args.direction, args.title, args.cluster_name, args.connections)
