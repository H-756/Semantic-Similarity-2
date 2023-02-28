import spacy

nlp = spacy.load('en_core_web_md')

with open('movies.txt', 'r') as f1:
    movie_list = []
    movies = f1.readlines()
    for movie in movies:
        movie_list.append(movie.strip('\n'))


hulk = 'Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on theplanet Sakaar where he is sold into slavery and trained as a gladiator.'


movie_watched = nlp(hulk)

def recommendation(movie_watched, movie_list):
    recommendation_list = []
    similarity_score_list = []
    for movie in movie_list:
        similarity = nlp(movie).similarity(movie_watched)
        similarity_score_list.append(similarity)
        recommendation_list.append(f'{movie[0: 7]} - {similarity}'.split(" - "))
    similarity_score_list.sort()
    
    for recommendation in recommendation_list:
        if str(similarity_score_list[-1]) == recommendation[1]:
            print(recommendation[0])
            break

recommendation(movie_watched, movie_list)