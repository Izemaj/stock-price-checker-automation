<!DOCTYPE html>
<html>
<head>
	<title>README: Stock Price Checker</title>
</head>
<body>
	<h1>Stock Price Checker</h1>
	<p>This program fetches the closing prices of a stock for the last two days from AlphaVantage API, calculates the percentage difference between the prices, fetches news articles related to the company, and sends SMS messages using Twilio API based on the percentage difference in stock prices.</p>
	<h2>Functions</h2>
	<p>The program is divided into several functions:</p>
	<ul>
		<li><code>get_stock_prices()</code>: This function fetches the closing prices of a stock for the last two days from AlphaVantage API.</li>
		<li><code>calculate_percentage_difference()</code>: This function calculates the percentage difference between the closing prices.</li>
		<li><code>get_news_articles()</code>: This function fetches news articles related to the company using News API.</li>
		<li><code>send_sms()</code>: This function sends an SMS message using Twilio API based on the percentage difference in stock prices.</li>
		<li><code>main()</code>: This function calls all the other functions in the correct order to execute the program.</li>
	</ul>
	<h2>How it works</h2>
	<p>When you run the program, it prompts you to enter the stock symbol for the company you want to check. Then, it uses the AlphaVantage API to fetch the closing prices of the stock for the last two days. It calculates the percentage difference between the prices and determines if it's a significant change. If the change is significant, it uses the News API to fetch news articles related to the company. Finally, it sends an SMS message using Twilio API to notify you of the change in stock prices and provide a summary of the news articles.</p>
	<h2>Requirements</h2>
	<ul>
		<li>Python 3.x</li>
		<li>Requests library</li>
		<li>Twilio library</li>
		<li>News API key</li>
		<li>AlphaVantage API key</li>
		<li>Twilio account and phone number</li>
	</ul>
	<h2>Usage</h2>
	<ol>
		<li>Clone the repository to your local machine.</li>
		<li>Install the required libraries using pip:</li>
		<pre><code>pip install -r requirements.txt</code></pre>
		<li>Get your News API key and AlphaVantage API key and update the <code>config.ini</code> file with your keys.</li>
		<li>Sign up for a Twilio account and get a Twilio phone number. Update the <code>config.ini</code> file with your Twilio account SID, auth token, and phone number.</li>
		<li>Run the program:</li>
		<pre><code>python stock_price_checker.py</code></pre>
	</ol>
</body>
</html>



