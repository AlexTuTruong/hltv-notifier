from dotenv import load_dotenv
import os
import smtplib


carriers = {
    "att": "@mms.att.net",
    "tmobile": " @tmomail.net",
    "verizon": "@vtext.com",
    "sprint": "@page.nextel.com",
    "freedom": "@txt.freedommobile.ca",
}

load_dotenv()
number = os.getenv("NUMBER")
carrier = os.getenv("CARRIER")
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")


def send(message):
    to_number = "{}{}".format(number, carriers[carrier])
    auth = (email, password)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(auth[0], auth[1])

    server.sendmail(auth[0], to_number, message)
    print("Message sent")


def main():
    send("This is a test text!")


if __name__ == "__main__":
    main()
