# File-Sharing-Man

Telegram bot to store Posts or Files that can be Accessed via a Special Link.
I Think This Will Be Useful for Many People.

## ⚠️ Disclaimer


```
I am not responsible for the misuse of this bot.
This bot is intended to help store desired files that can be accessed via a Special Link.
Use this bot at your own risk, and use it wisely.
```


### Features
- Fully customizable.
- Can be deployed on Heroku & VPS.
- Customizable welcome messages & force subscriptions.
- More than one Post in One Link (batch).
- Flexible FSUB Button can be 1 button or 2 buttons depending on the filled variable.

### Setup

- Add the bot to the Database Channel with all admin permissions.
- Add the bot to the ForceSub Channel and add the bot as ADMIN.
- Add the bot to the ForceSub Group and add the bot as ADMIN.

## 🛡 Installation
### Deploy on Heroku
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://risman.vercel.app/file-deploy.html)</br>

**Watch This Tutorial Video on YouTube for Help Installing on Heroku**<br>
<a href="https://youtu.be/O2tieQgzYZg">
  <img src="https://img.shields.io/badge/How%20to-Deploy-red?logo=youtube" width="147">
</a><br>

<details>
<summary><h3><b>🔗 Extra Custom & List Vars</b></h3></summary>

### Variables

* `API_HASH` Get API HASH from my.telegram.org.
* `API_ID` Get APP ID from my.telegram.org
* `TG_BOT_TOKEN` Get it from t.me/BotFather
* `OWNER` Input Telegram Username for BOT Owner
* `CHANNEL_ID` Input Channel ID For [Database Channel] example:- -100xxxxxxxx
* `ADMINS` Input User ID to get Admin rights in BOT
* `START_MESSAGE` Optional: /start message to initiate interaction with the bot, Use <a href='https://github.com/mrismanaziz/File-Sharing-Man/blob/main/README.md#start_message'>format</a> parsemode HTML 
* `FORCE_SUB_MESSAGE` Optional: Force Subscribe bot message, Use HTML parsemode format
* `FORCE_SUB_CHANNEL` Input Channel ID for Mandatory Subscription
* `FORCE_SUB_GROUP` Input Group ID for Mandatory Subscription

### Extra Variables

* `CUSTOM_CAPTION` put your Custom Text here if you want to Set Custom Text, You can use HTML and <a href='https://github.com/mrismanaziz/File-Sharing-Man/blob/main/README.md#custom_caption'>fillings</a> for formatting (for documents only)
* `DISABLE_CHANNEL_BUTTON` Input True to Disable the Share button on Channel Posts, Default if False

### Fillings
#### START_MESSAGE | FORCE_SUB_MESSAGE

* `{first}` - User first name
* `{last}` - User last name
* `{id}` - User ID
* `{mention}` - Mention the user
* `{username}` - Username

#### CUSTOM_CAPTION

* `{filename}` - file name of the Document
* `{previouscaption}` - Original Caption

</details>

## 🏷 Support   
- Follow Channel [@Lunatic0de](https://t.me/Lunatic0de) for bot Update info 
- Join Group [@SharingUserbot](https://t.me/SharingUserbot) for discussion, bug reporting, and help about File-Sharing-Man.

## 👨🏻‍💻 Credits

-  [Dan](https://github.com/delivrance) for [Pyrogram](https://github.com/pyrogram/pyrogram)
-  [Risman](https://github.com/mrismanaziz) for [File-Sharing-Man](https://github.com/mrismanaziz/File-Sharing-Man)
-  Based on [CodeXBotz](https://github.com/CodeXBotz) Repo [File-Sharing-Bot](https://github.com/CodeXBotz/File-Sharing-Bot)

## 📑 License
[![GNU GPLv3 Image](https://www.gnu.org/graphics/gplv3-127x51.png)](http://www.gnu.org/licenses/gpl-3.0.en.html)  

[FILE-SHARING-BOT](https://github.com/mrismanaziz/File-Sharing-Man/) is Free Software: You can use, study share and improve it at your
will. Specifically you can redistribute and/or modify it under the terms of the
[GNU General Public License](https://www.gnu.org/licenses/gpl.html) as
published by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version. 

##

   **Give Star to this Repo if You Like it ⭐⭐⭐⭐⭐**
