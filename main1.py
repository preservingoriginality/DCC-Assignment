
from flask import Flask, render_template, request,redirect,url_for,Response
from flask_mysqldb import MySQL

app = Flask(__name__)

# Connect to MySQL databases
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'gramaj11'
app.config['MYSQL_DB'] = 'dcc_project'
mysql=MySQL(app)
# app1=Flask(__name__)
# app1.config['MYSQL_HOST'] = 'localhost'
# app1.config['MYSQL_USER'] = 'root'
# app1.config['MYSQL_PASSWORD'] = 'gramaj11'
# app1.config['MYSQL_DB'] = 'purchasers'
# purchasers_db=MySQL(app1)
# Define routes and functions for each feature
@app.route('/')
def home():
    return render_template('index1.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form['query']
        
        # Connect to purchasers database
        cursor = mysql.connection.cursor()
        
        # Execute the search query and fetch data from the database
        sql = "SELECT * FROM (dcc_project.purchaser join dcc_project.party ) WHERE dcc_project.purchaser.bond_number = %s or dcc_project.purchaser.company_name=%s"#or %s in dcc_project.purchaser.company_name"
        cursor.execute(sql, (query, query))
        results = cursor.fetchall()
        
        return render_template('search.html', results=results)
    
    return render_template('search_form.html')

@app.route('/company_stats', methods=['GET', 'POST'])
def company_stats():
    if request.method == 'POST':
        selected_company = request.form['company']
        
        # Connect to purchasers database
        cursor = mysql.connection.cursor()
        
        # Execute the query to compute statistics for the selected company
        sql = "SELECT purchase_date,COUNT(Denominations), SUM(Denominations) FROM dcc_project.purchaser WHERE company_name = %s GROUP BY purchase_date"
        cursor.execute(sql, (selected_company[2:-3],))
        results = cursor.fetchall()
        
        return render_template('company_stats.html', results=results)
    
    # Connect to purchasers database
    cursor = mysql.connection.cursor()
    
    # Fetch the list of companies
    cursor.execute("SELECT DISTINCT company_name FROM dcc_project.purchaser")
    companies = cursor.fetchall()
    
    return render_template('company_stats_form.html', companies=companies)

@app.route('/party_stats', methods=['GET', 'POST'])
def party_stats():
    if request.method == 'POST':
        selected_party = request.form['party']
        
        # Connect to parties database
        cursor = mysql.connection.cursor()
        
        # Execute the query to compute statistics for the selected party
        sql = "SELECT purchase_date ,COUNT(*), SUM(Denominations) FROM dcc_project.party WHERE party_name = %s group by purchase_date"
        cursor.execute(sql, (selected_party[2:-3],))
        results = cursor.fetchall()
        
        return render_template('party_stats.html', results=results)
    
    # Connect to parties database
    cursor = mysql.connection.cursor()
    
    # Fetch the list of parties
    cursor.execute("SELECT DISTINCT party_name FROM dcc_project.party")
    parties = cursor.fetchall()
    return render_template('party_stats_form.html', parties=parties)

@app.route('/party_donors', methods=['GET', 'POST'])
def party_donors():
    if request.method == 'POST':
        selected_party = request.form['party']
        
        # Connect to purchasers database
        cursor = mysql.connection.cursor()
        
        # Execute the query to fetch donor information for the selected party
        sql = "SELECT company_name, SUM(dcc_project.party.Denominations) FROM (dcc_project.purchaser join dcc_project.party) where party_name = %s GROUP BY company_name"
        cursor.execute(sql, (selected_party[2:-3],))
        results = cursor.fetchall()
        
        return render_template('party_donors.html', results=results)
    
    # Connect to parties database
    cursor = mysql.connection.cursor()
    
    # Fetch the list of parties
    cursor.execute("SELECT DISTINCT party_name FROM dcc_project.party")
    parties = cursor.fetchall()
    
    return render_template('party_donors_form.html', parties=parties)

@app.route('/company_donations', methods=['GET', 'POST'])
def company_donations():
    if request.method == 'POST':
        selected_company = request.form['company']
        
        # Connect to purchasers database
        cursor = mysql.connection.cursor()
        
        # Execute the query to fetch donation information for the selected company
        sql = "SELECT party_name, SUM(dcc_project.party.Denominations) FROM (dcc_project.purchaser join dcc_project.party) WHERE company_name = %s GROUP BY party_name"
        cursor.execute(sql, (selected_company[2:-3],))
        results = cursor.fetchall()
        
        return render_template('company_donations.html', results=results)
    
    # Connect to purchasers database
    cursor = mysql.connection.cursor()
    
    # Fetch the list of companies
    cursor.execute("SELECT DISTINCT company_name FROM dcc_project.purchaser")
    companies = cursor.fetchall()
    
    return render_template('company_donations_form.html', companies=companies)

@app.route('/donation_pie_chart')
def donation_pie_chart():
    # Connect to parties database
    cursor = mysql.connection.cursor()
    
    # Execute the query to compute the total amount of donations to all parties
    cursor.execute("SELECT party_name, SUM(Denominations) FROM dcc_project.party GROUP BY party_name")
    results = cursor.fetchall()
    
    return render_template('donation_pie_chart.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
