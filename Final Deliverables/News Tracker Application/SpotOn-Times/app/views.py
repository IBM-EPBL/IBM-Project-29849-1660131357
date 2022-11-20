from app import app
import ibm_db
from flask import session, flash, redirect, render_template, request, url_for
from .request import (businessArticles, entArticles, get_news_source,
                      healthArticles, publishedArticles, randomArticles,
                      scienceArticles, sportArticles, techArticles,
                      topHeadlines)

conn = ibm_db.connect(
    'DATABASE=bludb;'
    'HOSTNAME=98538591-7217-4024-b027-8baa776ffad1.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud;'
    'PORT=30875;'
    'SECURITY=SSL;'
    'SSLServerCertificate=DigiCertGlobalRootCA.crt;'
    'UID=rzf07928;'
    'PWD=Gsmx9dW4PeOQMqze;', '', ''
)

global account

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # getting user data
        email = request.form.get('email')
        password = request.form.get('password')
        sql_check_query = "SELECT * FROM user WHERE email = ?"
        stmt = ibm_db.prepare(conn, sql_check_query)
        ibm_db.bind_param(stmt, 1, email)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)
        print(account)
        if account:
            # email id exists 
            # checking if the password is correct
            if not account['PASSWORD'] == password:
                flash('Invalid password', category='error')

            else:
                # user entered the correct password
                # redirecting the user to the dashboard
                session['user_id'] = account['EMAIL']
                return redirect(url_for('home'))

        else:
            # email id does not exist in the database
            flash('Email invalid... Try Again', category='error')
            
        return render_template('auth/login.html')
    
    return render_template('auth/login.html')
    # return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # getting user data
        email = request.form.get('email')
        password = request.form.get('password')
        # checking: user already exists or not
        sql_check_query = "SELECT * FROM user WHERE email = ?"
        stmt = ibm_db.prepare(conn, sql_check_query)
        ibm_db.bind_param(stmt, 1, email)
        ibm_db.execute(stmt) 

        account = ibm_db.fetch_assoc(stmt)
        # email id does not exist in the database
        if not account:
            # inserting the data into the database
            sql_insert_query = "INSERT INTO user VALUES (?, ?)"
            stmt = ibm_db.prepare(conn, sql_insert_query)
            ibm_db.bind_param(stmt, 1, email)
            ibm_db.bind_param(stmt, 2, password)
            ibm_db.execute(stmt)

            # user data inserted into the database
            # redirecting to login page
            flash('User created successfully! Please Login', category='success')
            return redirect('/')

        else:
            flash('Email id already exists! Try another one', category='error')

        return render_template('auth/register.html')

    return render_template('auth/register.html')
    # return render_template('register.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    articles = publishedArticles()
    
    todays_news = articles[0]
    top_headlines = articles[1]
    business_articles = articles[2]
    tech_articles = articles[3]
    entertainment_articles = articles[4]
    science_articles = articles[5]
    sport_articles = articles[6]
    health_articles = articles[7]
        
    return  render_template('home.html', 
                            todays_news = todays_news, 
                            top_headlines = top_headlines,
                            business_articles = business_articles,
                            tech_articles = tech_articles,
                            entertainment_articles = entertainment_articles,
                            science_articles = science_articles,
                            sport_articles = sport_articles,
                            health_articles = health_articles,
                            account = session['user_id'])

@app.route('/headlines')
def headlines():
    headlines = topHeadlines()

    return  render_template('headlines.html', headlines = headlines, account = session['user_id'])

@app.route('/articles')
def articles():
    random = randomArticles()

    return  render_template('articles.html', random = random, account = session['user_id'])

@app.route('/sources')
def sources():
    newsSource = get_news_source()

    return  render_template('sources.html', newsSource = newsSource, account = session['user_id'])

@app.route('/category/business')
def business():
    sources = businessArticles()

    return  render_template('business.html', sources = sources, account = session['user_id'])

@app.route('/category/tech')
def tech():
    sources = techArticles()

    return  render_template('tech.html', sources = sources, account = session['user_id'])

@app.route('/category/entertainment')
def entertainment():
    sources = entArticles()

    return  render_template('entertainment.html', sources = sources, account = session['user_id'])

@app.route('/category/science')
def science():
    sources = scienceArticles()

    return  render_template('science.html', sources = sources, account = session['user_id'])

@app.route('/category/sports')
def sports():
    sources = sportArticles()

    return  render_template('sport.html', sources = sources, account = session['user_id'])

@app.route('/category/health')
def health():
    sources = healthArticles()

    return  render_template('health.html', sources = sources, account = session['user_id'])