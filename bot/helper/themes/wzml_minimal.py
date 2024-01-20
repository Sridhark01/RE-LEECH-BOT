#!/usr/bin/env python3
class WZMLStyle:
    # ----------------------
    # async def start(client, message) ---> __main__.py
    ST_BN1_NAME = '✧ re leech ✧'
    ST_BN1_URL = 'https://t.me/maharaja_91'
    ST_BN2_NAME = 'Updates'
    ST_BN2_URL = 'https://t.me/RE_X_BOTZ'
    ST_MSG = '''<b>ᴛʜɪꜱ ʙᴏᴛ ᴄᴀɴ ᴍɪʀʀᴏʀ ᴀʟʟ ʏᴏᴜʀ ʟɪɴᴋꜱ | ғɪʟᴇꜱ | ᴛᴏʀʀᴇɴᴛꜱ ᴛᴏ ɢᴏᴏɢʟᴇ ᴅʀɪᴠᴇ ᴏʀ ᴀɴʏ ʀᴄʟᴏɴᴇ ᴄʟᴏᴜᴅ ᴏʀ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴍ
ᴛʏᴘᴇ {help_command} ᴛᴏ ɢᴇᴛ ᴀ ʟɪsᴛ ᴏғ ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs</b>'''
    ST_BOTPM = '''<b>ɴᴏᴡ, ᴛʜɪꜱ ʙᴏᴛ ᴡɪʟʟ ꜱᴇɴᴅ ᴀʟʟ ʏᴏᴜʀ ғɪʟᴇꜱ ᴀɴᴅ ʟɪɴᴋꜱ ʜᴇʀᴇ. sᴛᴀʀᴛ ᴜꜱɪɴɢ ...</b>'''
    ST_UNAUTH = '''<i>You Are not authorized user! Deploy your own WZML-X Mirror-Leech bot</i>'''
    OWN_TOKEN_GENERATE = '''<b>Temporary Token is not yours!</b>\n\n<i>Kindly generate your own.</i>'''
    USED_TOKEN = '''<b>Temporary Token already used!</b>\n\n<i>Kindly generate a new one.</i>'''
    LOGGED_PASSWORD = '''<b>Bot Already Logged In via Password</b>\n\n<i>No Need to Accept Temp Tokens.</i>'''
    ACTIVATE_BUTTON = 'Activate Temporary Token'
    TOKEN_MSG = '''<b><u>Generated Temporary Login Token!</u></b>
<b>Temp Token:</b> <code>{token}</code>
<b>Validity:</b> {validity}'''
    # ---------------------
    # async def token_callback(_, query): ---> __main__.py
    ACTIVATED = '✅️ Activated ✅'
    # ---------------------
    # async def login(_, message): --> __main__.py
    LOGGED_IN = '<b>Already Bot Login In!</b>'
    INVALID_PASS = '<b>Invalid Password!</b>\n\nKindly put the correct Password .'
    PASS_LOGGED = '<b>Bot Permanent Login Successfully!</b>'
    LOGIN_USED = '<b>Bot Login Usage :</b>\n\n<code>/cmd [password]</code>'
    # ---------------------
    # async def log(_, message): ---> __main__.py
    LOG_DISPLAY_BT = '📑 Log Display'
    WEB_PASTE_BT = '📨 Web Paste (SB)'
    # ---------------------
    # async def bot_help(client, message): ---> __main__.py
    BASIC_BT = 'Basic'
    USER_BT = 'Users'
    MICS_BT = 'Mics'
    O_S_BT = 'Owner & Sudos'
    CLOSE_BT = 'Close'
    HELP_HEADER = "㊂ <b><i>Help Guide Menu!</i></b>\n\n<b>NOTE: <i>Click on any CMD to see more minor detalis.</i></b>"

    # async def stats(client, message):
    BOT_STATS = '''⌬ <b><i>BOT STATISTICS :</i></b>
┖ <b>Bot Uptime :</b> {bot_uptime}

┎ <b><i>RAM ( MEMORY ) :</i></b>
┃ {ram_bar} {ram}%
┖ <b>U :</b> {ram_u} | <b>F :</b> {ram_f} | <b>T :</b> {ram_t}

┎ <b><i>SWAP MEMORY :</i></b>
┃ {swap_bar} {swap}%
┖ <b>U :</b> {swap_u} | <b>F :</b> {swap_f} | <b>T :</b> {swap_t}

┎ <b><i>DISK :</i></b>
┃ {disk_bar} {disk}%
┃ <b>Total Disk Read :</b> {disk_read}
┃ <b>Total Disk Write :</b> {disk_write}
┖ <b>U :</b> {disk_u} | <b>F :</b> {disk_f} | <b>T :</b> {disk_t}
    
    '''
    SYS_STATS = '''⌬ <b><i>OS SYSTEM :</i></b>
┠ <b>OS Uptime :</b> {os_uptime}
┠ <b>OS Version :</b> {os_version}
┖ <b>OS Arch :</b> {os_arch}

⌬ <b><i>NETWORK STATS :</i></b>
┠ <b>Upload Data:</b> {up_data}
┠ <b>Download Data:</b> {dl_data}
┠ <b>Pkts Sent:</b> {pkt_sent}k
┠ <b>Pkts Received:</b> {pkt_recv}k
┖ <b>Total I/O Data:</b> {tl_data}

┎ <b>CPU :</b>
┃ {cpu_bar} {cpu}%
┠ <b>CPU Frequency :</b> {cpu_freq}
┠ <b>System Avg Load :</b> {sys_load}
┠ <b>P-Core(s) :</b> {p_core} | <b>V-Core(s) :</b> {v_core}
┠ <b>Total Core(s) :</b> {total_core}
┖ <b>Usable CPU(s) :</b> {cpu_use}
    '''
    REPO_STATS = '''⌬ <b><i>REPO STATISTICS :</i></b>
┠ <b>Bot Updated :</b> {last_commit}
┠ <b>Current Version :</b> {bot_version}
┠ <b>Latest Version :</b> {lat_version}
┖ <b>Last ChangeLog :</b> {commit_details}

⌬ <b>REMARKS :</b> <code>{remarks}</code>
    '''
    BOT_LIMITS = '''⌬ <b><i>BOT LIMITATIONS :</i></b>
┠ <b>Direct Limit :</b> {DL} GB
┠ <b>Torrent Limit :</b> {TL} GB
┠ <b>GDrive Limit :</b> {GL} GB
┠ <b>YT-DLP Limit :</b> {YL} GB
┠ <b>Playlist Limit :</b> {PL}
┠ <b>Mega Limit :</b> {ML} GB
┠ <b>Clone Limit :</b> {CL} GB
┖ <b>Leech Limit :</b> {LL} GB

┎ <b>Token Validity :</b> {TV}
┠ <b>User Time Limit :</b> {UTI} / task
┠ <b>User Parallel Tasks :</b> {UT}
┖ <b>Bot Parallel Tasks :</b> {BT}
    '''
    # ---------------------

    # async def restart(client, message): ---> __main__.py
    RESTARTING = '<i>Restarting...</i>'
    # ---------------------

    # async def restart_notification(): ---> __main__.py
    RESTART_SUCCESS = '''⌬ <b><i>Restarted Successfully!</i></b>
┠ <b>Date:</b> {date}
┠ <b>Time:</b> {time}
┠ <b>TimeZone:</b> {timz}
┖ <b>Version:</b> {version}'''
    RESTARTED = '''⌬ <b><i>Bot Restarted!</i></b>'''
    # ---------------------

    # async def ping(client, message): ---> __main__.py
    PING = '<i>Starting Ping..</i>'
    PING_VALUE = '<b>Pong</b>\n<code>{value} ms..</code>'
    # ---------------------

    # async def onDownloadStart(self): --> tasks_listener.py
    LINKS_START = """<b><i>Task Started</i></b>
┠ <b>Mode:</b> {Mode}
┖ <b>By:</b> {Tag}\n\n"""
    LINKS_SOURCE = """➲ <b>Source:</b>
┖ <b>Added On:</b> {On}
------------------------------------------
{Source}
------------------------------------------\n\n"""
    
    # async def __msg_to_reply(self): ---> pyrogramEngine.py
    PM_START =            "➲ <b><u>Task Started :</u></b>\n┃\n┖ <b>Link:</b> <a href='{msg_link}'>Click Here</a>"
    L_LOG_START =           "➲ <b><u>Leech Started :</u></b>\n┃\n┠ <b>User :</b> {mention} ( #ID{uid} )\n┖ <b>Source :</b> <a href='{msg_link}'>Click Here</a>"

    # async def onUploadComplete(): ---> tasks_listener.py
    NAME =                  '<b>✓ ɴᴀᴍᴇ : <code>{Name}</code></b>\n\n'
    SIZE =                  '┠ <b>sɪᴢᴇ : </b><code>{Size}</code>\n'
    ELAPSE =                '┠ <b>ᴇʟᴀᴘsᴇᴅ : </b><code>{Time}</code>\n'
    MODE =                  '┠ <b>ᴍᴏᴅᴇ : </b><code>{Mode}</code>\n'

    # ----- LEECH -------
    L_TOTAL_FILES =         '┠ <b>ᴛᴏᴛᴀʟ ғɪʟᴇs : </b><code>{Files}</code>\n'
    L_CORRUPTED_FILES =     '┠ <b>Corrupted Files: </b><code>{Corrupt}</code>\n'
    L_CC =                  '┖ <b>ᴜᴘʟᴏᴅᴇ ʙʏ: </b><code>{Tag}</code>\n\n'
    PM_BOT_MSG =            '<b>🔰 ғɪʟᴇ (ꜱ) ʜᴀᴠᴇ ʙᴇᴇɴ sᴇɴᴛ above</b>'
    L_BOT_MSG =             '<b>🔰 ғɪʟᴇ (ꜱ) ʜᴀᴠᴇ ʙᴇᴇɴ sᴇɴᴛ ᴛᴏ ʙᴏᴛ ᴘᴍ ᴘʀɪᴠᴀᴛᴇ...</b>'
    L_LL_MSG =              '<b>🔰 ғɪʟᴇ (ꜱ) ʜᴀᴠᴇ ʙᴇᴇɴ sᴇɴᴛ. ᴀᴄᴄᴇꜱꜱ ᴠɪᴀ ʟɪɴᴋꜱ...</b>\n'
    
    # ----- MIRROR -------
    M_TYPE =                '┠ <b>Type: </b>{Mimetype}\n'
    M_SUBFOLD =             '┠ <b>SubFolders: </b>{Folder}\n'
    TOTAL_FILES =           '┠ <b>Files: </b>{Files}\n'
    RCPATH =                '┠ <b>Path: </b><code>{RCpath}</code>\n'
    M_CC =                  '┖ <b>By: </b>{Tag}\n\n'
    M_BOT_MSG =             '➲ <b><i>Link(s) have been Sent to Bot PM (Private)</i></b>'
    # ----- BUTTONS -------
    CLOUD_LINK =      '☁️ Cloud Link'
    SAVE_MSG =        '📨 Save Message'
    RCLONE_LINK =     '♻️ RClone Link'
    DDL_LINK =        '📎 {Serv} Link'
    SOURCE_URL =      '🔐 Source Link'
    INDEX_LINK_F =    '🗂 Index Link'
    INDEX_LINK_D =    '⚡ Index Link'
    VIEW_LINK =       '🌐 View Link'
    CHECK_PM =        '📥 View in Bot PM'
    CHECK_LL =        '🖇 View in Links Log'
    MEDIAINFO_LINK =  '📃 MediaInfo'
    SCREENSHOTS =     '🖼 ScreenShots'
    # ---------------------

    # def get_readable_message(): ---> bot_utilis.py
    ####--------OVERALL MSG HEADER----------
    STATUS_NAME =       '<b>✓ ɴᴀᴍᴇ : <code>{Name}</code></b>'

    #####---------PROGRESSIVE STATUS-------
    BAR =               '\n┃ {Bar}'
    PROCESSED =         '\n┠ <b>ᴘʀᴏᴄᴇssᴇᴅ :</b> {Processed}'
    STATUS =            '\n┠ <b>sᴛᴀᴛᴜs :</b> <a href="{Url}">{Status}</a>'
    ETA =                                                ' | <b>ᴇᴛᴀ :</b> <code>{Eta}</code>'
    SPEED =             '\n┠ <b>sᴘᴇᴇᴅ :</b> <code>{Speed}</code>'
    ELAPSED =                                     ' | <b>ᴇʟᴀᴘsᴇᴅ :</b> {Elapsed}'
    ENGINE =            '\n┠ <b>ᴇɴɢɪɴᴇ :</b> <code>{Engine}</code>'
    STA_MODE =          '\n┠ <b>ᴍᴏᴅᴇ :</b> {Mode}'
    SEEDERS =           '\n┠ <b>Seeders:</b> {Seeders} | '
    LEECHERS =                                           '<b>Leechers:</b> {Leechers}'

    ####--------SEEDING----------
    SEED_SIZE =      '\n┠ <b>Size: </b>{Size}'
    SEED_SPEED =     '\n┠ <b>Speed: </b> {Speed} | '
    UPLOADED =                                     '<b>Uploaded: </b> {Upload}'
    RATIO =          '\n┠ <b>Ratio: </b> {Ratio} | '
    TIME =                                         '<b>Time: </b> {Time}'
    SEED_ENGINE =    '\n┠ <b>Engine:</b> {Engine}'

    ####--------NON-PROGRESSIVE + NON SEEDING----------
    STATUS_SIZE =    '\n┠ <b>Size: </b>{Size}'
    NON_ENGINE =     '\n┠ <b>Engine:</b> {Engine}'

    ####--------OVERALL MSG FOOTER----------
    USER =              '\n┠ <b>User:</b> <code>{User}</code> | '
    ID =                                                        '<b>ID:</b> <code>{Id}</code>'
    BTSEL =          '\n┠ <b>Select:</b> {Btsel}'
    CANCEL =         '\n┖ {Cancel}\n\n'

    ####------FOOTER--------
    FOOTER = '<b>┌────❪ ʙᴏᴛ sᴛᴀᴛᴜs ❫─────༻</b>\n'
    TASKS =  '┠ <b>ᴛᴀsᴋs :</b> <code>{Tasks}</code>\n'
    BOT_TASKS = '┠ <b>ᴛᴀsᴋs :</b> <code>{Tasks}</code>/<code>{Ttask}</code> | <b>ᴀᴠʟ :</b> <code>{Free}</code>\n'
    Cpu = '┠ <b>ᴄᴘᴜ :</b> <code>{cpu}%</code> | '
    FREE =                      '<b>ғʀᴇᴇ :</b> <code>{free}</code> <code>[{free_p}%</code>]'
    Ram = '\n┠ <b>RAM:</b> <code>{ram}%</code> | '
    uptime =                     '<b>ᴜᴘᴛɪᴍᴇ :</b> <code>{uptime}</code>'
    DL = '\n┖ <b>ᴅʟ :</b> <code>{DL}</code>/s | '
    UL =                        '<b>ᴜʟ :</b> <code>{UL}</code>/s\n└──────────────────༻</b>\n'

    ###--------BUTTONS-------
    PREVIOUS = '⇇ ʙᴀᴄᴋ'
    REFRESH = 'ᴘᴀɢᴇs\n{Page}'
    NEXT = 'ɴᴇxᴛ ⇉'
    # ---------------------

    #STOP_DUPLICATE_MSG: ---> clone.py, aria2_listener.py, task_manager.py
    STOP_DUPLICATE = 'File/Folder is already available in Drive.\nHere are {content} list results:'
    # ---------------------

    # async def countNode(_, message): ----> gd_count.py
    COUNT_MSG = '<b>Counting:</b> <code>{LINK}</code>'
    COUNT_NAME = '<b><i>{COUNT_NAME}</i></b>\n┃\n'
    COUNT_SIZE = '┠ <b>Size: </b>{COUNT_SIZE}\n'
    COUNT_TYPE = '┠ <b>Type: </b>{COUNT_TYPE}\n'
    COUNT_SUB =  '┠ <b>SubFolders: </b>{COUNT_SUB}\n'
    COUNT_FILE = '┠ <b>Files: </b>{COUNT_FILE}\n'
    COUNT_CC =   '┖ <b>By: </b>{COUNT_CC}\n'
    # ---------------------

    # LIST ---> gd_list.py
    LIST_SEARCHING = '<b>Searching for <i>{NAME}</i></b>'
    LIST_FOUND = '<b>Found {NO} result for <i>{NAME}</i></b>'
    LIST_NOT_FOUND = 'No result found for <i>{NAME}</i>'
    # ---------------------

    # async def mirror_status(_, message): ----> status.py
    NO_ACTIVE_DL = '''<i>No Active Downloads!</i>
    
⌬ <b><i>Bot Stats</i></b>
┠ <b>CPU:</b> {cpu}% | <b>F:</b> {free} [{free_p}%]
┖ <b>RAM:</b> {ram} | <b>UPTIME:</b> {uptime}
    '''
    # ---------------------

    # USER Setting --> user_setting.py 
    USER_SETTING = '''<b>🌟 ᴜsᴇʀ sᴇᴛᴛɪɴɢs :</b>
        
┏<b>👤 ɴᴀᴍᴇ :</b> {NAME}
┠<b>🔖 ᴜsᴇʀ ɴᴀᴍᴇ :</b> {USERNAME}
┠<b>🔮 ᴛᴇʟᴇɢʀᴀɴ ᴅᴄ :</b> <code>{DC}</code>
┗<b>🗣️ ʟᴀɴɢᴜᴀɢᴇ :</b> <code>{LANG}</code>

🫅 ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ ›› <a href='https://t.me/maharaja_91'>ʀᴀᴊᴀ ᠰ TɢX</a>

'''

    UNIVERSAL = '''<b><u>🌟 ᴜɴɪᴠᴇʀsᴀʟ sᴇᴛᴛɪɴɢs :</u> {NAME}</b>

┎<b> ʏᴛ-ᴅʟᴘ ᴏᴘᴛɪᴏɴs :</b> <b><code>{YT}</code></b>
┠<b> ᴅᴀɪʟʏ ᴛᴀsᴋs :</b> <code>{DT}</code> per day
┠<b> ʟᴀsᴛ ʙᴏᴛ ᴜsᴇᴅ :</b> <code>{LAST_USED}</code>
┠<b> User Session :</b> <code>{USESS}</code>
┠<b> ᴍᴇᴅɪᴀ ɪɴғᴏ ᴍᴏᴅᴇ :</b> <code>{MEDIAINFO}</code>
┠<b> sᴀᴠᴇ ᴍᴏᴅᴇ :</b> <code>{SAVE_MODE}</code>
┖<b> ᴜsᴇʀ ʙᴏᴛ ᴘᴍ :</b> <code>{BOT_PM}</code>

🫅 ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ ›› <a href='https://t.me/maharaja_91'>ʀᴀᴊᴀ ᠰ TɢX</a>

'''

    MIRROR = '''<b><u>🌟 ᴍɪʀʀᴏʀ-ᴄʟᴏɴᴇ sᴇᴛᴛɪɴɢs :</u> {NAME}</b>

┎<b> ᴅᴀɪʟʏ ᴍɪʀʀᴏʀ :</b> <code>{DM}</code> per day
┠<b> ʀᴄʟᴏɴᴇ ᴄᴏɴғɪɢ :</b> <i>{RCLONE}</i>
┠<b> ᴍɪʀʀᴏʀ ᴘʀᴇғɪx :</b> <code>{MPREFIX}</code>
┠<b> Mirror Suffix :</b> <code>{MSUFFIX}</code>
┠<b> Mirror Remname :</b> <code>{MREMNAME}</code>
┠<b> DDL Server(s) :</b> <i>{DDL_SERVER}</i>
┠<b> User TD Mode :</b> <i>{TMODE}</i>
┖<b> Total User TD(s) :</b> <i>{USERTD}</i>'''

    LEECH = '''<b><u>🌟 ʟᴇᴇᴄʜ sᴇᴛᴛɪɴɢs ғᴏʀ</u> - {NAME}</b>

┎<b> ᴅᴀɪʟʏ ʟᴇᴇᴄʜ : </b><code>{DL}</code> per day
┠<b> ʟᴇᴇᴄʜ ᴛʏᴘᴇ : </b> <i>{LTYPE}</i>
┠<b> ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ : </b> <i>{THUMB}</i>
┠<b> ʟᴇᴇᴄʜ sᴘʟɪᴛ sɪᴢᴇ :</b> <code>{SPLIT_SIZE}</code>
┠<b> ᴇǫᴜᴀʟ sᴘʟɪᴛs :</b> <i>{EQUAL_SPLIT}</i>
┠<b> ᴍᴇᴅɪᴀ ɢʀᴏᴜᴘ :</b> <i>{MEDIA_GROUP}</i>
┠<b> ʟᴇᴇᴄʜ ᴄᴀᴘᴛɪᴏɴ :</b> <code>{LCAPTION}</code>
┠<b> ʟᴇᴇᴄʜ ᴘʀᴇғɪx :</b> <code>{LPREFIX}</code>
┠<b> ʟᴇᴇᴄʜ sᴜғғɪx :</b> <code>{LSUFFIX}</code>
┠<b> Leech ᴅᴜᴍᴘs :</b> <code>{LDUMP}</code>
┖<b> ʟᴇᴇᴄʜ ʀᴇᴍᴀɴᴍᴇ :</b> <code>{LREMNAME}</code>'''
