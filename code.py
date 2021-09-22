import sys,requests,json,os


# get 3 parameter: url,op,file
url = str(input("url:"))
op = str(input("op:"))
file = str(input("file:"))
#  download the file
def download():
	url_download = os.path.join(url,'download/',file)
	folder_path = str(input("folder_path:"))
	download_path = os.path.join('file_path',file)
	r = requests.get(url_download,stream=True)
	print(r)
	f = open(download_path, "wb")
	for chunk in r.iter_content(chunk_size=512):
		if chunk:
			f.write(chunk)
	print("Here is download")

	

#  upload the file
def upload():
	url_upload = os.path.join(url,'upload/')
	files = {'filename': open(file, 'rb')}
	r = requests.post(url_upload,files=files)
	print("Here is upload")
	


#  delete the file
def delete():
	url_delete = os.path.join(url,'deleteFile/',file)
	r = requests.get(url_delete)
	print("Here is delete")


#  list the file
def list():
	url_listFile = os.path.join(url,'listFile/')
	r = requests.get(url_listFile)
	print(r.content)
	print("Here is list")

#  when something is wrong
def call_back():
	print("Something is wrong,please check your inputs and try it again!")

#  choose which op
if op=="download":
	download()
	list()
elif op=="upload":
	upload()
	list()
elif op=="delete":
	delete()
	list()
elif op=="list":
	list()
else:
	call_back()
