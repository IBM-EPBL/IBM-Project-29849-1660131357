from app.models import Articles
from app.models import Sources
from newsapi import NewsApiClient
from app.config import Config
import urllib.request,json

api_key=None
base_url=None
base_url_for_everything=None
base_url_top_headlines=None
base_source_list=None

all_types_articles = []

def news_sorter(all_articles):

    source = []
    title = []
    desc = []
    author = []
    img = []
    p_date = []
    url = []
    
    for i in range(len(all_articles)):
        
        article = all_articles[i]
        source.append(article['source'])
        title.append(article['title'])
        desc.append(article['description'])
        author.append(article['author'])
        img.append(article['urlToImage'])
        p_date.append(article['publishedAt'])
        url.append(article['url'])

        article_object = Articles(source, title, desc, author, img, p_date, url)
        all_types_articles.append(article_object)
        contents = zip(source, title, desc, author, img, p_date, url)
    
    return  contents

def publishedArticles():
    newsapi = NewsApiClient(api_key= Config.API_KEY)
    news= []
    
    #todays news

    get_articles = newsapi.get_everything(sources= 'cnn, reuters, cnbc, the-verge, gizmodo, the-next-web, techradar, recode, ars-technica')
    all_articles = get_articles['articles']
    
    output = news_sorter(all_articles)
    news.append(output)
    
    #top headlines
    
    get_articles = newsapi.get_top_headlines(sources= 'cnn, reuters, cnbc, techcrunch, the-verge, gizmodo, the-next-web, techradar, recode, ars-technica')
    all_articles = get_articles['articles']
    
    output = news_sorter(all_articles)
    news.append(output)
    
    #business articles
    
    get_articles = newsapi.get_top_headlines(category='business')
    all_articles = get_articles['articles']
    
    output = news_sorter(all_articles)
    news.append(output)
    
    #tech articles
    
    get_articles = newsapi.get_top_headlines(category='technology')
    all_articles = get_articles['articles']
    
    output = news_sorter(all_articles)
    news.append(output)
    
    #entertainment_articles
    
    get_articles = newsapi.get_top_headlines(category='entertainment')
    all_articles = get_articles['articles']
    
    output = news_sorter(all_articles)
    news.append(output)
    
    #science_articles
    
    science_articles = newsapi.get_top_headlines(category='science')
    all_articles = science_articles['articles']
    
    output = news_sorter(all_articles)
    news.append(output)
    
    #sport articles
    
    sport_articles = newsapi.get_top_headlines(category='sports')
    all_articles = sport_articles['articles']
    
    output = news_sorter(all_articles)
    news.append(output)
    
    #health articles
    
    get_articles = newsapi.get_top_headlines(category='health')
    all_articles = get_articles['articles']
    
    output = news_sorter(all_articles)
    news.append(output)
    
    return news

def topHeadlines():
    newsapi = NewsApiClient(api_key= Config.API_KEY)
    top_headlines = newsapi.get_top_headlines(sources= 'cnn, reuters, cnbc, techcrunch, the-verge, gizmodo, the-next-web, techradar, recode, ars-technica')
    all_headlines = top_headlines['articles']

    return  news_sorter(all_headlines)

def randomArticles():
    newsapi = NewsApiClient(api_key= Config.API_KEY)
    random_articles = newsapi.get_everything(sources= 'the-verge, gizmodo, the-next-web, recode, ars-technica')
    all_articles = random_articles['articles']

    return  news_sorter(all_articles)

def businessArticles():
    newsapi = NewsApiClient(api_key= Config.API_KEY)
    business_articles = newsapi.get_top_headlines(category='business')
    all_articles = business_articles['articles']
    
    return  news_sorter(all_articles)

def techArticles():
    newsapi = NewsApiClient(api_key= Config.API_KEY)
    tech_articles = newsapi.get_top_headlines(category='technology')
    all_articles = tech_articles['articles']

    return  news_sorter(all_articles)

def entArticles():
    newsapi = NewsApiClient(api_key= Config.API_KEY)
    ent_articles = newsapi.get_top_headlines(category='entertainment')
    all_articles = ent_articles['articles']
    
    return  news_sorter(all_articles)

def scienceArticles():
    newsapi = NewsApiClient(api_key= Config.API_KEY)
    science_articles = newsapi.get_top_headlines(category='science')
    all_articles = science_articles['articles']

    return  news_sorter(all_articles)

def sportArticles():
    newsapi = NewsApiClient(api_key= Config.API_KEY)
    sport_articles = newsapi.get_top_headlines(category='sports')
    all_articles = sport_articles['articles']
    
    return  news_sorter(all_articles)

def healthArticles():
    newsapi = NewsApiClient(api_key= Config.API_KEY)
    health_articles = newsapi.get_top_headlines(category='health')
    all_articles = health_articles['articles']

    return  news_sorter(all_articles)

def get_news_source():
  '''
  Function that gets the json response to our url request
  '''
  get_news_source_url = 'https://newsapi.org/v2/sources?apiKey=' + Config.API_KEY
  with urllib.request.urlopen(get_news_source_url) as url:
    get_news_source_data = url.read()
    get_news_source_response = json.loads(get_news_source_data)
    news_source_results = None

    if get_news_source_response['sources']:
      news_source_results_list = get_news_source_response['sources']
      news_source_results = process_sources(news_source_results_list)

  return news_source_results

def process_sources(source_list):
  '''
  function that process the news articles and transform them to a list of objects
  '''
  news_source_result = []
  for news_source_item in source_list:
    name = news_source_item.get('name')
    description = news_source_item.get('description')
    url = news_source_item.get('url')

    if name:
      news_source_object = Sources(name, description,url)
      news_source_result.append(news_source_object)
  return news_source_result