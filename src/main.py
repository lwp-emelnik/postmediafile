import sys
import webbrowser

from config.ini_config import IniConfig
from input.acdsee_xmp import ACDSeeXmp
from output.telegram_bot import TelegramBot
from output.blogger_post import BloggerPost


def main(argv):
    config = IniConfig()
    telegram_bot = TelegramBot(config.get_config('telegram_bot'))
    blogger_post = BloggerPost(config.get_config('blogger_post'))

    if len(argv) != 2:
        print_help(argv[0])
        return

    if argv[1] == '--list-telegram-chats':
        list_telegram_chats(telegram_bot)
    elif argv[1] == '--blogger-login':
        print_blogger_auth_url(blogger_post)
    else:
        input_file_name = argv[1]
        try:
            input_file = open(input_file_name, 'r')
            input_file_content = input_file.read()
        except OSError:
            print('Could not open/read file:', input_file_name)
            return

        input_data = ACDSeeXmp(input_file_name, input_file_content)
        input_data_parsed = input_data.get_parsed_data()

        #telegram_bot.send_data(input_data_parsed)
        #print('Successfully sent via Telegram API!')

        result_link = blogger_post.create_post(input_data_parsed)
        print('Successfully created post via Blogger API:', result_link)


def print_help(executable):
    print('usage:', executable, '<input_file_path>')


def list_telegram_chats(telegram_bot):
    for update in telegram_bot.get_updates():
        if update['message']['chat']['type'] == 'group':
            title = update['message']['chat']['title']
        else:
            title = update['message']['chat']['first_name'] + ' ' + update['message']['chat']['last_name']
        print('ID:', update['message']['chat']['id'], '|', title)


def print_blogger_auth_url(blogger_post):
    auth_uri = blogger_post.get_auth_uri()
    print('Go here if browser was not open automatically:', auth_uri)
    print('Authorize and put fetched code value to the config')
    webbrowser.open(auth_uri)


if __name__ == "__main__":
    try:
        main(sys.argv)
    except Exception as e:
        print('EXCEPTION occurred:', e)
