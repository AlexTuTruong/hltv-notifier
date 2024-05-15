# HLTV Notifier

HLTV Notifier is a utility you can utilize to send you a text message when your favourite Counter Strike team plays during the day.

[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) is used to scrape the the the games from the front page of [HLTV](https://www.hltv.org/).


The text notifications takes advantage of many carrier's [Email-To-Text support](https://www.att.com/support/article/wireless/KM1061254/), by sending an email to your phone number's mailbox, in turn, sending you a text.

There are some Limitations to SMS, primarily character count (160), this is exaggerated by the carrier also forwarding the sender's email address, as well as the subject line since it is an email, so the ouput message is formatted and truncated to attempt fitiing it within 1 SMS message.

### Installing and running

* Clone this respository
    * HTTPS: `https://github.com/AlexTuTruong/hltv-notifier.git`
    * SSH: `git@github.com:AlexTuTruong/hltv-notifier.git`
    * Github CLI: `gh repo clone AlexTuTruong/hltv-notifier`
* Navigate to the src folder in this repository
    * `cd /path/to/folder/src`
* Install the dependencies
    * `pip install -r requirements.txt`
* Configure your `.env` file
    * You can create a `.env` file or rename the `.env.example` file which already exists within the src folder
        * `TEAM='Virtus.pro'` Enter the team you would like notifications for, exacly as shown on HLTV.org
        * `NUMBER='1234567890'` Enter your number without -'s
        * `CARRIER='freedom'` Carriers supported: att, tmobile, verizon, sprint, freedom
        * `EMAIL='email@gmail.com'` Enter your Gmail address, only gmail smtp supported currently
        * `PASSWORD='use your app password here'` Gmail does not support standard password login, use an app password instead, you can find details on generating one [here](https://support.google.com/accounts/answer/185833?hl=en)
* Run the application
    * You would probably want to run this as a cron job on a server at a set time everyday to notify you appropriately
        *  But to run the script itself, lets say to test it, you can enter `python3 main.py`
    * To schedule a cron job to run the script:
        * Make the script executable: `chmod +x main.py`
        * Open the crontab file: `crontab -e`
        * Add a cron job entry: `0 0 * * * /path/to/main.py` 
            * Note that this example sets the script to run everyday at midnight, you can read [this](https://phoenixnap.com/kb/set-up-cron-job-linux) for further cronjob configuration information
        * Save and exit the crontab file
        * Verify the cron job: `crontab -l` and check if your cron job is there

You can run a cron job on a service like [modal](https://modal.com/) if you don't have a server or computer you'd like to run this on

## Output

Script being run:

```
/hltv-notifier/src$ python3 main.py
sending message:
 Subject: FlyQuest is playing!

vs Vantage @ 05:00
vs Vantage @ 06:00
Message sent
```

Recieved SMS message:

![textexample (Medium)](https://github.com/AlexTuTruong/hltv-notifier/assets/53573114/182855f9-084d-471b-8048-3e763ef0192f)

## License

This project is licensed under the MIT License - see the LICENSE.md file for details
