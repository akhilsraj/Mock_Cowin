# No other modules apart from 'socket', 'BeautifulSoup', 'requests' and 'datetime'
# need to be imported as they aren't required to solve the assignment

# Import required module/s
import socket
from bs4 import BeautifulSoup
import requests
import datetime


# Define constants for IP and Port address of Server
# NOTE: DO NOT modify the values of these two constants
HOST = '127.0.0.1'
PORT = 24680


def fetchWebsiteData(url_website):
	"""Fetches rows of tabular data from given URL of a website with data excluding table headers.

	Parameters
	----------
	url_website : str
		URL of a website

	Returns
	-------
	bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	"""
	
	web_page_data = ''

	##############	ADD YOUR CODE HERE	##############
	
	page = requests.get(url_website)
	soup = BeautifulSoup(page.content, 'html.parser')
	web_page_data = soup.find_all('tbody')
	##################################################

	return web_page_data


def fetchVaccineDoses(web_page_data):
	"""Fetch the Vaccine Doses available from the Web-page data and provide Options to select the respective Dose.

	Parameters
	----------
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers

	Returns
	-------
	dict
		Dictionary with the Doses available and Options to select, with Key as 'Option' and Value as 'Command'
	
	Example
	-------
	>>> url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	>>> web_page_data = fetchWebsiteData(url_website)
	>>> print(fetchVaccineDoses(web_page_data))
	{'1': 'Dose 1', '2': 'Dose 2'}
	"""

	vaccine_doses_dict = {}

	##############	ADD YOUR CODE HERE	##############
	for i in web_page_data:
		X = (i.find_all(attrs={"class":"dose_num"}))
		for i in X:
			vaccine_doses_dict[str(int(i.text))]="Dose {}".format(i.text)
	

	##################################################

	return vaccine_doses_dict


def fetchAgeGroup(web_page_data, dose):
	"""Fetch the Age Groups for whom Vaccination is available from the Web-page data for a given Dose
	and provide Options to select the respective Age Group.

	Parameters
	----------
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	dose : str
		Dose available for Vaccination and its availability for the Age Groups

	Returns
	-------
	dict
		Dictionary with the Age Groups (for whom Vaccination is available for a given Dose) and Options to select,
		with Key as 'Option' and Value as 'Command'
	
	Example
	-------
	>>> url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	>>> web_page_data = fetchWebsiteData(url_website)
	>>> print(fetchAgeGroup(web_page_data, '1'))
	{'1': '18+', '2': '45+'}
	>>> print(fetchAgeGroup(web_page_data, '2'))
	{'1': '18+', '2': '45+'}
	"""

	age_group_dict = {}

	##############	ADD YOUR CODE HERE	##############
	ages=set()	
	for i in web_page_data:
		doses=i.find_all('td',attrs={'class':'dose_num'})
		age=i.find_all('td',attrs={'class':'age'})
		for j in range(len(age)):
			if(doses[j].text==dose):
				ages.add(age[j].text)
	ages=sorted(list(ages))
	for i in range(len(ages)):
		age_group_dict[str(i+1)]=ages[i]
	##################################################
	return age_group_dict


def fetchStates(web_page_data, age_group, dose):
	"""Fetch the States where Vaccination is available from the Web-page data for a given Dose and Age Group
	and provide Options to select the respective State.

	Parameters
	----------
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	age_group : str
		Age Group available for Vaccination and its availability in the States
	dose : str
		Dose available for Vaccination and its availability for the Age Groups

	Returns
	-------
	dict
		Dictionary with the States (where the Vaccination is available for a given Dose, Age Group) and Options to select,
		with Key as 'Option' and Value as 'Command'
	
	Example
	-------
	>>> url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	>>> web_page_data = fetchWebsiteData(url_website)
	>>> print(fetchStates(web_page_data, '18+', '1'))
	{
		'1': 'Andhra Pradesh', '2': 'Arunachal Pradesh', '3': 'Bihar', '4': 'Chandigarh', '5': 'Delhi', '6': 'Goa',
		'7': 'Gujarat', '8': 'Harayana', '9': 'Himachal Pradesh', '10': 'Jammu and Kashmir', '11': 'Kerala', '12': 'Telangana'
	}
	"""

	states_dict = {}

	##############	ADD YOUR CODE HERE	##############
	c = []
	for i in web_page_data:
		Y = (i.find_all(attrs={"class":"dose_num"}))
		X = (i.find_all(attrs={"class":"age"}))
		Z = (i.find_all(attrs={"class":"state_name"}))
		for i,j,k in zip(X,Y,Z):
			if((str(i.text)==age_group) and (str(j.text) == dose)):
				c.append(str(k.text))
	c.sort()
	for i in range(1,len(c)+1):
		states_dict[str(i)] = c[i-1]
	
	##################################################
	return states_dict


