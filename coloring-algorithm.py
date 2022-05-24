
def greedy_coloring(graph_nodes: list, graph_size: int):

    available_colors = ["RED", "GREEN", "BLUE", "WHITE", "YELLOW", "ORANGE", "PURPLE"]
    nodes_colors = {}
    
    """
      A  B  C  D  E  F  G   
    A 0  1  0  0  1  0  1  
    B 1  0  1  0  0  0  0 
    C 0  1  0  1  0  0  1  
    D 0  0  1  0  1  1  0
    E 1  0  0  1  0  0  0
    F 0  0  0  1  0  0  0
    G 1  0  1  0  0  0  0
    """

    for index, i in enumerate(graph_nodes, start=0):
        node_char = chr(index+65)
        node_color = None
        neighbor_colors = []

        print(f"-------------- Node {node_char} --------------")

        if len(nodes_colors.keys()) == 0:
            # this is the first node
            node_color = available_colors[0]

        elif node_char not in nodes_colors.keys():
            for iindex, ii in enumerate(i, start=0):
                node_ii_char = chr(iindex+65)
                if iindex != index and ii == 1 and node_ii_char in nodes_colors.keys():
                    neighbor_colors.append(nodes_colors[node_ii_char])

            used_colors = set(nodes_colors.values())
            neighbor_colors = set(neighbor_colors)
            can_use_colors = used_colors - neighbor_colors

            if len(can_use_colors) == 0:
                node_color = (list(set(available_colors)-neighbor_colors))[0]
            else:
                node_color = (list(can_use_colors))[0]

        nodes_colors[node_char] = node_color

        print("Neighbor Colors", neighbor_colors)
        print("Nodes Colors", nodes_colors)

    return set(nodes_colors.values())


if __name__ == '__main__':
    # First example
    result = greedy_coloring(
        [
            [0, 1, 1, 1],
            [1, 0, 1, 0],
            [1, 1, 0, 0],
            [1, 0, 0, 0],
        ], 4)

    # Second Example
    # result = greedy_coloring(
    #     [
    #         [0, 1, 1, 1, 0],
    #         [1, 0, 1, 0, 0],
    #         [0, 1, 0, 1, 1],
    #         [0, 0, 1, 0, 1],
    #         [1, 0, 1, 1, 0],
    #     ], 5)


    print("\n------------------ Result ------------------")
    print(f"Chromatic number = {len(result)}")
    print(f"Chromatic values = {result}")
