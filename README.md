<!DOCTYPE html>
<html>
<head>
</head>
<body>
	<h1>Stock Alert App</h1>
	<p>This is a simple Python application that sends SMS alerts based on the percentage change in stock prices of a particular company.</p>
  <h2>Features</h2>
<ul>
	<li>Fetches the closing prices of a stock for the last two days from AlphaVantage API.</li>
	<li>Calculates the percentage difference between two prices and indicates if it was an increase or decrease.</li>
	<li>Fetches news articles related to a query from GNews API.</li>
	<li>Sends SMS messages using Twilio API based on the percentage difference in stock prices.</li>
</ul>

<h2>Installation</h2>
<ol>
	<li>Clone the repository: <code>git clone https://github.com/your-username/stock-alert-app.git</code></li>
	<li>Install the required dependencies: <code>pip install -r requirements.txt</code></li>
	<li>Set environment variables for sensitive information:
		<ul>
			<li><code>ALPHAVANTAGE_API_KEY</code>: AlphaVantage API key</li>
			<li><code>GNEWS_API_KEY</code>: GNews API key</li>
			<li><code>TWILIO_ACCOUNT_SID</code>: Twilio account SID</li>
			<li><code>TWILIO_AUTH_TOKEN</code>: Twilio authentication token</li>
			<li><code>TWILIO_PHONE_NUMBER</code>: Twilio phone number</li>
		</ul>
	</li>
</ol>

<h2>Usage</h2>
<p>To run the application, execute the following command in the terminal:</p>
<pre><code>python main.py</code></pre>

<p>The application will fetch the closing prices of the specified stock for the last two days and calculate the percentage difference. If the percentage difference is greater than 5%, it will fetch news articles related to the company and send an SMS alert with the percentage difference and the news articles.</p>

<h2>Contributing</h2>
<p>Contributions are welcome! If you would like to contribute to this project, please follow these steps:</p>
<ol>
	<li>Fork the repository</li>
	<li>Create a new branch: <code>git checkout -b new-feature</code></li>
	<li>Make your changes and commit them: <code>git commit -m 'Add new feature'</code></li>
	<li>Push to the branch: <code>git push origin new-feature</code></li>
	<li>Create a pull request</li>
</ol>

<h2>Credits</h2>
<p>This project was created by <a href="https://github.com/izemaj">Izemaj</a>.</p>
 </body>
</html>


