import logging
import os

# BASE_DIR = os.path.dirname(__file__)
# logging.basicConfig(level=logging.INFO,
#                     filename=os.path.join(BASE_DIR, 'backupdb.log'),
#                     format='%(asctime)s [%(levelname)s] %(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S')
# log = logging.getLogger("backupdb")

cmdStr = (r'cd {webdir}/db '
          '&& rm -rf db db2'
          '&& dd if=db.txt |openssl des3 -d -k "6yhn(IJN&U*"|tar zxf - '
          '&& mv db db2 '
          '&& [ "x$(diff db2/production.sqlite3 {webdir}/src/mysite/production.sqlite3)" != "x" ] '
          '&& rm -rf {webdir}/db '
          '&& mkdir -p {webdir}/db '
          '&& cp {webdir}/src/mysite/production.sqlite3 {webdir}/db/ '
          '&& cd {webdir}/db '
          '&& rm -rf db.txt '
          '&& tar -zcvf - db|openssl des3 -salt -k "6yhn(IJN&U*" | dd of=db.txt '
          '&& git commit -a -m "routinely update"'
          '&& git push'.format(webdir=r'''{remote_website_dir}'''))

os.system(cmdStr)
