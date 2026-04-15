from rdflib import Graph, URIRef
from obse.graphwrapper import GraphWrapper


def test_01():
    graph = Graph()
    graph_wrapper = GraphWrapper(graph, "https://www.frittenburger.de/test")
    instance_type = URIRef("https://www.frittenburger.de/test#TestClass")
    instance = graph_wrapper.add_named_instance(instance_type, "test-instance")

    assert len(graph) == 2
    assert (instance, None, None) in graph
    assert (instance, URIRef("http://www.w3.org/2000/01/rdf-schema#label"), None) in graph
