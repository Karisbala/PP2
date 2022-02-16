import json

def is_above_55(movies):
    print('Enter the name of your movie: ', end = '')
    n = input()
    for i in range(len(movies)):
        if movies[i]['imdb'] >= 5.5 and movies[i]['name'] == n:
            return True
        
def list_of_above_55(movies):
    list_above_55 = []
    for i in range(len(movies)):
        if movies[i]['imdb'] >= 5.5:
            list_above_55.append(movies[i])
    return list_above_55

def category(movies):
    print('Please enter the name of your chosen category: ', end = '')
    c = input()
    print('List of movies that have "{}" category:'.format(c))
    for i in range(len(movies)):
        if movies[i]['category'] == c:
            print('-{}'.format(movies[i]['name']))

def aver_movie_imdb(movies):
    imdb_sum = 0
    for i in range(len(movies)):
        imdb_sum += movies[i]['imdb']
    aver_imdb = imdb_sum / len(movies)
    return round(aver_imdb, 1)
        
def aver_cat_imdb(movies):
    print('Please enter the name of your chosen category: ', end = '')
    c = input()
    imdb_sum = 0
    k = 0
    for i in range(len(movies)):
        if movies[i]['category'] == c:
            k += 1
            imdb_sum += movies[i]['imdb']
    aver_imdb = imdb_sum / k
    return round(aver_imdb, 1)


f = open('movie_list.json')
movies = json.load(f)


#task1
print(is_above_55(movies))
#task2
print('List of movies that have IMDB above 5.5:',list_of_above_55(movies))
#task3
category(movies)
#task4
print('The average IMDB of all movies:', aver_movie_imdb(movies))
#task5
print('The average IMDB of chosen category:', aver_cat_imdb(movies))


f.close()