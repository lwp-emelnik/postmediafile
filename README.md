# PostMediaFile

This is a script that takes a video or photo file and posts it to a Telegram chat or/and to a blog. The Media file is posted along with comments to it. The comments should be provided in the metadata in the media file itself or in a [sidecar file](https://en.wikipedia.org/wiki/Sidecar_file).

The script can be used to support the scenario, when a user keeps all their media files and comments to them locally, and posts some of them to the Internet. 

The script is being developed, it is not ready to be used yet.


### Currently supported

* Input files:

    * ACDSee XMP file (filled "notes" field inside is mandatory, "caption" is optional, file name will be used if caption is not set)

* Output services:

    * Telegram (bot will send the file with description to the specified chat)

    * Blogger (a new post will be created for the specified account) `//in progress//`


### Configuration

#### Telegram

1. [Create new bot](https://core.telegram.org/bots#6-botfather) if not yet created 
 
2. Put the **token** into the configuration file `data/config.ini` below the `[telegram_bot]` section.

3. [Add this bot to the needed chat](https://stackoverflow.com/questions/37338101/how-to-add-a-bot-to-a-telegram-group) (may differ depending on used Telegram app).

4. To be able to send messages to some chat, ID of that chat should be placed in the configuration file first.
For this, you can use the script with parameter `--list-telegram-chats` where you will see something like this:

   ```bash
   $ /path/to/app/run.sh --list-telegram-chats
   # use 'run.bat' for windows #
   ID: 264877391 | Some User
   ID: -469669482 | SomeGroup
   ```
   
    So just copy needed ID into the file `data/config.ini`:

   ```
   [telegram_bot]
   token=141....GAU
   chat_id=-469669482
   ```

    *Note: if you get empty list, just send some dummy message in the needed chat yourself (message should start with `/` character, for example `/hello`) and run the command again.*


#### Blogger

1. [Create new blog](https://www.blogger.com/about/) if not yet created.

2. [Create Google OAuth credentials](https://console.developers.google.com/apis/credentials) if not yet created, it's needed for authorization in [Blogger API](https://developers.google.com/blogger/docs/3.0/using#auth).
Put client id and client secret to the configuration file:

   ```
   [blogger_post]
   client_id=86...1.apps.googleusercontent.com
   client_secret=V_...rRuN
   ```

3. After that you have to authorize via Google, run an app with the `--blogger-login` argument:

   ```
   $ ./run.sh --blogger-login
   # use 'run.bat' for windows #
   Go here if browser was not open automatically: https://accounts.google.com/o/oauth2/auth?client_id=8626...
   Authorize and put fetched code value to the config
   ```

    Which will show you a link and open a web browser (use the link if it was not open automatically), where you should log in and grant needed permissions to the application.
    Then copy result code value to the config file:

   ```
   [blogger_post]
   ...
   code=4/11...asRA4
   ```

   *Note: this action is needed only once, in the future everything will work through the `refresh_token` without any extra interactions.*
   
   *Note: the application should be able to write data to its config file `data/config.ini`, where it will save the `refresh_token` value.*


#### Python (Windows)

1. Go to the [website](https://www.python.org/downloads/), download and install python package (check "Add python to PATH" option).

2. Install all the needed libraries listed in the `requirements.txt` file.
This could be easily done with python package manager (in console):

   ```
   cd X:\path\to\app\
   pip install -r requirements.txt
   ```

    *Note: if you can not run `pip` due to "is not recognized as an internal or external command" error, you have to [configure PATH value](https://stackoverflow.com/questions/23708898/pip-is-not-recognized-as-an-internal-or-external-command) additionally.*


### Usage

After all the configurations are done...