def fetchDistricts(web_page_data, state, age_group, dose):
	"""Fetch the District where Vaccination is available from the Web-page data for a given State, Dose and Age Group
	and provide Options to select the respective District.

	Parameters
	----------
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	state : str
		State where Vaccination is available for a given Dose and Age Group
	age_group : str
		Age Group available for Vaccination and its availability in the States
	dose : str
		Dose available for Vaccination and its availability for the Age Groups

	Returns
	-------
	dict
		Dictionary with the Districts (where the Vaccination is available for a given State, Dose, Age Group) and Options to select,
		with Key as 'Option' and Value as 'Command'
	
	Example
	-------
	>>> url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	>>> web_page_data = fetchWebsiteData(url_website)
	>>> print(fetchDistricts(web_page_data, 'Ladakh', '18+', '2'))
	{
		'1': 'Kargil', '2': 'Leh'
	}
	"""

	districts_dict = {}

	##############	ADD YOUR CODE HERE	##############
	c = []
	for i in web_page_data:
		Y = (i.find_all(attrs={"class":"dose_num"}))
		X = (i.find_all(attrs={"class":"age"}))
		Z = (i.find_all(attrs={"class":"state_name"}))
		A = (i.find_all(attrs={"class":"district_name"}))
		for v,j,k,p in zip(X,Y,Z,A):
			if((str(v.text)==age_group) and (str(j.text) == dose) and (str(k.text) == state)):
				c.append(str(p.text))
	c.sort()
	for i in range(1,len(c)+1):
		districts_dict[str(i)] = c[i-1]
	

	##################################################

	return districts_dict


def fetchHospitalVaccineNames(web_page_data, district, state, age_group, dose):
	"""Fetch the Hospital and the Vaccine Names from the Web-page data available for a given District, State, Dose and Age Group
	and provide Options to select the respective Hospital and Vaccine Name.

	Parameters
	----------
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	district : str
		District where Vaccination is available for a given State, Dose and Age Group
	state : str
		State where Vaccination is available for a given Dose and Age Group
	age_group : str
		Age Group available for Vaccination and its availability in the States
	dose : str
		Dose available for Vaccination and its availability for the Age Groups

	Returns
	-------
	dict
		Dictionary with the Hosptial and Vaccine Names (where the Vaccination is available for a given District, State, Dose, Age Group)
		and Options to select, with Key as 'Option' and Value as another dictionary having Key as 'Hospital Name' and Value as 'Vaccine Name'
	
	Example
	-------
	>>> url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	>>> web_page_data = fetchWebsiteData(url_website)
	>>> print(fetchHospitalVaccineNames(web_page_data, 'Kargil', 'Ladakh', '18+', '2'))
	{
		'1': {
				'MedStar Hospital Center': 'Covaxin'
			}
	}
	>>> print(fetchHospitalVaccineNames(web_page_data, 'South Goa', 'Goa', '45+', '2'))
	{
		'1': {
				'Eden Clinic': 'Covishield'
			}
	}
	"""
	
	hospital_vaccine_names_dict = {}

	##############	ADD YOUR CODE HERE	##############
	c = []
	h = []
	my_dict = dict
	for i in web_page_data:
		Y = (i.find_all(attrs={"class":"dose_num"}))
		X = (i.find_all(attrs={"class":"age"}))
		Z = (i.find_all(attrs={"class":"state_name"}))
		A = (i.find_all(attrs={"class":"district_name"}))
		B = (i.find_all(attrs={"class":"hospital_name"}))
		C = (i.find_all(attrs={"class":"vaccine_name"}))
		for v,j,k,p,n,q in zip(X,Y,Z,A,B,C):
			if((str(v.text)==age_group) and (str(j.text) == dose) and (str(k.text) == state) and (str(p.text) == district)):
				c.append(str(n.text))
				h.append(str(q.text))
	zip_iterator = zip(c, h)
	u = dict(zip_iterator)
	x =[]
	for i in range(1,len(u)+1):
		x.append(str(i))
	for key, ele in zip(x, u.items()):
    		hospital_vaccine_names_dict[key] = dict([ele])
	##################################################

	return hospital_vaccine_names_dict

