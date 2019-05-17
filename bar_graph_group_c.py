# bar_graph_group_c.py
# Gorav Soni
# 5.2.19
# CS 101 Assignment 4 EC
# takes data from a file and using the matplotlib creates a bar graph
# for group c.

import matplotlib.pyplot as plt

def main():
    group_c = []
    movie_genre= ['Action', 'Science Fiction', 'Comedy', 'History']
    group_c_action = []
    group_c_percentage = []
    group_c_scifi = []
    group_c_percentage_scifi = []
    group_c_comedy = []
    group_c_percentage_comedy= []
    group_c_history = []
    group_c_percentage_history = []
    fin = open("data.txt", 'r')
    data = fin.readline()
    slist = []
    while (data):
        data = data.strip().split(';')
        slist.append(data)
        data = fin.readline()
    for i in range(15):
        if int(slist[i][1]) in range(19, 23):
            group_c.append(slist[i])

    fig = plt.figure(figsize=(7, 5))

    for data in range(len(group_c)):
        if group_c[data][2] == 'Like':
            group_c_action.append(group_c[data][2])
    for data in range(len(group_c)):
        if group_c[data][3] == 'Like':
            group_c_scifi.append(group_c[data][3])

    for data in range(len(group_c)):
        if group_c[data][4] == 'Like':
            group_c_comedy.append(group_c[data][4])

    for data in range(len(group_c)):
        if group_c[data][5] == 'Like':
            group_c_history.append(group_c[data][5])

    group_c_percentage_action = len(group_c_action)/12 * 100
    group_c_percentage.append(group_c_percentage_action)
    group_c_percentage_scifi = len(group_c_scifi) / 12 * 100
    group_c_percentage.append(group_c_percentage_scifi)
    group_c_percentage_comedy = len(group_c_comedy) / 12 * 100
    group_c_percentage.append(group_c_percentage_comedy)
    group_c_percentage_history = len(group_c_history) / 12 * 100
    group_c_percentage.append(group_c_percentage_history)


    positions = [0,1,2,3]
    plt.bar(positions, group_c_percentage, width = 0.5, color = 'green')
    plt.xticks(positions, movie_genre)
    plt.title("Favorite Movie Genre in College")
    plt.ylabel("Percentage")
    plt.xlabel("n = 4 Students")
    print(group_c)
    plt.show()



main()
