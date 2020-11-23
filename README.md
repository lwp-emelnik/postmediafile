# PostMediaFile

This is a script that takes a video or photo file and posts it to a Telegram chat or/and to a blog. The Media file is posted along with comments to it. The comments should be provided in the metadata in the media file itself or in a [sidecar file](https://en.wikipedia.org/wiki/Sidecar_file).

The script can be used to support the scenario, when a user keeps all their media files and comments to them locally, and posts some of them to the Internet. 

The script is being developed, it is not ready to be used yet.


### Currently supported

* Input files:

    * ACDSee XMP file (with filled "notes" field inside)

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
So just copy needed id into the file `data/config.ini`.

*Note: if you get empty list of chats, just send some dummy message in the needed chat yourself (message should start with `/` character, for example `/hello`).*


#### Blogger

1. [Create new blog](https://www.blogger.com/about/) if not yet created.

2. [Create Google app credentials](https://console.developers.google.com/apis/credentials) if not yet created.

...
