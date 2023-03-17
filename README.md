<!DOCTYPE html>
<html>
<head>
</head>
<body>
	<h1>Stock Price Checker</h1>
	<p>This program fetches the closing prices of a stock for the last two days from AlphaVantage API, calculates the percentage difference between the prices, fetches news articles related to the company, and sends SMS messages using Twilio API based on the percentage difference in stock prices.</p>
	<h2>Functions</h2>
	<p>The program is divided into several functions:</p>
	<ul>
		<li><code>get_stock_prices()</code>: This function fetches the closing prices of a stock for the last two days from AlphaVantage API.</li>
		<li><code>calculate_percentage_difference()</code>: This function calculates the percentage difference between the closing prices.</li>
		<li><code>get_news()</code>: This function fetches news articles related to the company using News API.</li>
		<li><code>send_messages()</code>: This function sends an SMS message using Twilio API based on the percentage difference in stock prices.</li>
		<li><code>main()</code>: This function calls all the other functions in the correct order to execute the program.</li>
	</ul>
	<h2>How it works</h2>
	<p>The automation script fetches the closing prices of a stock for the last two days using the AlphaVantage API after prompting for the stock symbol. It then calculates the percentage difference between the prices and checks if it's a significant change. If it is significant, the script fetches news articles related to the company using the News API. In the final step, it sends an SMS message through the Twilio API to inform you about the change in stock prices and provide a summary of the news articles.</p>
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
		<pre><code>pip install twilio</code></pre>
		<pre><code>pip install requests</code></pre>
		<li>Update the enviroment variables with your News API key, AlphaVantage API key, Twilio account SID, auth token, and phone number.</li>
		<li>Run the program:</li>
		<pre><code>python main.py</code></pre>
	</ol>
<p>Before running the program, make sure you have signed up for a Twilio account and obtained a Twilio phone number, as well as acquired your News API key and AlphaVantage API key. The program will automatically fetch the closing prices of a stock for the last two days using the AlphaVantage API, calculate the percentage difference between the prices, fetch news articles related to the company using the News API, and send SMS messages using the Twilio API based on the percentage difference in stock prices. </p>
</body>
</html>



