import requests
import pyttsx3


def get_news(api_key, category="general"):
    base_url = "http://api.mediastack.com/v1/news"
    params = {
        "access_key": api_key,
        "categories": category
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    articles = data.get("data", [])
    return articles


def get_category_choice():
    categories = {
        "1": "business",
        "2": "entertainment",
        "3": "health",
        "4": "science",
        "5": "sports",
        "6": "technology"
    }

    print("Select a category:")
    for key, value in categories.items():
        print(f"{key}. {value.capitalize()}")

    choice = input("Enter the number: ")
    return categories.get(choice)


def speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    api_key = "4b41612000d274eb2b461c03a6f508a5"

    print("Hii!..I'm clara here to serve you news and articles")

    while True:
        choice = input("Enter '1' for live news or '2' for articles (Press 'q' to quit): ")

        if choice == 'q':
            break

        category = get_category_choice()
        if category is None:
            print("Invalid category selection.")
            continue

        news_list = get_news(api_key, category)

        if not news_list:
            print("No news or articles found.")
            continue

        for idx, news in enumerate(news_list, start=1):
            print(f"{idx}. {news['title']}")
            print(news['description'])
            print("=" * 50)

        listen_choice = input("Do you want to listen? (y/n): ")
        if listen_choice.lower() == 'y':
            full_news = "\n".join(
                [f"{idx}. {news['title']}. {news['description']}" for idx, news in enumerate(news_list, start=1)])
            speak(full_news)
