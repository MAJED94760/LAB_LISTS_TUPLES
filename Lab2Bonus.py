movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

# احسب التقييم المتوسط لكل فيلم
movie_avg_list = []
for movie in movies:
    title, year, ratings = movie
    avg_rating = sum(ratings) / len(ratings)
    if avg_rating >= 6.0:
        movie_avg_list.append((title, year, round(avg_rating, 2)))

# رتب الأفلام حسب التقييم المتوسط
movie_avg_list.sort(key=lambda x: x[2], reverse=True)

# عرض النتائج
print("\n🎬 Top Rated Movies:")
for idx, movie in enumerate(movie_avg_list):
    print(f"{idx+1}. {movie[0]} ({movie[1]}) - Average rating: {movie[2]} ★")
