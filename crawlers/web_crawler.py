import argparse
import requests

from bs4 import BeautifulSoup
from unidecode import unidecode

def get_reddit_info(sub):
	'''
	This functions searches reddit for topics in the especified subreddit.

	Args:
		parma 1 (string) - the name of the subreddit to search for

	Returns
		bool: Whether the search concluded without errors. Does not take into account 
		      whether the search returned any results
		dict: Result dict with threads information
		int: Thread count
	'''

	
	#Get page content
	page_link = 'https://old.reddit.com/r/' + sub + '/'
	page = requests.get(page_link, headers = {'User-agent': 'agent'})
	if page.status_code != 200:
		print("Erro ao acessar subreddit: %s" % sub)
		return (False, None, None)

	soup = BeautifulSoup(page.text, 'html.parser')

	result_dict = {
		'rank': [],
		'upvotes': [],
		'subreddit': [],
		'title': [],
		'comment_link': [],
		'link': []
	}


	#Find required fields
	reached_limit = False
	post_list = soup.find(class_='sitetable linklisting')
	post_count = 0
	for element in post_list:
	 	find_rank = element.find(class_="rank")
	 	if find_rank:
	 		if find_rank.contents:

	 			upvotes = element.find(class_="score likes")
	 			upvotes = upvotes.contents[0].replace("k", "00").replace('.', '')
	 			
	 			if upvotes == '•':
	 				upvotes = 0

	 			if int(upvotes) < 5000:
	 			 	continue

	 			post_count += 1

	 			result_dict['upvotes'].append(upvotes)

	 			result_dict['rank'].append(find_rank.contents[0])

	 			comment_list = element.find(class_='first').find('a', href=True)
	 			result_dict['comment_link'].append(comment_list['href'])

	 			link = element.find(class_='title').find('a', href=True)
	 			if link['href'].startswith("/r"):
	 				real_link = 'https://old.reddit.com' + link['href']
	 			else:
	 				real_link = link['href']
	 			result_dict['link'].append(real_link)

	 			title = link.contents[0]
	 			result_dict['title'].append(unidecode(title))

	 			result_dict['subreddit'].append(sub)

	return (True, result_dict, post_count)

def pretty_print(result_dict, sub, post_count):
	'''
	This function pretty prints a dictionary that has a format defined in 
	the function get_reddit_info.

	Args:
		param 1 (dict) - dictionary as constructed in get_reddit_info
		param 2 (string) - name of the subrredit
		param 3 (int) - number of interesting post found

	Returns 
		string: formatted message to print
	'''
	message = ""
	if post_count > 0:

		message += "\nThreads bombando no momento em %s\n" % sub
		for index in range(0, post_count):
			message += "\n\tTitulo: %s\n" % result_dict['title'][index]
			message += "\tUpvotes: %s\n" % result_dict['upvotes'][index]
			message += "\tLink: %s\n" % result_dict['link'][index]
			message += "\tLink para comentarios: %s\n" % result_dict['comment_link'][index]
		message += "**************************************************************\n"

	else:
		message += "\nNada foi encontrado para %s :(\n" % sub

	return message

if __name__ == "__main__":

	######################################### Required Arguments #################################### 
	################################################################################################# 
	parser = argparse.ArgumentParser()
	parser.add_argument("-s", "--subreddits", help="Lista de subreddits para pesquisar, separados por ;", 
	                    type=str, required=True)
	args = parser.parse_args()
	#################################################################################################


	#Code Execution
	subreddits = args.subreddits
	subreddits = subreddits.split(";")

	for sub in subreddits:
		(success, result_dict, post_count) = get_reddit_info(sub)

		if not success:
			print("Algo deu errado, tente nova consulta para o subreddit %s" % sub)
		else:
			message = pretty_print(result_dict, sub, post_count)
			print(message)


		