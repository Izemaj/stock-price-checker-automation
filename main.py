import os
import requests
from datetime import datetime, timedelta
from typing import Tuple
from twilio.rest import Client

STOCK_NAME = "SHOP.TRT"
COMPANY_NAME = "Shopify"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://gnews.io/api/v4/search"

# Load sensitive information from environment variables
API_KEY_STOCKS = os.environ.get("ALPHAVANTAGE_API_KEY")
API_KEY_NEWS = os.environ.get("GNEWS_API_KEY")
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.environ.get("TWILIO_PHONE_NUMBER")

def get_stock_prices(api_key: str, stock_name: str, days: int = 2) -> Tuple[float, float]:
    """
    Fetches the closing prices of a stock for the last two days from AlphaVantage API.

    Args:
        api_key (str): AlphaVantage API key.
        stock_name (str): Stock symbol.
        days (int): Number of days for which the closing prices are required.

    Returns:
        A tuple containing the closing prices of the stock for the last two days.
    """
    end_date = datetime.today() - timedelta(days=1)
    start_date = end_date - timedelta(days=days-1)
    start_date_str = start_date.strftime("%Y-%m-%d")
    end_date_str = end_date.strftime("%Y-%m-%d")

    params = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": stock_name,
        "apikey": api_key,
    }

    response = requests.get(STOCK_ENDPOINT, params=params)
    data = response.json()
    day_before_closing_price = float(data["Time Series (Daily)"][start_date_str]["4. close"])
    yesterday_closing_price = float(data["Time Series (Daily)"][end_date_str]["4. close"])

    return day_before_closing_price, yesterday_closing_price

def calculate_percentage_difference(price1: int, price2:int)-> Tuple[float, str]:
    """
    Calculates the percentage difference between two prices and indicates if it was an increase or decrease.
    
    Args:
        price1 (float): The first price.
        price2 (float): The second price.
    
    Returns:
        A tuple containing the percentage difference as a float and a string indicating whether it was an increase or decrease.
    """
    percentage_difference = (price2 - price1) / price1 * 100
    
    if percentage_difference > 0:
        return (round(percentage_difference, 2), "increase")
    elif percentage_difference < 0:
        return (round(abs(percentage_difference), 2), "decrease")
    else:
        return (percentage_difference, "no change")

def get_news()-> list:
    """
    Fetches news articles related to a query from GNews API.

    Args:
        api_key (str): GNews API key.
        query (str): Query string for which news articles are required.

    Returns:
        A list of news articles.
    """
    url = f"{NEWS_ENDPOINT}?q={COMPANY_NAME}&lang=en&country=us&max=10&apikey={API_KEY_NEWS}"
    response = requests.get(url=url)
    response.raise_for_status()
    news_data = response.json()
    return news_data["articles"][:3]

def send_messages(account_sid: str,
                 auth_token: str,
                 from_phone_number:str,
                 to_phone_number:str, 
                 percentage_difference:int, 
                 articles:list,
                 change:str)-> list:
    """
    Sends SMS messages using Twilio API.

    Args:
        account_sid (str): Twilio account SID.
        auth_token (str): Twilio authentication token.
        from_phone_number (str): Twilio phone number.
        to_phone_number (str): Phone number to which messages should be sent.
        articles (list): List of articles to be sent as messages.
        percentage_difference (int): Percentage difference between the closing prices of the stock for the last two days.
        change (str): Indicates whether the percentage difference was an increase or decrease.

    Returns:
        A list of message statuses.
    """
    client = Client(account_sid, auth_token)
    messages = []
    if change == "increase":
        for i, article in enumerate(articles):
            message_body = f"TSLA: 🔺{percentage_difference}%\nHeadline: {article['title']}\nBrief: {article['description']}"
            message = client.messages.create(
                body=message_body,
                from_=from_phone_number,
                to=to_phone_number
            )
            messages.append(message)
            print(f"Message {i+1} status: {message.status}")
    elif change == "decrease":
        for i, article in enumerate(articles):
            message_body = f"TSLA: 🔻{percentage_difference}%\nHeadline: {article['title']}\nBrief: {article['description']}"
            message = client.messages.create(
                body=message_body,
                from_=from_phone_number,
                to=to_phone_number
            )
            messages.append(message)
            print(f"Message {i+1} status: {message.status}")
    return messages

def main()-> list:
    """
    Sends SMS messages using Twilio API based on the percentage difference in stock prices.

    Returns:
        A list of message statuses.
    """
    stock_prices = get_stock_prices(api_key=API_KEY_STOCKS, stock_name=STOCK_NAME)
    percentage_difference = calculate_percentage_difference(stock_prices[0], stock_prices[1])
    if percentage_difference[0] > 5 and percentage_difference[1]=="increase":
        articles = get_news()
        messages = send_messages(account_sid=TWILIO_ACCOUNT_SID, auth_token=TWILIO_AUTH_TOKEN, from_phone_number=TWILIO_PHONE_NUMBER, to_phone_number="your_number",percentage_difference=percentage_difference[0], articles=articles, change="increase")
        return messages
    elif percentage_difference[0] > 5 and percentage_difference[1]=="decrease":
        articles = get_news()
        messages = send_messages(account_sid=TWILIO_ACCOUNT_SID, auth_token=TWILIO_AUTH_TOKEN, from_phone_number=TWILIO_PHONE_NUMBER, to_phone_number="your_number",percentage_difference=percentage_difference[0], articles=articles, change="decrease")
        return messages
    else:
        return []

if __name__ == "__main__":
    main()