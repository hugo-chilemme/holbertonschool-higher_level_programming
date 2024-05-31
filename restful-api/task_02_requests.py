import requests
import csv 


def fetch_posts():

	API_URL = 'https://jsonplaceholder.typicode.com/posts'

	response = requests.get(API_URL)

	if response.status_code != 200:

		exit(response.status_code)

	return response


def fetch_and_print_posts(print_posts = True):
	
	response = fetch_posts()

	print("Status Code: {}".format(response.status_code))

	posts = response.json()

	for post in posts:

		title = post.get('title')

		print("{}".format(title))


def fetch_and_save_posts():

	response = fetch_posts()

	posts = response.json()

	rows = ['id', 'title', 'body']

	with open('posts.csv', 'w') as file:

		obj_to_csv = csv.writer(file)

		obj_to_csv.writerow(rows)

		for post in posts:

			obj_to_csv.writerow([
				post.get('id'),
				post.get('title'),
				post.get('body')
			])


	