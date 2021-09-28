from flask import Flask, render_template, request, jsonify, session, url_for, redirect
import numpy as np
import pandas as pd
from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField
from operator import itemgetter


movies = []


def get_similar_movies(df, sample_json):
    similarity = df[sample_json[0]]*(sample_json[1]-2.5)
    similarity = similarity.sort_values(ascending=False)
    movie_similarity = similarity.to_frame().reset_index()['index'].values[0:9]
    movie_suggestions = []
    for x in movie_similarity:
        movie_suggestions.append(
            [int(x), df.iloc[x]['title'], round((similarity[int(x)]/2.5)*100, 2)])
    return movie_suggestions


def movie_prediction(movies):
    content = movies
    results = []
    for movie in content:
        results = results + get_similar_movies(df_sim, movie)
    results = sorted(results, reverse=True, key=itemgetter(2))
    for movie in content:
        for i in range(len(results)-1, -1, -1):
            if movie[0] == results[i][1]:
                results.pop(i)
    return results[0:9]


app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        movie = request.form['movie']
        rating = int(request.form['rating'])
        movies.append([movie, rating, len(movies)])
        suggestions = movie_prediction(movies)
        return render_template('index.html', movies=movies, suggestions=suggestions)
    elif movies:
        suggestions = movie_prediction(movies)
        return render_template('index.html', movies=movies, suggestions=suggestions)
    return render_template('index.html')


@app.route("/delete/<int:movie_index>")
def delete(movie_index):
    movies.pop(movie_index)
    for movie in movies:
        movie[2] = movies.index(movie)
    return redirect(url_for("index"))


df_sim = pd.read_csv('./data/item_sim_df.csv')

if __name__ == '__main__':
    app.run()
