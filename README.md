# PostMediaFile

This is a script that takes a video or photo file and posts it to a Telegram chat or/and to a blog. The Media file is posted along with comments to it. The comments should be provided in the metadata in the media file itself or in a [sidecar file](https://en.wikipedia.org/wiki/Sidecar_file).

The script can be used to support the scenario, when a user keeps all their media files and comments to them locally, and posts some of them to the Internet. 

The script is being developed, it is not ready to be used yet.


### Currently supported

* Input files:

    * ACDSee XMP file (filled "notes" field inside is mandatory, "caption" is optional, filename will be used if caption is not set)

* Output services:

    * Telegram (bot will send the file with description to the specified chat)

    * Blogger (a new post will be created for the specified account) `//in progress//`


### Configuration

#### Telegram

1. [Create new bot](https://core.telegram.org/bots#6-botfather) if not yet created 
 
2. Put the **token** into the configuration file `data/config.ini` below the `[telegram_bot]` section.

3. [Add this bot to the needed group chat](https://stackoverflow.com/questions/37338101/how-to-add-a-bot-to-a-telegram-group) (may differ depending on used Telegram app).

4. To be able to send messages to some chat, id of that chat should be placed to the configuration file.
First of all, you have to run the script with parameter `--list-telegram-chats` where you will see something like this:

   ```
   $ ./run.sh --list-telegram-chats
   ID: 264877391 | Some User
   ID: -469669482 | SomeGroup
   ```
   
    So just copy needed id into the file `data/config.ini`:

   ```
   [telegram_bot]
   token=141....GAU
   chat_id=-469669482
   ```

    *Note: if you get empty list of chats, just send some dummy message in the needed chat yourself (message should start with `/` character, for example `/hello`).*


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
   ```

    Which should show a link and open a web browser (use the link if was not open automatically), where you should log in and grant needed permissions to the application.
    Then copy result code value to the config file:

   ```
   [blogger_post]
   ...
   code=4/1...RA4
   ```
   
   *Note: this action is needed only once, in the future everything will work through that code without any extra interactions.*


#### Install python

1. Go to the [website](https://www.python.org/downloads/), download and install python package (check "Add python to PATH" option).

2. Install all the needed libraries listed in the `requirements.txt` file.
This could be done with python packages manager:

   ```
   pip install -r requirements.txt
   ```


### Usage

After all the configurations are done...
