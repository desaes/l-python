import imaplib
import pprint
import configparser

config = configparser.ConfigParser()
config.read(r'c:\Dev\l-python\lbd\imap\config.ini')


imap_host = config.get("config", "imap_host")
imap_user = config.get("config", "imap_user")
imap_pass = config.get("config", "imap_pass")


with imaplib.IMAP4(imap_host) as imap:
    imap.login(imap_user, imap_pass)

    tmp, data = imap.list()
    print(data)

    imap.select('Inbox')

    tmp, data = imap.search(None, 'ALL')
    for num in data[0].split():
        #tmp, data = imap.fetch(num, '(RFC822)')
        #tmp, data = imap.fetch(num, '(BODY.PEEK[HEADER] FLAGS)')
        tmp, data = imap.fetch(num, 'UID')
        print('Message: {0}\n'.format(num))
        #pprint.pprint(data[0][1])
        pprint.pprint(data)
        #break

    status = imap.status(
            '"{}"'.format('Inbox'),
            '(MESSAGES RECENT UIDNEXT UIDVALIDITY UNSEEN)',)
    #print(status)