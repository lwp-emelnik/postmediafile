import sys

from config.ini_config import IniConfig
from input.acdsee_xmp import ACDSeeXmp
from output.telegram_bot import TelegramBot


def main(argv):
    config = IniConfig()
    telegram_bot = TelegramBot(config.get_config('telegram_bot'))

    if len(argv) != 2:
        print_help(argv[0])
        return

    if argv[1] == '--list-telegram-chats':
        for update in telegram_bot.get_updates():
            if update['message']['chat']['type'] == 'group':
                title = update['message']['chat']['title']
            else:
                title = update['message']['chat']['first_name'] + ' ' + update['message']['chat']['last_name']
            print('ID:', update['message']['chat']['id'], '|', title)
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


def print_help(executable):
    print('usage:', executable, '<input_file_path>')


if __name__ == "__main__":
    try:
        main(sys.argv)
    except Exception as e:
        print('EXCEPTION occurred:', e)
