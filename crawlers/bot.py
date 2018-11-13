import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from web_crawler import get_reddit_info, pretty_print

def start(bot, update):
	'''
	Function that defines returned messagem when user starts conversation or types /start
	'''
	message = "Busque as threads que bombam na primeira página dos subreddits! Para buscar, digite o comando /NadaPraFazer e os subreddits desejados separados por ponto e virgula! Exemplo: /NadaPraFazer cats;AskReddit"
	update.message.reply_text(message)

def random_message(bot, update):
	'''
	Function that handles any message that the user sends that is not one of the two aviables commands
	'''
	message = "Busque as threads que bombam na primeira página dos subreddits! Para buscar, digite o comando /NadaPraFazer e os subreddits desejados separados por ponto e virgula! Exemplo: /NadaPraFazer cats;AskReddit"
	update.message.reply_text(message)

def nothing_to_do(bot, update, args):
	'''
	Function that handles the /NadaPraFazer command
	'''
	if args:
		subreddits = args[0].split(";")
		message = ""
		for sub in subreddits:	
			(success, result_dict, post_count) = get_reddit_info(sub)
			message += pretty_print(result_dict, sub, post_count)
	else:
		message = "Escolha um subreddit para buscar threads que bombam, para buscar mais de um, separe-os por ponto e virgula! Exemplo: Exemplo: /NadaPraFazer cats;AskReddit"

	update.message.reply_text(message, parse_mode=telegram.ParseMode.MARKDOWN)

def run_bot():

	#Initialize bot
	updater = Updater('TOKEN')
	dispatcher = updater.dispatcher
	print("Bot is up!")

	#Create handlers
	start_handler = CommandHandler('start', start)
	nothing_handler = CommandHandler('NadaPraFazer', nothing_to_do, pass_args=True)
	random_msg_handler = MessageHandler(Filters.text, random_message)

	#Add handlers to dispatcher
	dispatcher.add_handler(start_handler)
	dispatcher.add_handler(random_msg_handler)
	dispatcher.add_handler(nothing_handler)

	#Run bot!
	updater.start_polling()
	updater.idle()

if __name__ == '__main__':
  run_bot()