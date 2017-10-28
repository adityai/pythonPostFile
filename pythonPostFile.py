import requests
import sys

def main():
	url = 'https://www.google.com/search?q=test&oq=test'
	files = {'data': open('requirements.txt', 'rb')}
	r = requests.post(url, files=files)
	print (r.status_code)

main()
chmod 755 PythonVirtualEnv/PythonVirtualEnvInstaller.sh
