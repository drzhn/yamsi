# -*- coding: utf-8 -*-
from graph_tool.all import *
from lastfm_graphs.LastAPI import similar_artists
from lastfm_graphs.Last2neo import last2neo

API_KEY = "6d44fe32b4be725146401adc08001305"
API_SECRET = "af1f7ec4eb7d3ab8b9580972d95ff604"


# sim = get_lastfm.similar_artists("mr. Kitty", API_KEY)
# for i in sorted(sim.keys()):
#     print(sim[i])

# g = Graph(directed=False)
# artist_graph = {}
# artist_map = g.new_vertex_property("string")


# def SimilarityGraph_tool(artist_graph, artist_list, step):
#     for artist in artist_list:
#         if not artist in artist_graph.keys():
#             artist_graph[artist] = g.add_vertex()
#             artist_map[artist_graph[artist]] = artist
#
#         sim = similar_artists(artist, API_KEY)
#         temp = []
#         for i in sim.keys():
#             if sim[i] in artist_graph.keys():
#                 g.add_edge(artist_graph[artist], artist_graph[sim[i]])
#             else:
#                 if i > 0.8:
#                     artist_graph[sim[i]] = g.add_vertex()
#                     artist_map[artist_graph[sim[i]]] = sim[i]
#                     for k in range(step):
#                         print("  ", end="")
#                     print(sim[i])
#                     g.add_edge(artist_graph[artist], artist_graph[sim[i]])
#                     temp.append(sim[i])
#         if step > 0:
#             SimilarityGraph_tool(artist_graph, temp, step - 1)
#     return


def SimilarityGraph_neo(graph, name, step, threshold=0.5):
    global artist_list
    if not name in artist_list:
        artist_list.append(name)
        graph.create_artist(name)

    sim = similar_artists(name, API_KEY)
    temp = []
    for i in sim.keys():
        if sim[i] in artist_list:
            if i > threshold:
                graph.create_rel(name, sim[i], i)
        else:
            if i > threshold:
                artist_list.append(sim[i])
                graph.create_artist(sim[i])
                for k in range(step):
                    print("  ", end="")
                print(sim[i])
                graph.create_rel(name, sim[i], i)
                temp.append(sim[i])
    if step > 0:
        for t in temp:
            SimilarityGraph_neo(graph, t, step - 1, threshold)
    return


# g = Graph()
# v1 = g.add_vertex()
# v2 = g.add_vertex()
# e = g.add_edge(v1, v2)
# string_map = g.new_vertex_property("string")
# string_map[v1] = "first"
# string_map[v2] = "second"
# print(type(g.vertex_index))

artists = []
f = open("../get_music/audiolists/97333924", "r")
for artist in f.readlines():
    artist = artist[:-1].replace("&amp;", "&")
    if not artist[:-1].replace("&amp;", "&") in artists:
        artists.append(artist)

g = last2neo()
artist_list = []
# SimilarityGraph_neo(g, "Mr.Kitty", 1, 0.5)
for i in range(10000):
    g.check_if_exists("sdfsdf")
# SimilarityGraph(artist_graph, ["Mr.Kitty"], 2)
# g.save("my_graph.xml.gz")
# g.load("my_graph.xml.gz")
# graph_draw(g, vertex_text=artist_map, vertex_font_size=10, output_size=(4000, 4000), output="two-nodes.png")