def fetchVaccineSlots(web_page_data, hospital_name, district, state, age_group, dose):
	"""Fetch the Dates and Slots available on those dates from the Web-page data available for a given Hospital Name, District, State, Dose and Age Group
	and provide Options to select the respective Date and available Slots.

	Parameters
	----------
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	hospital_name : str
		Name of Hospital where Vaccination is available for given District, State, Dose and Age Group
	district : str
		District where Vaccination is available for a given State, Dose and Age Group
	state : str
		State where Vaccination is available for a given Dose and Age Group
	age_group : str
		Age Group available for Vaccination and its availability in the States
	dose : str
		Dose available for Vaccination and its availability for the Age Groups

	Returns
	-------
	dict
		Dictionary with the Dates and Slots available on those dates (where the Vaccination is available for a given Hospital Name,
		District, State, Dose, Age Group) and Options to select, with Key as 'Option' and Value as another dictionary having
		Key as 'Date' and Value as 'Available Slots'
	
	Example
	-------
	>>> url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	>>> web_page_data = fetchWebsiteData(url_website)
	>>> print(fetchVaccineSlots(web_page_data, 'MedStar Hospital Center', 'Kargil', 'Ladakh', '18+', '2'))
	{
		'1': {'May 15': '0'}, '2': {'May 16': '81'}, '3': {'May 17': '109'}, '4': {'May 18': '78'},
		'5': {'May 19': '89'}, '6': {'May 20': '57'}, '7': {'May 21': '77'}
	}
	>>> print(fetchVaccineSlots(web_page_data, 'Eden Clinic', 'South Goa', 'Goa', '45+', '2'))
	{
		'1': {'May 15': '0'}, '2': {'May 16': '137'}, '3': {'May 17': '50'}, '4': {'May 18': '78'},
		'5': {'May 19': '145'}, '6': {'May 20': '64'}, '7': {'May 21': '57'}
	}
	"""

	vaccine_slots = {}

	##############	ADD YOUR CODE HERE	##############
	dates=['May 15','May 16','May 17','May 18','May 19','May 20','May 21']
	slots=[]	
	for i in web_page_data:
		doses=i.find_all('td',attrs={'class':'dose_num'})
		age=i.find_all('td',attrs={'class':'age'})
		state_name=i.find_all('td',attrs={'class':'state_name'})
		district_name=i.find_all('td',attrs={'class':'district_name'})
		hospital_names=i.find_all('td',attrs={'class':'hospital_name'})
		May_15=i.find_all('td',attrs={'class':'may_15'})
		May_16=i.find_all('td',attrs={'class':'may_16'})
		May_17=i.find_all('td',attrs={'class':'may_17'})
		May_18=i.find_all('td',attrs={'class':'may_18'})
		May_19=i.find_all('td',attrs={'class':'may_19'})
		May_20=i.find_all('td',attrs={'class':'may_20'})
		May_21=i.find_all('td',attrs={'class':'may_21'})
	
		for j in range(len(age)):
			if(doses[j].text==dose and age[j].text==age_group and state_name[j].text==state and district_name[j].text==district and hospital_names[j].text==hospital_name):
				slots.extend([May_15[j].text,May_16[j].text,May_17[j].text,May_18[j].text,May_19[j].text,May_20[j].text,May_21[j].text])
	slots=list(slots)

	for i in range(len(slots)):
		vaccine_slots[str(i+1)]={dates[i]:slots[i]}
	##################################################

	return vaccine_slots


