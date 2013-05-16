
import pydot

def makeDisjoinsetGraph(partition_set):
    graphviz = pydot.Dot(graph_type='digraph')

    for n in partition_set.values():
        graphviz.add_node(pydot.Node(str(n.data)))

    for n in partition_set.values():
        graphviz.add_edge(pydot.Edge(pydot.Node(str(n.data)), pydot.Node(str(n.parent.data))))

    graphviz.write_png('disjoinset_graph.png')

def tupleToString(tuple):
    string = ""
    first = True
    for i in range(0, len(tuple) % 10):
        if tuple[i] != None:
            if first: first = False
            else: string += ", "
            string += str(tuple[i])

    if len(tuple) > 10:
        string += " and " + str(len(tuple)-1) + " others"
    return string

def printCondensedGraph(condensedFromSet):
    graphviz = pydot.Dot(graph_type='digraph')
    graphviz_nodes = {}

    for n in condensedFromSet.nodes():
        print_node = pydot.Node(tupleToString(n))
        graphviz.add_node(print_node)
        graphviz_nodes[n] = print_node


    for e in condensedFromSet.edges():
        graphviz.add_edge(pydot.Edge(graphviz_nodes[e[0]], graphviz_nodes[e[1]]))

    graphviz.write_png('condensed_graph.png')