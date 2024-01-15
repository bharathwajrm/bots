import requests
import pyttsx4

# Replace with your API key from newsapi.org
NEWS_API_KEY = 'a6328c7ab54a41b097f69cafa69782e2'

# Initialize the pyttsx3 engine
engine = pyttsx4.init()

def get_news(category):
    url = f'https://newsapi.org/v2/top-headlines'
    params = {
        'apiKey': NEWS_API_KEY,
        'category': category,
        'language': 'en',
    }

    response = requests.get(url, params=params)
    data = response.json()

    if data['status'] == 'ok':
        articles = data['articles']
        return articles
    else:
        return []

def read_news(news_articles):
    for i, article in enumerate(news_articles, 1):
        title = article['title']
        print(f"{i}. {title}")
        engine.say(title)
        engine.runAndWait()

def print_categories():
    categories = {
        1: 'technology',
        2: 'sports',
        3: 'entertainment',
        4: 'science',
        5: 'health'
    }

    print("\nAvailable Categories:")
    for num, category in categories.items():
        print(f"{num}. {category}")

def main():
    print("Welcome to the News Bot!")
    print("i'm NewsMate what do you want ?!")

    while True:
        print_categories()
        user_input = input("Enter a category number (or 'exit' to quit): ").lower()

        if user_input == 'exit':
            break

        try:
            category_num = int(user_input)
            if category_num not in range(1, 10):
                print("Invalid category number. Please choose from the available options.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid category number.")
            continue

        category = {
            1: 'technology',
            2: 'sports',
            3: 'entertainment',
            4: 'science',
            5: 'health'
        }[category_num]

        news_articles = get_news(category)
        if not news_articles:
            print("Error fetching news. Please try again later.")
            continue

        print(f"\n--- {category.capitalize()} News ---")
        read_news(news_articles)

if __name__ == "__main__":
    main()
