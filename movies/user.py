from movie import Movie


class User:
	def __init__(self, name):
		self.name = name
		self.movies = []

	def __repr__(self):
		return "<User {}>".format(self.name)

	def add_movie(self, name, genre):
		self.movies.append(Movie(name, genre, False))

	def delete_movie(self, title):
		self.movies = list(filter(lambda movie: movie.title != title, self.movies))

	def watched_movies(self):
		return list(filter(lambda movie: movie.watched, self.movies))

	def save_to_file(self):
		with open('{}.txt'.format(self.name), 'w') as f:
			f.write(self.name + '\n')
			for movie in self.movies:
				f.write('{}, {}, {}\n'.format(movie.title, movie.genre, str(movie.watched)))

	def set_watched(self, title):
		for movie in self.movies:
			if movie.title == title:
				movie.watched = True
	# @classmethod
	# def load_from_file(cls, filename):
	# 	with open('{}.txt'.format(filename), 'r') as f:
	# 		content = f.readlines()
	# 		username = content[0]
	# 		movies = []
	#
	# 		for line in content[1:]:
	# 			movie_data = line.split(',')  # ['title', 'genre', 'watched']
	# 			movies.append(Movie(movie_data[0], movie_data[1], movie_data[2] == 'True'))
	#
	# 		user = cls(username)
	# 		user.movies = movies
	# 		return user

	def json(self):
		return {
			'name': self.name,
			'movies': [
				movie.json() for movie in self.movies
			]
		}

	@classmethod
	def from_json(cls, json_data):
		user = cls(json_data['name'])
		movies = []
		for movie_data in json_data['movies']:
			movies.append(Movie.from_json(movie_data))

		user.movies = movies
		return user
