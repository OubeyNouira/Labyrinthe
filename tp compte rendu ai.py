import turtle
import random
from collections import deque
class Labyrinthe:
    def __init__(self):
        self.nodes = []
        self.arcs = []

    def ajouterNoeud(self, node):
        self.nodes.append(node)

    def ajouterArc(self, arc):
        self.arcs.append(arc)
def listerNoeuds(self):
      return list(self.graph.keys())

class File:
  def __init__(self):
    self.elements = deque()
  def file_vide(self):
    return len(self.elements) == 0
  def enfiler(self, element):
    self.elements.append(element)
  def defiler(self):
    if not self.file_vide():
      return self.elements.popleft()
    else:
      print("La file est vide.")
  def taille_file(self):
    return len(self.elements)
class Pile:
  def __init__(self):
    self.elements = deque()
  def pile_vide(self):
    return len(self.elements) == 0
  def empiler(self, element):
    self.elements.append(element)
  def depiler(self):
    if not self.pile_vide():
      return self.elements.pop()
    else:
      print("La pile est vide.")
  def taille_pile(self):
    return len(self.elements)

def listerArcs(self):
      edges = []
      for node,arcs in self.graph:
              edges.append(arcs)
      return edges


def listerArcs(self, node):
      if node in self.graph:
        return self.graph.get(node,[])
def AfficherGraphe(self):
      for node in self.graph:
          print(f"{node} -> {self.graph[node]}")    
def Afficher_labyrinth(labyrinthe):
    screen = turtle.Screen()
    screen.setup(width=600, height=600)
    screen.setworldcoordinates(0, 0, 15, 15)

    pen = turtle.Turtle()
    pen.speed(0)
    pen.penup()
    pen.color("black")

    # Draw nodes
    for node in labyrinthe.nodes:
        pen.goto(node[0], node[1])
        pen.dot(5)

    # Draw arcs
    pen.pendown()
    for arc in labyrinthe.arcs:
        start = arc[0]
        end = arc[1]
        traversable = arc[2]
        if not traversable:  # If the arc is not traversable
            pen.penup()
            pen.goto(start[0], start[1])
            pen.pendown()
            pen.goto(end[0], end[1])

    pen.hideturtle()

def search_path(labyrinthe):
    start_node = random.choice(labyrinthe.nodes)
    current_node = start_node
    
    pen = turtle.Turtle()
    pen.speed(0)
    pen.penup()
    pen.color("red")
    pen.goto(start_node[0], start_node[1])
    pen.pendown()
    pen.begin_fill()
    
    while True:
        neighbors = []
        for node in labyrinthe.nodes:
            if (node[0] == current_node[0] + 1 and node[1] == current_node[1]) or \
               (node[0] == current_node[0] - 1 and node[1] == current_node[1]) or \
               (node[0] == current_node[0] and node[1] == current_node[1] + 1) or \
               (node[0] == current_node[0] and node[1] == current_node[1] - 1):
                neighbors.append(node)
        
        # Choose a random neighbor
        next_node = random.choice(neighbors)
        
        # Check existance du porte
        for arc in labyrinthe.arcs:
            if (arc[0] == current_node and arc[1] == next_node) or \
               (arc[0] == next_node and arc[1] == current_node):
                if arc[2]:  # If porte passable 
                    pen.goto(next_node[0], next_node[1])
                    current_node = next_node
                    break
        else:  # s'il ya un port passer a un autre neighbord
            continue
        
        # Check si l current woslet l node fel edge walle 
        if (current_node[0] == 0 or current_node[0] == 14 or current_node[1] == 0 or current_node[1] == 14) and \
           all((arc[0] != current_node and arc[1] != current_node) or arc[2] for arc in labyrinthe.arcs):
            pen.goto(current_node[0], current_node[1])
            break
    
    pen.end_fill()


labyrinthe = Labyrinthe()

# definition du taille 
tailledulabyrinthe = 10

# random labyrinth
def generation_labyrinthe_random(tailledulabyrinthe):
    for i in range(tailledulabyrinthe):
        for j in range(tailledulabyrinthe):
            node = (i, j)
            labyrinthe.ajouterNoeud(node)
            if i < tailledulabyrinthe - 1 and j < tailledulabyrinthe - 1:
                labyrinthe.ajouterArc(((i, j), (i + 1, j), random.choice([True, False])))
                labyrinthe.ajouterArc(((i, j), (i, j + 1), random.choice([True, False])))

# Generation du labyrinthe
generation_labyrinthe_random(tailledulabyrinthe)
# display du labyrinth
Afficher_labyrinth(labyrinthe)
# el Search w rasm el path 
search_path(labyrinthe)
turtle.done()
