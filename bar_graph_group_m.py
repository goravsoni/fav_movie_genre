# bar_graph_group_m.py
# Gorav Soni
# 5.2.19
# CS 101 Assignment 4 EC
# takes data from a file and using the matplotlib creates a bar graph
# for group m.

import matplotlib.pyplot as plt

def main():
    group_m = []
    movie_genre= ['Action', 'Science Fiction', 'Comedy', 'History']
    group_m_action = []
    group_m_percentage = []
    group_m_scifi = []
    group_m_percentage_scifi = []
    group_m_comedy = []
    group_m_percentage_comedy= []
    group_m_history = []
    group_m_percentage_history = []
    fin = open("data.txt", 'r')
    data = fin.readline()
    slist = []
    while (data):
        data = data.strip().split(';')
        slist.append(data)
        data = fin.readline()
    for i in range(15):
        if int(slist[i][1]) in range(10, 15):
            group_m.append(slist[i])


    fig = plt.figure(figsize=(7, 5))

    for data in range(len(group_m)):
        if group_m[data][2] == 'Like':
            group_m_action.append(group_m[data][2])
    for data in range(len(group_m)):
        if group_m[data][3] == 'Like':
            group_m_scifi.append(group_m[data][3])

    for data in range(len(group_m)):
        if group_m[data][4] == 'Like':
            group_m_comedy.append(group_m[data][4])

    for data in range(len(group_m)):
        if group_m[data][5] == 'Like':
            group_m_history.append(group_m[data][5])

    group_m_percentage_action = len(group_m_action)/12 * 100
    group_m_percentage.append(group_m_percentage_action)
    group_m_percentage_scifi = len(group_m_scifi) / 12 * 100
    group_m_percentage.append(group_m_percentage_scifi)
    group_m_percentage_comedy = len(group_m_comedy) / 12 * 100
    group_m_percentage.append(group_m_percentage_comedy)
    group_m_percentage_history = len(group_m_history) / 12 * 100
    group_m_percentage.append(group_m_percentage_history)


    positions = [0,1,2,3]
    plt.bar(positions, group_m_percentage, width = 0.5, color = 'green')
    plt.xticks(positions, movie_genre)
    plt.title("Favorite Movie Genre in Middle School")
    plt.ylabel("Percentage")
    plt.xlabel("n = 3 Students")
    print(group_m)
    plt.show()



main()
