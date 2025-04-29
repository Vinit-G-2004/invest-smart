from flask import Flask, render_template, request

app = Flask(__name__)

# Your stock data (sample data with more companies)
STOCKS = {
    'Apple': 175.16, 'Microsoft': 320.57, 'Amazon': 125.75, 'Tesla': 232.12, 'Google': 135.89,
    'Facebook': 325.50, 'Netflix': 595.45, 'Uber': 56.12, 'Airbnb': 188.43, 'Spotify': 284.16,
    'Intel': 51.25, 'NVIDIA': 617.45, 'AMD': 122.35, 'Boeing': 226.45, 'Adobe': 563.16,
    'PayPal': 305.12, 'Salesforce': 265.70, 'Twitter': 74.33, 'Snap': 41.50, 'Pinterest': 64.22,
    'Zoom': 360.34, 'Snapchat': 42.25, 'Slack': 35.45, 'Square': 229.43, 'Spotify': 240.76,
    'IBM': 125.44, 'Oracle': 81.36, 'Microsoft': 321.87, 'Disney': 177.92, 'Visa': 225.76,
    'Mastercard': 365.74, 'Roku': 225.20, 'eBay': 54.13, 'Pinterest': 62.10, 'Shopify': 702.13,
    'Shopify': 751.15, 'Salesforce': 270.45, 'Zoom': 400.23, 'Spotify': 285.11, 'Spotify': 285.30,
    'Shopify': 750.15, 'Xerox': 23.56, 'Adobe': 563.76, 'Alibaba': 234.44, 'Nokia': 11.25,
    'Qualcomm': 138.56, 'T-Mobile': 115.12, 'Verizon': 48.43, 'AT&T': 26.98, 'Walmart': 140.21,
    'HomeDepot': 326.22, 'Lowe’s': 212.90, 'BestBuy': 78.12, 'CVS': 91.16, 'Walgreens': 38.50,
    'Target': 203.48, 'Costco': 509.98, 'Kroger': 48.76, 'Macy’s': 28.23, 'Nordstrom': 35.90,
    'JCPenney': 19.05, 'Sears': 12.35, 'Gap': 14.02, 'H&M': 23.42, 'Zara': 27.65,
    'Nike': 125.17, 'Adidas': 144.00, 'Under Armour': 21.35, 'Reebok': 59.25, 'Puma': 76.67,
    'Lululemon': 360.12, 'Burberry': 206.45, 'Rolex': 5000.00, 'Gucci': 1200.30, 'Louis Vuitton': 1560.45,
    'Prada': 1320.25, 'Chanel': 1800.00, 'Coach': 650.20, 'Tommy Hilfiger': 120.65, 'Calvin Klein': 78.75,
    'Lacoste': 85.50, 'Abercrombie & Fitch': 29.12, 'Hollister': 35.75, 'Forever21': 22.32, 'American Eagle': 26.10,
    'Aeropostale': 15.56, 'Gap': 14.02, 'Old Navy': 21.60, 'Banana Republic': 26.78, 'Uniqlo': 30.22,
    'Muji': 22.44, 'Zara': 37.21, 'H&M': 25.99, 'Shein': 49.99, 'Asos': 43.33,
    'Farfetch': 234.20, 'ModCloth': 65.33, 'Boohoo': 42.30, 'PrettyLittleThing': 49.99, 'Misguided': 40.00,
    'Romwe': 15.22, 'Zaful': 23.11, 'Forever21': 24.10, 'Lulus': 80.32, 'Revolve': 95.45,
    'Fabletics': 78.10, 'ThredUp': 39.45, 'StitchFix': 29.78, 'Levi\'s': 40.50, 'Wrangler': 23.33,
    'Lee': 18.72, 'Wrangler': 21.22, 'Dockers': 33.55, 'Carhartt': 99.12, 'Wrangler': 42.45
}


@app.route('/')
def home():
    return render_template('home.html', stocks=STOCKS)

@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    if request.method == 'POST':
        stock_name = request.form['stock_name']
        investment_value = float(request.form['investment_value'])
        predicted_value = STOCKS.get(stock_name, 0) * investment_value
        return render_template('result.html', stock_name=stock_name, predicted_value=predicted_value, investment_value=investment_value)
    return render_template('prediction.html', stocks=STOCKS)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

