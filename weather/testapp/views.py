from django.shortcuts import render
import requests as r
import datetime,calendar
# Create your views 
search_query="hisar"
def demo(request):
	if request.method == 'GET':
		global search_query
		search_query = request.GET.get('search_box')
		print(search_query)
		today = datetime.date.today()
		today=str(today)
		today=str(today)
		born = datetime.datetime.strptime(today,'%Y-%m-%d').weekday()
		k=calendar.day_name[born]
		a=[]
		for x in range(1, 5):
			today = datetime.date.today()
			k1=today + datetime.timedelta(days=x)
			born = datetime.datetime.strptime(str(k1),'%Y-%m-%d').weekday()
			k2=calendar.day_name[born]
			k2=k2[0:3]
			a.append(k2)
		print(a)
		api='http://api.openweathermap.org/data/2.5/forecast?APPID=b20d784cf83f0102efcc1d90dbe3e84d&q='+str(search_query)
		count=0
		b=[]
		json_data=r.get(api).json()
		if(len(json_data)>4):
			for i in range(len(json_data['list'])):
				if(count%8==0):
					clouds=json_data['list'][i]['weather'][0]['description']
					temp=json_data['list'][i]['main']['temp']
					temp=int(int(temp)-273)
					b.append(clouds)
					b.append(temp)
				count=count+1
			print(b)
			cloud=b[0]
			t=b[1]
			return render(request,'testapp/a.html',{'today':today,'t':t,'cloud':cloud,'k':k,'s':search_query,'a':a,'b':b})
		else:
			return render(request,'testapp/b.html')
def home(request):
	today = datetime.date.today()
	today=str(today)
	today=str(today)
	born = datetime.datetime.strptime(today,'%Y-%m-%d').weekday()
	k=calendar.day_name[born]
	a=[]
	for x in range(1, 5):
		today = datetime.date.today()
		k1=today + datetime.timedelta(days=x)
		born = datetime.datetime.strptime(str(k1),'%Y-%m-%d').weekday()
		k2=calendar.day_name[born]
		k2=k2[0:3]
		a.append(k2)
	print(a)
	api='http://api.openweathermap.org/data/2.5/forecast?APPID=b20d784cf83f0102efcc1d90dbe3e84d&q='
	url=api+search_query
	count=0
	b=[]
	json_data=r.get(url).json()
	for i in range(len(json_data['list'])):
		if(count%8==0):
			clouds=json_data['list'][i]['weather'][0]['description']
			temp=json_data['list'][i]['main']['temp']
			temp=int(int(temp)-273)
			b.append(clouds)
			b.append(temp)
		count=count+1
	print(b)
	cloud=b[0]
	t=b[1]
	c=b[2]
	print(type(c))
	return render(request,'testapp/a.html',{'today':today,'t':t,'cloud':cloud,'k':k,'s':search_query,'a':a,'b':b,'c':c})
def oneday(request):
	today = datetime.date.today()
	today=str(today)
	today=str(today)
	born = datetime.datetime.strptime(today,'%Y-%m-%d').weekday()
	k=calendar.day_name[born]
	api='http://api.openweathermap.org/data/2.5/forecast?APPID=b20d784cf83f0102efcc1d90dbe3e84d&q='+str(search_query)
	count=0
	b=[]
	json_data=r.get(api).json()
	c=[]
	for i in range(len(json_data['list'])):
		if(count%1==0):
			clouds=json_data['list'][i]['weather'][0]['description']
			temp=json_data['list'][i]['main']['temp']
			date=json_data['list'][i]['dt_txt']
			c.append(date[12:])
			if(count==1):
				k=date[12:]
			if(c[0]==k):
				break
			else:
				count=1
				temp=int(int(temp)-273)
				b.append(clouds)
				b.append(temp)
				date=json_data['list'][i]['dt_txt']
				b.append(date)
	print(b)
	return render(request,'testapp/c.html',{'today':today,'k':k,'b':b,'s':search_query})	
def rain(request):
	if request.method == 'GET':
		search_query = request.GET.get('search_box')
		mobileno=request.GET.get('number')
		print(mobileno)
		sum=0
		api='http://api.openweathermap.org/data/2.5/forecast?APPID=b20d784cf83f0102efcc1d90dbe3e84d&q='+str(search_query)
		json_data=r.get(api).json()
		count=0
		c=[]
		k=0
		if(len(json_data)>3):
			for i in range(len(json_data)):
				clouds=json_data['list'][i]['weather'][0]['main']
				date=json_data['list'][i]['dt_txt']
				c.append(date[12:])
				if(count==1):
					k=date[12:]
				else:
					count=1
				if(c[0]==k):
					break
				if(clouds=='Rain'):
					k=json_data['list'][i]['rain']['3h']
					print(k)
					sum=sum+k
			if(int(sum)!=0):
				content="Hello Dear,Their is great chance of rain in your area in next 24 hour for more update please visit our site link=https://floodfinal.pythonanywhere.com"
				no=str(mobileno)
				s=r.get('https://www.pay2all.in/web-api/send_sms?api_token=FLlX5miGTcTrpJPWuLjPXKfGSJATKi6utDNJD1lMwDSn1J2gAzd7wVUTXZRa&number='+no+'&senderid=KESHAV&message='+content+'&route=4')
				print(s)
			else:
				content="Hello Dear,Their is nohance of rain in your area in next 24 hour for more update please visit our site link=https://floodfinal.pythonanywhere.com"
				no=str(mobileno)
				s=r.get('https://www.pay2all.in/web-api/send_sms?api_token=FLlX5miGTcTrpJPWuLjPXKfGSJATKi6utDNJD1lMwDSn1J2gAzd7wVUTXZRa&number='+no+'&senderid=KESHAV&message='+content+'&route=4')
				print(s)
			return render(request,'testapp/d.html')
		else:
			return render(request,'testapp/b.html')
	return render(request,'testapp/a.html')