import requests
import urllib.request
import threading
import json

#EDIT THE URL VALUE HERE! I AM NOT TO BE HELD RESPONSIBLE IF YOU SCREW THIS UP! NO SLASH AT THE END!
url = "https://install.appcenter.ms/api/v0.1/apps/keepcoder/telegram-swift/distribution_groups/public"
currentVersion = None
fileName = "file.zip"

def check():
	threading.Timer(60.0, check).start()
	IDGetter = requests.get(f"{url}/public_releases?scope=tester")
	IDJSON = json.loads(IDGetter.text)
	urlForDL = str(IDJSON[0]["id"])

	if not urlForDL == currentVersion:
		print("about to get new version!")
		dlURL = f"{url}/releases/{urlForDL}"
		dlURLGetter = requests.get(dlURL)
		URLJSON = json.loads(dlURLGetter.text)
		theURL = URLJSON["download_url"]
		urlForGet = theURL
		urllib.request.urlretrieve(urlForGet, fileName)
		print("got new version!")

check()