def openConnection():
	"""Opens a socket connection on the HOST with the PORT address.

	Returns
	-------
	socket
		Object of socket class for the Client connected to Server and communicate further with it
	tuple
		IP and Port address of the Client connected to Server
	"""

	client_socket = None
	client_addr = None

	##############	ADD YOUR CODE HERE	##############
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	    s.bind((HOST, PORT))
	    s.listen()
	    client_socket, client_addr = s.accept()
	##################################################
	
	return client_socket, client_addr


def startCommunication(client_conn, client_addr, web_page_data):
	"""Starts the communication channel with the connected Client for scheduling an Appointment for Vaccination.

	Parameters
	----------
	client_conn : socket
		Object of socket class for the Client connected to Server and communicate further with it
		IP and Port address of the Client connected to Server
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	"""

	##############	ADD YOUR CODE HERE	##############
	with client_conn:
		flag = True
		print('Client is connected at:  ', client_addr)
		count = 0
		client_conn.sendall(bytes("============================",'utf-8'))
		client_conn.sendall(bytes("\n# Welcome to CoWIN ChatBot #\n",'utf-8'))
		client_conn.sendall(bytes("============================\n",'utf-8'))
		client_conn.sendall(bytes("Schedule an Appointment for Vaccination:\n",'utf-8'))
		count = 0
		online = 1
		client_conn,count,dose,online = get_dose(client_conn,count,web_page_data,online)
		count = 0
		if(online):
			age_group,online = get_age(client_conn,count,dose,web_page_data,online)
		count = 0
		if(online):
			state,online = get_state(client_conn,count,dose,web_page_data,age_group,online)
		count = 0
		if(online):
			district,online = get_district(client_conn,count,dose,web_page_data,age_group,state,online)
		count = 0
		if(online):
			hospital_name,online = get_hostpital(client_conn,count,dose,web_page_data,age_group,state,district,online)
		count =0
		if(online):
			get_slots(client_conn,count,dose,web_page_data,age_group,state,district,hospital_name,online)


	##################################################


def stopCommunication(client_conn):
	"""Stops or Closes the communication channel of the Client with a message.

	Parameters
	----------
	client_conn : socket
		Object of socket class for the Client connected to Server and communicate further with it
	"""

	##############	ADD YOUR CODE HERE	##############
	client_conn.shutdown(socket.SHUT_RDWR)
	##################################################


################# ADD UTILITY FUNCTIONS HERE #################
## You can define any utility functions for your code.      ##
## Please add proper comments to ensure that your code is   ##
## readable and easy to understand.                         ##
##############################################################
def get_dose(client_conn,count,web_page_data,online):
	client_conn.sendall(bytes(">>> Select the Dose of Vaccination:\n{}\n".format(fetchVaccineDoses(web_page_data)),'utf-8'))
	dose = client_conn.recv(1024).decode('utf-8')
	if((str(dose) == str(1))):
		client_conn.sendall(bytes("<<< Dose selected: {}\n".format(dose),'utf-8'))
		print("Dose selected: ",dose)
		return client_conn,count,dose,online
	elif(str(dose) == str(2)):
		print("Dose selected: ",dose)
		client_conn,count,dose,online = get_date(client_conn,dose,count,online)
		count = 0
		return client_conn,count,dose,online
	elif((str(dose) == 'b') or (str(dose) == 'B')):
		count = 0
		return(get_dose(client_conn,count,web_page_data,online))
	elif((str(dose) == 'q') or (str(dose) == 'Q')):
		client_conn.close()
		online = 0
		return client_conn,count,dose,online
	else:
		count = count + 1;
		client_conn.sendall(bytes("<<< Invalid input provided {} time(s)! Try again.\n".format(count),'utf-8'))
		print("Invalid input detected {} time(s)!".format(count))
		if(count == 3):
			count = 0
			client_conn.sendall(bytes("<<< See ya! Visit again :)",'utf-8'))
			print("Notifying the client and closing the connection!")
			client_conn.close()
			online = 0 
			dose = None
			return client_conn,count,dose,online
		return(get_dose(client_conn,count,web_page_data,online))
