from tkinter import *
from tkinter import ttk
import json
import requests
root=Tk()
root.overrideredirect(True)
root.geometry("300x200")
root.title("weather app")



label3=Label(root, text="city name", fg="black", font=("times",20))
label3.place(relx=0.5, rely=0.15, anchor=CENTER)

inputbox=Entry(root,)
inputbox.place(relx=0.5, rely=0.3, anchor=CENTER)

label4=Label(root, text=" ", fg="black", font=("times",14))
label4.place(relx=0.7, rely=0.4, anchor=CENTER)

label5=Label(root, text=" ", fg="black", font=("times",14))
label5.place(relx=0.6, rely=0.5, anchor=CENTER)

def cityname():
    api_request=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+inputbox.get()+"&appid=21cab08deb7b27f4c2b55f3e2df28ea4")
    api_request_json=json.loads(api_request.content)
    weatherinfo=api_request_json["weather"][0]["main"]
    humidity=api_request_json["main"]["humidity"]
    label4["text"]="weather="+str(weatherinfo)
    label5["text"]="humidity="+str(humidity)
    label3["text"]=inputbox.get()
    inputbox.destroy()
    button1.destroy()
    
button1=Button(root,text="start",command=cityname,relief=FLAT)
button1.place(relx=0.5, rely=0.6, anchor=CENTER)  



root.mainloop()
        