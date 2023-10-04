from flask import Flask, render_template, request, redirect, url_for
import networkx as nx
import matplotlib.pyplot as plt

app = Flask(__name__)

# Initialize a NetworkX graph
graph = nx.Graph()

@app.route('/')
def index():
    people = graph.nodes()
    return render_template('input_relationship.html', people=people)

@app.route('/add_relationship', methods=['POST'])
def add_relationship():
    from_person_name = request.form.get('from_person')
    to_person_name = request.form.get('to_person')

    if from_person_name and to_person_name:
        graph.add_node(from_person_name)
        graph.add_node(to_person_name)
        graph.add_edge(from_person_name, to_person_name)

    return redirect(url_for('index'))

@app.route('/visualize_network')
def visualize_network():
    visualize_social_network(graph)
    return render_template('visualize_network.html')

def visualize_social_network(graph):
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_color='skyblue', node_size=800, font_size=10, font_color='black')
    plt.title("Social Network Graph")
    plt.axis('off')
    plt.savefig('static/network.png')
    plt.close()

if __name__ == '__main__':
    app.run(debug=True)