def get_age(client_conn,count,dose,web_page_data,online):
	client_conn.sendall(bytes(">>> Select the Age Group:\n{}\n".format(fetchAgeGroup(web_page_data, dose)),'utf-8'))
	x = client_conn.recv(1024).decode('utf-8')
	if((str(x) == "1") or (str(x) == "2")):
		age_group = str(fetchAgeGroup(web_page_data, dose)[x])
		client_conn.sendall(bytes("<<< Selected Age Group: {}".format(age_group),'utf-8'))
		print("Age Group selected:  {}".format(age_group))
		return age_group,online
	elif((str(x) == 'b') or (str(x) == 'B')):
		client_conn,count,dose,online = get_dose(client_conn,count,web_page_data,online)
		count = 0
		return(get_age(client_conn,count,dose,web_page_data,online))
	elif((str(x) == 'q') or (str(x) == 'Q')):
		client_conn.close()
		online = 0
		age_group = None
		return age_group,online
	else:
		count = count + 1;
		client_conn.sendall(bytes("<<< Invalid input provided {} time(s)! Try again.\n".format(count),'utf-8'))
		print("Invalid input detected {} time(s)!".format(count))
		if(count == 3):
			count = 0
			client_conn.sendall(bytes("<<< See ya! Visit again :)",'utf-8'))
			print("Notifying the client and closing the connection!")
			client_conn.close() 
			online =0
			age_group = None
			return age_group,online
		return(get_age(client_conn,count,dose,web_page_data,online))
def get_state(client_conn,count,dose,web_page_data,age_group,online):
	client_conn.sendall(bytes(">>> Select the State:\n{}\n".format(fetchStates(web_page_data, age_group,dose)),'utf-8'))
	x = client_conn.recv(1024).decode('utf-8')
	if x in fetchStates(web_page_data, age_group, dose).keys():
		state = str(fetchStates(web_page_data, age_group, dose)[x])
		client_conn.sendall(bytes("<<< Selected State: {}\n".format(state),'utf-8'))
		print("State selected:  {}".format(state))
		return state,online
	elif((str(x) == 'b') or (str(x) == 'B')):
		client_conn,count,dose,online = get_dose(client_conn,count,web_page_data,online)
		count = 0
		age_group,online = get_age(client_conn,count,dose,web_page_data,online)
		return(get_state(client_conn,count,dose,web_page_data,age_group,online))
	elif((str(x) == 'q') or (str(x) == 'Q')):
		client_conn.close()
		online = 0
		state = None
		return state,online
	else:
		count = count + 1;
		client_conn.sendall(bytes("<<< Invalid input provided {} time(s)! Try again.\n".format(count),'utf-8'))
		print("Invalid input detected {} time(s)!".format(count))
		if(count == 3):
			count = 0
			client_conn.sendall(bytes("<<< See ya! Visit again :)",'utf-8'))
			print("Notifying the client and closing the connection!")
			client_conn.close()
			online = 0 
			state = None
			return state,online
		return(get_state(client_conn,count,dose,web_page_data,age_group,online))
def get_district(client_conn,count,dose,web_page_data,age_group,state,online):
	client_conn.sendall(bytes(">>> Select the District:\n{}".format(fetchDistricts(web_page_data, state, age_group, dose)),'utf-8'))
	x = client_conn.recv(1024).decode('utf-8')
	if x in fetchDistricts(web_page_data, state, age_group, dose).keys():	
		district = str(fetchDistricts(web_page_data, state, age_group, dose)[x])
		client_conn.sendall(bytes("<<< Selected District: {}\n".format(district),'utf-8'))
		print("District selected:  {}".format(district))
		return district,online
	elif((str(x) == 'b') or (str(x) == 'B')):
		client_conn,count,dose,online = get_dose(client_conn,count,web_page_data,online)
		count = 0
		age_group,online = get_age(client_conn,count,dose,web_page_data,online)
		count = 0
		state,online = get_state(client_conn,count,dose,web_page_data,age_group,online)
		count = 0
		return(get_district(client_conn,count,dose,web_page_data,age_group,state,online))
	elif((str(x) == 'q') or (str(x) == 'Q')):
		client_conn.close()
		online = 0
		return district,online
	else:
		count = count + 1;
		client_conn.sendall(bytes("<<< Invalid input provided {} time(s)! Try again.\n".format(count),'utf-8'))
		print("Invalid input detected {} time(s)!".format(count))
		if(count == 3):
			count = 0
			client_conn.sendall(bytes("<<< See ya! Visit again :)",'utf-8'))
			print("Notifying the client and closing the connection!")
			client_conn.close()
			online = 0
			district = None 
			return district,online
		return(get_district(client_conn,count,dose,web_page_data,age_group,state,online))
