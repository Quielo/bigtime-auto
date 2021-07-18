import bot.login as l
import bot.hours as h
import connection.server as s
import schedule


def bot():
    l.login()
    h.hours()


def start():
    s.start_server()
    schedule.every().friday.at('18:00').do(bot)


if __name__ == '__main__':
    start()
