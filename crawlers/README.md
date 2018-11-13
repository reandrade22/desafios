# Desafio 2: Crawlers

### web_crawler.py

Este script busca na página inicial de um subreddit os tópicos que foram considerados como "bombando".

Necessita de um parâmetro:
1. -s   : sequência de subreddit para realizar a busca, separador por ponto e virgula ";"

*Exemplo de execução*
`python web_crawler.py -s "cats;AskReddit"`

Quando mais de um subreddit for buscados, os termos devem estar em aspas, como acima.


### bot.py

Script utilizado pelo @nothing_to_do_bot, um bot do Telegram que retorna as threads que bombam em subreddits especificados.

Na conversa com o bot, é necessário digitar o comando /NadaPraFazer, seguido dos subreddits onde se deseja pesquisar, no mesmo formato que o web_crawler.

*Exemplo de comando no Telegram*
`/NadaPrafazer cats;AskReddit`