def get_hostpital(client_conn,count,dose,web_page_data,age_group,state,district,online):
	client_conn.sendall(bytes(">>> Select the Vaccination Center Name:\n{}\n".format(fetchHospitalVaccineNames(web_page_data, district, state, age_group, dose)),'utf-8'))
	x = client_conn.recv(1024).decode('utf-8')
	if x in fetchHospitalVaccineNames(web_page_data, district, state, age_group, dose).keys():
		hospital_name = (fetchHospitalVaccineNames(web_page_data, district, state, age_group, dose)[x])
		client_conn.sendall(bytes("<<< Selected Vaccination Center: {}\n".format(list(hospital_name.keys())),'utf-8'))
		print("Hospital selected:  {}".format((hospital_name)))
		return hospital_name,online
	elif((str(x) == 'b') or (str(x) == 'B')):
		client_conn,count,dose,online = get_dose(client_conn,count,web_page_data,online)
		count = 0
		age_group,online = get_age(client_conn,count,dose,web_page_data,online)
		count = 0
		state,online = get_state(client_conn,count,dose,web_page_data,age_group,online)
		count = 0
		district,online = (get_district(client_conn,count,dose,web_page_data,age_group,state,online))
		count = 0
		return(get_hostpital(client_conn,count,dose,web_page_data,age_group,state,district,online))
	elif((str(x) == 'q') or (str(x) == 'Q')):
		client_conn.close()
		online = 0
		hospital_name = None
		return hospital_name,online
	else:
		count = count + 1;
		client_conn.sendall(bytes("<<< Invalid input provided {} time(s)! Try again.\n".format(count),'utf-8'))
		print("Invalid input detected {} time(s)!".format(count))
		if(count == 3):
			count = 0
			client_conn.sendall(bytes("<<< See ya! Visit again :)",'utf-8'))
			print("Notifying the client and closing the connection!")
			client_conn.close() 
			online = 0
			return hospital_name,online
		return(get_hostpital(client_conn,count,dose,web_page_data,age_group,state,district,online))
def get_slots(client_conn,count,dose,web_page_data,age_group,state,district,hospital_name,online):
	client_conn.sendall(bytes(">>> Select one of the available slots to schedule the Appointment:\n{}".format(fetchVaccineSlots(web_page_data, list(hospital_name.keys())[0], district, state, age_group, dose)),'utf-8'))
	x = client_conn.recv(1024).decode('utf-8')
	if x in list(fetchVaccineSlots(web_page_data,list(hospital_name.keys())[0], district, state, age_group, dose).keys()):
		slot = fetchVaccineSlots(web_page_data, list(hospital_name.keys())[0], district, state, age_group, dose)[x]
		client_conn.sendall(bytes("<<< Selected Vaccination Appoitnment Date: {}".format(list(slot.keys())[0]),'utf-8'))
		client_conn.sendall(bytes("<<< Available Slots on the selected Date: {}".format(list(slot.values())[0]),'utf-8'))
		print("Vaccination Date selected:  {}".format(list(slot.keys())[0]))
		print("Available Slots on that date:  {}".format(list(slot.values())[0]))
		client_conn.sendall(bytes("<<< Your appointment is scheduled. Make sure to carry ID Proof while you visit Vaccination Center!",'utf-8'))
		client_conn.sendall(bytes("<<< See ya! Visit again :)",'utf-8'))
	elif((str(x) == 'b') or (str(x) == 'B')):
		client_conn,count,dose,online = get_dose(client_conn,count,web_page_data,online)
		count = 0
		age_group,online = get_age(client_conn,count,dose,web_page_data,online)
		count = 0
		state,online = get_state(client_conn,count,dose,web_page_data,age_group,online)
		count = 0
		district,online = get_district(client_conn,count,dose,web_page_data,age_group,state,online)
		count = 0
		hospital_name,online = get_hostpital(client_conn,count,dose,web_page_data,age_group,state,district,online)
		count = 0
		return 0
	elif((str(x) == 'q') or (str(x) == 'Q')):
		client_conn.close()
		online = 0
		return 0
	else:
		count = count + 1;
		client_conn.sendall(bytes("<<< Invalid input provided {} time(s)! Try again.\n".format(count),'utf-8'))
		print("Invalid input detected {} time(s)!".format(count))
		if(count == 3):
			count = 0
			client_conn.sendall(bytes("<<< See ya! Visit again :)",'utf-8'))
			print("Notifying the client and closing the connection!")
			client_conn.close()
			online =0 
			return 0
		return(get_slots(client_conn,count,dose,web_page_data,age_group,state,district,hospital_name,online))
