import schedule
import bot.login as l
import bot.hours as h
import connection.database as db


def bot():
    # schedule.every().friday.at('18:00').do(bot)
    schedule.every(10).seconds.do(bot)
    # add login phase
    results = db.selecting()
    for res in results:
        userInput = res[0]
        passInput = res[1]

        print(userInput)
        print(passInput)
        l.login(userInput, passInput)
        h.hours()