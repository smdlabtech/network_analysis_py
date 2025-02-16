
# 📊 Analyse des Réseaux - Co-Auteurs Scientifiques  
![Network Analysis](https://img.shields.io/badge/Network_Analysis-Graph_Theory-blue?style=flat&logo=graphviz)
![Machine Learning](https://img.shields.io/badge/Machine_Learning-LLM-orange?style=flat&logo=ai)
![Data Science](https://img.shields.io/badge/Data_Science-Graph_Analytics-green?style=flat&logo=python)
![AI](https://img.shields.io/badge/AI-Graph_Neural_Networks-blueviolet?style=flat&logo=OpenAI)
![Research](https://img.shields.io/badge/Research-Scientometrics-orange?style=flat&logo=google-scholar)
![Big Data](https://img.shields.io/badge/Big_Data-Network_Visualization-red?style=flat&logo=databricks)

---

## 🔍 Présentation  

Cette étude porte sur le **réseau de co-auteurs** des scientifiques travaillant sur la **théorie et l'expérience des réseaux**.  

📌 **Sources des données**  
- 📖 *SIAM Review*, Vol. 45, pp. 167-256 (2003)  
- 📖 *Physics Reports*, Vol. 424, pp. 175-308 (2006)  
- 📚 **Données enrichies** par des références supplémentaires ajoutées **manuellement**  

📌 **Nature du réseau**  
- 📎 **Type** : Réseau de co-auteurs scientifiques  
- 🔗 **Propriétés** : Graphes pondérés (liens basés sur les co-publications)  
- ⚖️ **Modèle utilisé** : Graph Theory, PageRank, Graph Neural Networks (GNNs)  

---

## 📈 Objectifs de l'Analyse  

🎯 **Explorer la structure du réseau** → Identification des clusters et des hubs scientifiques  
🎯 **Analyser les liens de collaboration** → Détection des partenariats clés  
🎯 **Identifier les auteurs influents** → Algorithme **PageRank** et **centralité des nœuds**  
🎯 **Étudier la connectivité et la densité du réseau** → Métriques : degré moyen, diamètre du graphe  
🎯 **Visualiser les communautés et collaborations** → Algorithmes de détection de communautés (**Louvain**, **K-Means**, **Spectral Clustering**)  

---

## 📂 Méthodologie & Pipeline d'Analyse  

```bash
📦 network-analysis-project
 ┣ 📂 data
 ┃ ┣ 📜 coauthors_network.csv        # Données brutes du réseau
 ┃ ┣ 📜 preprocessed_network.gexf    # Fichier pré-traité (Graph format)
 ┣ 📂 notebooks
 ┃ ┣ 📜 1_data_cleaning.ipynb        # Nettoyage des données
 ┃ ┣ 📜 2_network_analysis.ipynb     # Analyse des métriques
 ┃ ┣ 📜 3_visualization.ipynb        # Graphes interactifs avec NetworkX
 ┣ 📂 models
 ┃ ┣ 📜 gnn_model.pth                # Modèle GNN entraîné pour prédiction
 ┣ 📂 results
 ┃ ┣ 📜 network_graph.html           # Visualisation interactive (D3.js)
 ┣ 📜 README.md                      # Documentation
 ┣ 📜 requirements.txt                # Dépendances Python
 ┣ 📜 LICENSE                        # Licence du projet
```
