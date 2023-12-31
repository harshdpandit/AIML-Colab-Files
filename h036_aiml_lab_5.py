# -*- coding: utf-8 -*-
"""H036 AIML Lab 5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kLn1WOv1_f8t9RNRYEEee3SmsFdekYvO

Aim: To implement BFS algorithm using python/matlab.
"""

#---------------------------------------------------------------------------------------
#Harsh Pandit
#H036
root_node=int(input("Enter the value of root node: "))
queue=[]
list_node_values=[]
list_node_values.append(root_node)
search_tree={}
#the BFS algorithm-->
def search_goal_node(goal_node,list_node_values,queue):
  for node_value in list_node_values :
     if goal_node not in queue:
       queue.append(node_value)

def get_goal_node():
  return(int(input('Enter the value of goal node: ')))

#forms a new node in search tree
def form_node(parent_node,search_tree):
  successor_nodes=[]
  print('You are giving successor node for node {}'.format(parent_node))
  print_statement='Please enter the value of successor.'
  print_statement+=' Double Press space bar to stop'
  cond_value='random_value'
  while cond_value != '  ':
    print(print_statement)
    cond_value=input()
    if cond_value != '  ':
      cond_value=int(cond_value)
      successor_nodes.append(cond_value)
      list_node_values.append(cond_value)
  search_tree[parent_node]=successor_nodes

for node_values in list_node_values:
  form_node(node_values,search_tree)
print('The search tree is: ')
print(search_tree)

goal_node=get_goal_node()
while goal_node not in list_node_values:
  print('Goal node not present in search tree')
  goal_node=get_goal_node()

search_goal_node(goal_node,list_node_values,queue)
print('The search path using BFS is: ')
print(queue)

