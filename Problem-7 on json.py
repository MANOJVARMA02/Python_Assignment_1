from urllib.request import urlopen
import json
import operator

def genres_data(movies_data,each_year):
    list=[]
    for movie in movies_data:
        if(movie['year']==each_year):
            list.append(movie['genres'])
    return list

def splitting(genres_list):
    list2=[]
    for movie_genre in genres_list:
        No_of_genres=len(movie_genre)-1
        while(No_of_genres>=0):
            list2.append(movie_genre[No_of_genres])
            No_of_genres -= 1
    return list2

def repeatation(splitted_list,temp):
    dict={}
    for i in range(0,len(splitted_list)):
        inc=0
        for j in range(i+1,len(splitted_list)):
            if(splitted_list[i]==splitted_list[j] and splitted_list[i] not in dict):
                inc+=1
        if(inc!=0):
            dict.update({splitted_list[i]:inc})
        elif(splitted_list[i] not in dict):
            dict.update({splitted_list[i]:1})
    if(temp==0):
        max_value=max(sorted(dict.values()))
        return (list(dict.items())[list(dict.values()).index(max_value)])
    else:
        return (sorted(dict.items(),key=operator.itemgetter(1),reverse=True))    

def main():
    try:
        url="https://raw.githubusercontent.com/prust/wikipedia-movie-data/master/movies.json"  #----Storing url
        response=urlopen(url)                                                                  #----storing the response of url
        movies_data=json.loads(response.read())                                                #----storing the json response
    except:
        print("Invalid url")
    print("The genres which had most num of films from the year 2010 to 2018 are :")
    for each_year in range(2010,2019):                                                         #----iterating from year 2010 to 2018
        genres_list=genres_data(movies_data,each_year)                                         #---it is used to get all the years from 2010 to 2018                                    
        splitted_list=splitting(genres_list)                                                   #---it is used to splitt the genre if film contains two genres
        max_repeated_genre=repeatation(splitted_list,0)                                        #---used to find the count of max repeated genre for each year
        print(max_repeated_genre,"in the year", each_year)
        if(each_year==2018):
            repeated_genres=repeatation(splitted_list,1)                                       #---used to get number of movies releaded in each genre during 2018
            print("Number of films released in the year 2018 in different genres are : ")
            print(repeated_genres)

main()