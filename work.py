def set_location():
	self.ip = get('https://api.ipify.org').content.decode('utf8')
	self.location = DbIpCity.get(ip, api_key="free")
	#this method will get the user’s location

def get_api_key():
	# instruct user to make .env file to store in format API_KEY=29374af23 first. Then run this function automatically upon instantiation of class
	load_dotenv()
	api_key = os.getenv("API_KEY")
	#this will set the api key for the user
