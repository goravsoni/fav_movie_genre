# fav_movie_genre.py
# Gorav Soni
# 5.2.19
# CS 101 Assignment 4
# takes data from a file and using a class structure prints out the data in
# a specified order

group_e = []
group_m = []
group_h = []
group_c = []

class Student:
    def __init__(self, name, age, genre):
        self.name = name
        self.age = age
        self.genre = genre

    def set_name(self,name):
        self.name = name
    def set_age(self,age):
        self.age = age
    def set_movie_genre(self,genre):
        self.genre = genre
    def find_fav_genre(self, entry, group_data):
        count_likes_action = 0
        count_likes_scifi = 0
        count_likes_comedy = 0
        count_likes_history = 0
        if entry == 'E' or entry == 'M' or entry == 'H' or entry == 'C':
            for k in range(len(group_data)):
                if group_data[k][2] == 'Like':
                    count_likes_action += 1
                if group_data[k][3] == 'Like':
                    count_likes_scifi += 1
                if group_data[k][4] == 'Like':
                    count_likes_comedy += 1
                if group_data[k][5] == 'Like':
                    count_likes_history += 1
        if count_likes_action > count_likes_scifi and count_likes_action > count_likes_comedy \
                and count_likes_action > count_likes_history:
            print('Favorite Movie Genre: Action')

        if count_likes_scifi > count_likes_action and count_likes_scifi > count_likes_comedy \
                and count_likes_scifi > count_likes_history:
            print('Favorite Movie Genre: Scifi')

        if count_likes_comedy > count_likes_scifi and count_likes_comedy > count_likes_action \
                and count_likes_comedy > count_likes_history:
            print('Favorite Movie Genre: Comedy')

        if count_likes_history > count_likes_scifi and count_likes_history > count_likes_action \
                and count_likes_history > count_likes_comedy:
            print('Favorite Movie Genre: History')

    def calc_percentage_genre(self, entry, group_data):
        count_likes_action = 0
        count_likes_scifi = 0
        count_likes_comedy = 0
        count_likes_history = 0
        if entry == 'E' or entry == 'M' or entry == 'H' or entry == 'C':
            for k in range(len(group_data)):
                if group_data[k][2] == 'Like':
                    count_likes_action += 1
                if group_data[k][3] == 'Like':
                    count_likes_scifi += 1
                if group_data[k][4] == 'Like':
                    count_likes_comedy += 1
                if group_data[k][5] == 'Like':
                    count_likes_history += 1

        length_group = len(group_data)
        scifi_percentage = float(count_likes_scifi / length_group * 100)
        comedy_percentage = float(count_likes_comedy / length_group * 100)
        history_percentage = float(count_likes_history / length_group * 100)
        action_percentage = float(count_likes_action / length_group * 100)
        print("% of students who like Scifi = ", format(scifi_percentage, '.1f'),"%", sep = '')
        print("% of students who like Action = ", format(action_percentage, '.1f'), "%", sep = '')
        print("% of students who like Comedy = ", format(comedy_percentage, '.1f'), "%", sep = '')
        print("% of students who like History = ", format(history_percentage, '.1f'), "%", sep = '')

    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_movie_genre(self):
        return self.genre


def main():
    group_e = []
    group_m = []
    group_h = []
    group_c = []
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
        elif int(slist[i][1]) in range(10, 15):
            group_m.append(slist[i])
        elif int(slist[i][1]) in range(15, 19):
            group_h.append(slist[i])
        elif int(slist[i][1]) in range(19, 23):
            group_c.append(slist[i])
    name = ''
    age = 0
    genre = ''
    survey = Student(name, age, genre)

    entry = 'E'
    print("Age Group: E")
    survey.find_fav_genre(entry, group_e)
    survey.calc_percentage_genre(entry, group_e)
    print('\n')

    entry = 'M'
    print("Age Group: M")
    survey.find_fav_genre(entry, group_m)
    survey.calc_percentage_genre(entry, group_m)
    print('\n')

    entry = 'H'
    print("Age Group: H")
    survey.find_fav_genre(entry, group_h)
    survey.calc_percentage_genre(entry, group_h)
    print('\n')

    entry = 'C'
    print("Age Group: C")
    survey.find_fav_genre(entry, group_c)
    survey.calc_percentage_genre(entry, group_c)

main()