def get_date(client_conn,dose,count,online):
	client_conn.sendall(bytes(">>> Provide the date of First Vaccination Dose (DD/MM/YYYY), for e.g. 12/5/2021",'utf-8'))
	x = client_conn.recv(1024).decode('utf-8')
	format = "%d/%m/%Y"
	isValidDate = True
	try :
	    datetime.datetime.strptime(x, format)
	except ValueError :
	    isValidDate = False
	if (isValidDate):
		client_conn.sendall(bytes("<<< Date of First Vaccination Dose provided: {}".format(x),'utf-8'))
		x = x.split('/')
		date = datetime.date(int(x[2]),int(x[1]),int(x[0]))
		date_today = datetime.date.today()
		days = abs(date - date_today).days
		weeks = days//7
		if(weeks < 4):
			client_conn.sendall(bytes("<<< You are not eligible right now for 2nd Vaccination Dose! Try after {} weeks.".format(4-int(weeks)),'utf-8'))
			client_conn.sendall(bytes("<<< See ya! Visit again :)",'utf-8'))
			client_conn.close()
			online = 0
			return client_conn,count,dose,online
		elif((weeks >=4) and (weeks <= 8)):
			client_conn.sendall(bytes("<<< You are eligible for 2nd Vaccination Dose and are in the right time-frame to take it.",'utf-8'))
			client_conn.sendall(bytes("<<< Number of weeks from today: {}".format(weeks),'utf-8'))
			
			return client_conn,count,dose,online
		else:
			client_conn.sendall(bytes("<<< You have been late in scheduling your 2nd Vaccination Dose by {} weeks.".format(int(weeks) - 8),'utf-8'))
			return client_conn,count,dose,online
	else:
		if((str(x) == 'b') or (str(x) == 'B')):
			client_conn,count,dose,online = get_dose(client_conn,count,web_page_data,online)
			count = 0
			return client_conn,count,dose,online
		elif((str(x) == 'q') or (str(x) == 'Q')):
			client_conn.close()
			online = 0
			return client_conn,count,dose,online
		else:
			count = count + 1;
			client_conn.sendall(bytes("<<< Invalid input provided {} time(s)! Try again.\n".format(count),'utf-8'))
			print("Invalid input detected {} time(s)!".format(count))
			if(count == 3):
				count = 0
				client_conn.sendall(bytes("<<< See ya! Visit again :)",'utf-8'))
				print("Notifying the client and closing the connection!")
				client_conn.close()
				online = 0 
				dose = None
				return client_conn,count,dose,online
			return get_date(client_conn,dose,count,online)
		
##############################################################


if __name__ == '__main__':
	"""Main function, code begins here
	"""
	url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	web_page_data = fetchWebsiteData(url_website)
	client_conn, client_addr = openConnection()
	startCommunication(client_conn, client_addr, web_page_data)

