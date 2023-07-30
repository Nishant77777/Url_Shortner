import string
import random

class URLShortener:
    def __init__(self):
        self.url_mapping = {}
        self.short_code_length = 6
        self.allowed_chars = string.ascii_letters + string.digits

    def generate_short_code(self):
        return ''.join(random.choice(self.allowed_chars) for _ in range(self.short_code_length))

    def shorten_url(self, long_url):
        short_code = self.generate_short_code()
        self.url_mapping[short_code] = long_url
        return f"http://short.url/{short_code}"


if __name__ == "__main__":
    url_shortener = URLShortener()

    while True:
        print("1. Shorten URL")
        #print("2. Get Long URL")
        print("2. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            long_url = input("Enter the long URL to shorten: ")
            short_url = url_shortener.shorten_url(long_url)
            print(f"Short URL: {short_url}")
       
        elif choice == 2:
            break
        else:
            print("Invalid choice. Try again.")
