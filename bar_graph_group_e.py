# bar_graph_group_e.py
# Gorav Soni
# 5.2.19
# CS 101 Assignment 4 EC
# takes data from a file and using the matplotlib creates a bar graph
# for group e.

import matplotlib.pyplot as plt

def main():
    group_e = []
    movie_genre= ['Action', 'Science Fiction', 'Comedy', 'History']
    group_e_action = []
    group_e_percentage = []
    group_e_scifi = []
    group_e_percentage_scifi = []
    group_e_comedy = []
    group_e_percentage_comedy= []
    group_e_history = []
    group_e_percentage_history = []
    fin = open("data.txt", 'r')
    data = fin.readline()
    slist = []
    while (data):
        data = data.strip().split(';')
        slist.append(data)
        data = fin.readline()
    for i in range(15):
        if int(slist[i][1]) in range(5, 10):
            group_e.append(slist[i])

    fig = plt.figure(figsize=(7, 5))

    for data in range(len(group_e)):
        if group_e[data][2] == 'Like':
            group_e_action.append(group_e[data][2])
    for data in range(len(group_e)):
        if group_e[data][3] == 'Like':
            group_e_scifi.append(group_e[data][3])

    for data in range(len(group_e)):
        if group_e[data][4] == 'Like':
            group_e_comedy.append(group_e[data][4])

    for data in range(len(group_e)):
        if group_e[data][5] == 'Like':
            group_e_history.append(group_e[data][5])

    group_e_percentage_action = len(group_e_action)/12 * 100
    group_e_percentage.append(group_e_percentage_action)
    group_e_percentage_scifi = len(group_e_scifi) / 12 * 100
    group_e_percentage.append(group_e_percentage_scifi)
    group_e_percentage_comedy = len(group_e_comedy) / 12 * 100
    group_e_percentage.append(group_e_percentage_comedy)
    group_e_percentage_history = len(group_e_history) / 12 * 100
    group_e_percentage.append(group_e_percentage_history)


    positions = [0,1,2,3]
    plt.bar(positions, group_e_percentage, width = 0.5, color = 'green')
    plt.xticks(positions, movie_genre)
    plt.title("Favorite Movie Genre in Elementary School")
    plt.ylabel("Percentage")
    plt.xlabel("n = 4 Students")

    plt.show()



main()
