from file2 import GreetingCard, BirthdayCard


def main():
    my_greeting = GreetingCard("Lior", "Natan")
    my_birthday = BirthdayCard("Lior", "Natan", 16)

    my_greeting.greeting_msg()
    my_birthday.greeting_msg()


if __name__ == '__main__':
    main()
