import smtplib

carriers = {
    "att": "@mms.att.net",
    "tmobile": " @tmomail.net",
    "verizon": "@vtext.com",
    "sprint": "@page.nextel.com",
    "freedom": "@txt.freedommobile.ca",
}


def send(message):
    to_number = "000-000-0000{}".format(carriers["att"])
    auth = ("**email**", "**password**")

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(auth[0], auth[1])

    server.sendmail(auth[0], to_number, message)
    print("Message sent!")
