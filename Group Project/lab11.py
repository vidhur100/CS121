'''
Created on 11/29/2023
@author:   Vidhur Busannagari & Jason Dong
Pledge:    I pledge my honor that I have abided by the Stevens Honor System - VB & JD

CS115 - Lab 11
'''
import os

def get_artists(artists):
    """Gets list of artists from string, standardized"""
    # Jason Dong
    artists = artists.split(',')
    artists = [a.strip().title() for a in artists]
    artists.sort()
    return artists

def save_and_quit(users):
    """Saves user database to file and quits program"""
    # Jason Dong
    with open('database.txt', 'w') as f:
        for user in sorted(users):
            artists = ','.join(users[user])
            f.write(f'{user}:{artists}\n')
    quit()

def enter_preferences(username, users):
    """Gets artist preferences from user and updates database"""
    # Jason Dong
    prefs = []
    while True:
        print("Enter an artist that you like (Enter to finish): ")
        artist = input()
        if artist == '':
            break
        prefs.append(artist.title())
    
    prefs.sort()
    users[username] = prefs
    
def get_recommendations(username, users):
    """Prints artist recommendations for user"""
    # Jason Dong
    most_similar = None
    max_overlap = 0
    for other_user, artists in users.items():
        if other_user == username or other_user.endswith('$'):
            continue
        overlap = len(set(artists) & set(users[username]))
        if overlap > max_overlap and overlap < len(artists):
            most_similar = other_user
            max_overlap = overlap
            
    if most_similar is None:
        print("No recommendations available at this time.")
        return
    
    recommendations = []
    for artist in users[most_similar]:
        if artist not in users[username]:
            recommendations.append(artist)
            
    recommendations.sort()
    
    for artist in recommendations:
        print(artist)
        
def show_most_popular(users):
    """Prints 3 most popular artists"""
    # Jason Dong
    counts = {}
    for user,artists in users.items():
        if user.endswith('$'): 
            continue
        for artist in artists:
            if artist in counts:
                counts[artist] += 1
            else:
                counts[artist] = 1
                
    sorted_artists = sorted(counts, key=counts.get, reverse=True)


    if not sorted_artists:
        print("Sorry, no artists found.")
        return

    for i in range(min(3, len(sorted_artists))):
        print(sorted_artists[i])
        
def most_popular_count(users):
    """Prints count of most popular artist""" 
    # Vidhur Busannagari
    counts = {}
    for user,artists in users.items():
        if user.endswith('$'):
            continue
        for artist in artists:
            if artist in counts:
                counts[artist] += 1
            else:
                counts[artist] = 1

    if not counts:
        print("Sorry, no artists found.")
        return
    
    print(max(counts.values()))
        
def most_artists_user(users):
    """Prints user(s) who like most artists"""
    # Vidhur Busannagari
    artist_counts = {}
    for user in users:
        if user.endswith('$'):
            continue
        artist_counts[user] = len(set(users[user]))

    if not artist_counts:
        print("Sorry, no user found.")
        return

    max_count = max(artist_counts.values())
    for user, count in artist_counts.items():
        if count == max_count:
            print(user)
        
def load_database():
    # Vidhur Busannagari
    """Loads user preferences from 'database.txt' file and returns a dictionary."""
    users = {}
    if os.path.exists('database.txt'):
        with open('database.txt') as f:
            for line in f:
                line = line.strip()
                if line == '':
                    continue
                    
                parts = line.split(':')
                if len(parts) != 2:
                    continue
                    
                user = parts[0].strip()
                artists = parts[1].strip()
                users[user] = get_artists(artists)

    else:
        open('database.txt', 'w').close()
        
    return users

def main():
    """Handles the main program flow, user interaction, and menu options."""
    # Vidhur Busannagari
    print("Enter your name (put a $ symbol after your name if you wish your preferences to remain private):")
    username = input()
    
    users = load_database()
    
    if username not in users:
        enter_preferences(username, users)
        
    while True:
        print('''Enter a letter to choose an option:
e - Enter preferences
r - Get recommendations
p - Show most popular artists
h - How popular is the most popular  
m - Which user has the most likes
q - Save and quit''')
        
        choice = input()
        
        if choice == 'e':
            enter_preferences(username, users)
        elif choice == 'r':
            get_recommendations(username, users) 
        elif choice == 'p':
            show_most_popular(users)
        elif choice == 'h':
           most_popular_count(users)
        elif choice == 'm':
            most_artists_user(users)
        elif choice == 'q':
            save_and_quit(users)
            
main()


'''
testInsert(insertV1)
testSearch()
testInsert(insertV2)
testV1()
testV2()
testSort(insertSortV1)
testSort(insertSortV2)
letterCounts("dict.py")
'''