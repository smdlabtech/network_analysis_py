import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import itertools

# Fonction pour charger le graphe depuis un fichier GML
def load_graph(file_path):
    return nx.read_gml(file_path, label='id')

# Fonction pour calculer les métriques du graphe
def compute_metrics(G):
    metrics = {
        "Nombre de nœuds": G.number_of_nodes(),
        "Nombre d'arêtes": G.number_of_edges(),
        "Densité": round(nx.density(G), 6),
    }
    return metrics

# Fonction pour détecter les communautés
def detect_communities(G, k=1):
    comp = nx.algorithms.community.centrality.girvan_newman(G)
    for communities in itertools.islice(comp, k):
        return tuple(sorted(c) for c in communities)

# Fonction pour dessiner le graphe
def draw_graph(G):
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=False, node_size=10, edge_color="gray")
    st.pyplot(plt)

# Interface Streamlit
st.title("Analyse de Graphes en Réseau")

# Téléchargement du fichier GML
gml_file = st.file_uploader("Télécharge un fichier .gml", type=["gml"])

if gml_file:
    G = load_graph(gml_file)
    
    # Affichage des métriques
    st.subheader("Métriques du Graphe")
    metrics = compute_metrics(G)
    for key, value in metrics.items():
        st.write(f"**{key}**: {value}")
    
    # Détection de communautés
    if st.button("Détecter les communautés"):
        communities = detect_communities(G, k=1)
        st.write("Nombre de communautés détectées :", len(communities))
    
    # Visualisation du graphe
    st.subheader("Visualisation du Graphe")
    draw_graph(G)
