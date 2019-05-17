# bar_graph_group_h.py
# Gorav Soni
# 5.2.19
# CS 101 Assignment 4 EC
# takes data from a file and using the matplotlib creates a bar graph
# for group h.

import matplotlib.pyplot as plt

def main():
    group_h = []
    movie_genre= ['Action', 'Science Fiction', 'Comedy', 'History']
    group_h_action = []
    group_h_percentage = []
    group_h_scifi = []
    group_h_percentage_scifi = []
    group_h_comedy = []
    group_h_percentage_comedy= []
    group_h_history = []
    group_h_percentage_history = []
    fin = open("data.txt", 'r')
    data = fin.readline()
    slist = []
    while (data):
        data = data.strip().split(';')
        slist.append(data)
        data = fin.readline()
    for i in range(15):
        if int(slist[i][1]) in range(15, 19):
            group_h.append(slist[i])


    fig = plt.figure(figsize=(7, 5))

    for data in range(len(group_h)):
        if group_h[data][2] == 'Like':
            group_h_action.append(group_h[data][2])
    for data in range(len(group_h)):
        if group_h[data][3] == 'Like':
            group_h_scifi.append(group_h[data][3])

    for data in range(len(group_h)):
        if group_h[data][4] == 'Like':
            group_h_comedy.append(group_h[data][4])

    for data in range(len(group_h)):
        if group_h[data][5] == 'Like':
            group_h_history.append(group_h[data][5])

    group_h_percentage_action = len(group_h_action)/12 * 100
    group_h_percentage.append(group_h_percentage_action)
    group_h_percentage_scifi = len(group_h_scifi) / 12 * 100
    group_h_percentage.append(group_h_percentage_scifi)
    group_h_percentage_comedy = len(group_h_comedy) / 12 * 100
    group_h_percentage.append(group_h_percentage_comedy)
    group_h_percentage_history = len(group_h_history) / 12 * 100
    group_h_percentage.append(group_h_percentage_history)


    positions = [0,1,2,3]
    plt.bar(positions, group_h_percentage, width = 0.5, color = 'green')
    plt.xticks(positions, movie_genre)
    plt.title("Favorite Movie Genre in High School")
    plt.ylabel("Percentage")
    plt.xlabel("n = 4 Students")
    print(group_h)
    plt.show()



main()
