import entertainment_center
import fresh_tomatoes


def main():
    """ Run this file to build the site """
    fresh_tomatoes.open_movies_page(entertainment_center.get_movies())


if __name__ == "__main__":
    main()
