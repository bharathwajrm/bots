from googletrans import Translator


def translate_text(text, target_language='en'):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text


def main():
    print("Welcome to the Language Translation Bot!")

    while True:
        print("\n1. Translate text")
        print("2. Exit")

        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            text_to_translate = input("Enter the text you want to translate: ")

            print("\nCommonly used languages:")
            print("1. English")
            print("2. French")
            print("3. Spanish")
            print("4. German")
            print("5. Italian")
            print("6. Tamil")
            print("7. Hindi")
            print("8. Custom language (Enter language code)")

            option = input("\nEnter the option number or language code: ")

            if option == '1':
                target_language = 'en'
            elif option == '2':
                target_language = 'fr'
            elif option == '3':
                target_language = 'es'
            elif option == '4':
                target_language = 'de'
            elif option == '5':
                target_language = 'it'
            elif option == '6':
                target_language = 'ta'
            elif option == '7':
                target_language = 'hi'
            elif option == '8':
                target_language = input("Enter the language code: ")
            else:
                print("Invalid option. Translating to English by default.")
                target_language = 'en'

            translated_text = translate_text(text_to_translate, target_language)
            print(f"\nTranslated Text: {translated_text}")

        elif choice == '2':
            print("Thank you for using the Language Translation Bot. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
