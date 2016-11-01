# -*- coding: utf-8 -*-
# @Author: Sagar Ghai and Nicole Mikolajczak
# @Date:   2016-05-01 16:29:19
# @Last Modified by:   Sagar Ghai
# @Last Modified time: 2016-05-01 16:31:42
# @Bugs: 1. the interface works statically for only the places we decided to demonstrate for.
# 		 2. The messages are sent to people in English and not Hindi.
# @How To Run: 1. Go to istp/landslides/ folder and run the file gui.py.
#			   2. python gui.py

from ttk import *
from Tkinter import *
import tkMessageBox as mbox
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import goslate

from twilio.rest import TwilioRestClient

from random import randint

entry1 = ""
variable1 = ""
variable2 = ""
variable3 = ""
variable4 = ""


class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()

    def alertSent(self):
        global entry1
        time = entry1.get()
        global variable1
        place = variable1.get()
        global variable2
        severity = variable2.get()

        message = "Landslide near " + place + " at " + time + ". " + severity
        # gs = goslate.Goslate()
        # hindi_message=gs.translate(message,'hi')
        ACCOUNT_SID = ""
        AUTH_TOKEN = ""

        client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

        scope = ['https://spreadsheets.google.com/feeds']

        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            'landslides-26a900b3717d.json', scope)

        gc = gspread.authorize(credentials)

        sh = gc.open_by_url(
            '')
        worksheet = sh.sheet1
        list_of_lists = worksheet.get_all_values()
        print list_of_lists
        flag = 1
        for i in list_of_lists:
            if flag == 1:
                flag = 0
                continue
            if place == i[2]:
                messaging = client.messages.create(
                    to="+91" + i[1],
                    from_="",
                    body=message
                )
        a_message = "Your alert was sent to people in region " + place
        mbox.showinfo("Alert Sent", a_message)

    def alertMessage(self):
        window = Toplevel(self.parent)
        window.title("Alert Message")

        window.columnconfigure(0, pad=5)
        window.columnconfigure(1, pad=5)
        window.columnconfigure(2, pad=5)
        window.columnconfigure(3, pad=5)

        window.rowconfigure(0, pad=5)
        window.rowconfigure(1, pad=5)
        window.rowconfigure(2, pad=5)
        window.rowconfigure(3, pad=5)
        window.rowconfigure(4, pad=5)
        window.rowconfigure(5, pad=5)

        OPTIONS1 = [

            "Dudar",
            "Katindhi",
            "Khaliar",
            "Nela",
            "Bhiuli"
        ]

        OPTIONS2 = [

            "People Injured",
            "Life Loss",
            "Property Loss",
            "Road Blocked"
        ]

        lab1 = Label(
            window, text="Please enter the severity, location, and time of landslide event. ", width=50)
        lab1.grid(row=0, column=0)

        # Severity row
        lab2 = Label(window, text="Severity:", width=15)
        lab2.grid(row=1, column=0)
        global variable2
        variable2 = StringVar(window)
        variable2.set(OPTIONS2[0])  # default value
        v = apply(OptionMenu, (window, variable2) + tuple(OPTIONS2))
        v.grid(row=1, column=3)

        # Location row
        lab3 = Label(window, text="Location:", width=15)
        lab3.grid(row=2, column=0)

        global variable1
        variable1 = StringVar(window)
        variable1.set(OPTIONS1[0])  # default value
        v1 = apply(OptionMenu, (window, variable1) + tuple(OPTIONS1))
        v1.grid(row=2, column=3)

        # Time row
        lab4 = Label(window, text="Time: (HH:MM)", width=25)
        lab4.grid(row=3, column=0)

        global entry1
        entry1 = Entry(window)  # enter time here (input box)
        entry1.grid(row=3, column=3)

        # #Sending message row
        # lab5 = Label(window, text="Message to be sent:", width=25)
        # lab5.grid(row=4,column=0)

        # entry2 = Entry(window)
        # entry2.grid(row=4, column=3) #should return message according to values (output box)
        # but should be editable and restricted to 160 char

        # Warning button
        w = Button(window, text="Send Alert", command=self.alertSent)
        w.grid(row=5, columnspan=3)

        window.geometry("750x250+400+100")

    def riskMessage(self):
        window2 = Toplevel(self.parent)
        window2.title("Check Risk")

        window2.columnconfigure(0, pad=5)
        window2.columnconfigure(1, pad=5)
        window2.columnconfigure(2, pad=5)
        window2.columnconfigure(3, pad=5)
        window2.columnconfigure(4, pad=5)
        window2.columnconfigure(5, pad=5)

        window2.rowconfigure(0, pad=5)
        window2.rowconfigure(1, pad=5)
        window2.rowconfigure(2, pad=5)
        window2.rowconfigure(3, pad=5)
        window2.rowconfigure(4, pad=5)
        window2.rowconfigure(5, pad=5)
        window2.rowconfigure(5, pad=5)
        window2.rowconfigure(6, pad=5)
        window2.rowconfigure(7, pad=5)

        lb1 = Label(
            window2, text="Check probabilty of landslide risk in local areas. Please send appropriate messages.", width=65)
        lb1.grid(row=0, column=0)

        # Risk Threshold

        lb2 = Label(window2, text="Place")
        lb2.grid(row=1, column=0)

        lb3 = Label(window2, text="Susceptibility")
        lb3.grid(row=1, column=1)

        lb4 = Label(window2, text="Probability of Landslide")
        lb4.grid(row=1, column=2)

        lb5 = Label(window2, text="Message type required")
        lb5.grid(row=1, column=3)

       # table
        places = ["Bhiuli", "Katindhi", "Dudar", "Nela", "Khaliar"]
        spatial_map = {'Kathindi': 0.4545, 'Dudar': 0.5909, 'Nela': 0.7272, 'Khaliar': 1}
        level = ["Low", "Low", "Moderate", "High", "Very High"]
        vals = [4.545, 4.545, 5.909, 7.272, 10]
        warning_type = ["Educational", "Educational", "Advisory", "Watch", "Warning"]

        os.system('scrapy crawl rainfall > oaut.txt')
        fp = open('oaut.txt')
        temporal = (float)(fp.readline(100))
        for i in range(5):
            vals[i] = temporal * vals[i]

        rows = []
        for i in range(5):
            cols = []
            for j in range(4):
                e = Entry(window2, relief=RIDGE)
                e.grid(row=i + 2, column=j, sticky=NSEW)
                if j == 0:
                    # insert the data for place/ hazard level/ risk/ warning type here
                    e.insert(END, places[i])
                elif j == 1:
                    e.insert(END, level[i])
                elif j == 2:
                    output = ((str)(vals[i]))[0:4] + " %"

                    e.insert(END, output)
                else:
                    e.insert(END, warning_type[i])
            cols.append(e)
        rows.append(cols)

        w2 = Button(window2, text='Send Advisory, Watch or Warning', command=self.onPress)
        w2.grid(row=7, column=0)

        w3 = Button(window2, text='Send Educational Message', command=self.eduMessage)
        w3.grid(row=7, column=1)

    def onPress(self):
        # gs = goslate.Goslate()
        advisory_message = "Your area lies in moderate risk zone. Please stay clear."
        watch_message = "There is a Landslide possibility in other areas of the District. Please watch out."
        warn_message = "There is a landslide predicted in your area. Please stay clear of any dangers!"
        ACCOUNT_SID = ""
        AUTH_TOKEN = ""

        client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

        scope = ['https://spreadsheets.google.com/feeds']

        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            'landslides-26a900b3717d.json', scope)

        gc = gspread.authorize(credentials)

        sh = gc.open_by_url(
            '')
        worksheet = sh.sheet1
        list_of_lists = worksheet.get_all_values()
        print list_of_lists
        flag = 1
        for i in list_of_lists:
            if flag == 1:
                flag = 0
                continue
            if i[2] == 'Dudar':
                messaging = client.messages.create(
                    to="+91" + i[1],
                    from_="",
                    body=advisory_message
                )
            elif i[2] == 'Nela':
                messaging = client.messages.create(
                    to="+91" + i[1],
                    from_="",
                    body=watch_message
                )
            elif i[2] == 'Khaliar':
                messaging = client.messages.create(
                    to="+91" + i[1],
                    from_="",
                    body=warn_message
                )
        mbox.showinfo("Advisory, Watch, and Warning",
                      "Your Advisory Message was sent to  people in Dudar region.\n Your Watch Message was sent to people in Nela region\n Your Warning Message was sent to people in Khaliar region")

    def eduMessage(self):
        window3 = Toplevel(self.parent)
        window3.title("Educational Message")

        window3.columnconfigure(0, pad=5)
        window3.columnconfigure(1, pad=5)
        window3.columnconfigure(2, pad=5)
        window3.columnconfigure(3, pad=5)

        window3.rowconfigure(0, pad=5)
        window3.rowconfigure(1, pad=5)
        window3.rowconfigure(2, pad=5)
        window3.rowconfigure(3, pad=5)
        window3.rowconfigure(4, pad=5)

        OPTIONS3 = [

            "Rainfall",
            "Consequences",
            "Causes"
        ]

        OPTIONS4 = [
            "Katindhi",
            "Dudar",
            "Nela",
            "Khaliar",
            "Bhiuli"
        ]

        lab1 = Label(
            window3, text="Please select which type of landslide information to send ", width=50)
        lab1.grid(row=0, column=0)

        # Type of Message row
        lab2 = Label(window3, text="Type of information:", width=15)
        lab2.grid(row=1, column=0)

        global variable3
        variable3 = StringVar(window3)
        variable3.set(OPTIONS3[0])  # default value
        v3 = apply(OptionMenu, (window3, variable3) + tuple(OPTIONS3))
        v3.grid(row=1, column=3)

        # Level of Hazard row
        lab3 = Label(window3, text="Place :", width=25)
        lab3.grid(row=2, column=0)

        global variable4
        variable4 = StringVar(window3)
        variable4.set(OPTIONS4[0])  # default value
        v4 = apply(OptionMenu, (window3, variable4) + tuple(OPTIONS4))
        v4.grid(row=2, column=3)

        w4 = Button(window3, text='Send Educational Message', command=self.eduSent)
        w4.grid(row=4, column=3)

    def eduSent(self):

        rainfall_messages = [
            "When rainfall is present, it is encouraged to stay away from the roads. ",
            "Heavy rainfall increases moisture in the soil,thereby loosening it, which will make the area more prone to landslides.",
            "The average annual rainfall in Mandi is 1380 milimeters which makes it more prone to landslides.",
            "The rainy season in India is from June until September, so there is a greater chance of landslides during these months.",
            "Rainfall is one of the major causes of Landslides"
        ]

        causes_messages = [
            "Heavy rainfall is the leading trigger of a landslide in this area.",
            "Cutting mountains to build roads makes the area more susceptible to landslides.",
            "Earthquakes are a leading cause of landslides in this area.",
            "Animal grazing loosens the soil, causing the area to be more prone to landslides.",
            "Landslides are natural events, but human activity can further cause them to occur."
        ]

        consequence_messages = [
            "Not evacuating your home during a landslide event can cause serious damage to your health.",
            "Sudden landslides along the road can cause serious car accidents.",
            "Deforestation is one of the leading human causes of landslides.",
            "If your house is damaged by a landslide, you can receive financial assistance from the government.",
            "If you experience a landslide, call #1077 to report it, or #108 for an ambulance."
        ]
        message = ""
        global variable3
        global variable4
        type_of_message = variable3.get()
        place = variable4.get()
        if type_of_message == 'Rainfall':
            point = (int)(randint(0, 4))
            message = rainfall_messages[point]
        elif type_of_message == 'Causes':
            point = (int)(randint(0, 4))
            message = causes_messages[point]
        else:
            point = (int)(randint(0, 4))
            message = consequence_messages[point]
        gs = goslate.Goslate()
        # message=gs.translate(message,'hi')
        ACCOUNT_SID = ""
        AUTH_TOKEN = ""
        client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
        scope = ['https://spreadsheets.google.com/feeds']

        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            'landslides-26a900b3717d.json', scope)

        gc = gspread.authorize(credentials)

        sh = gc.open_by_url(
            '')
        worksheet = sh.sheet1
        list_of_lists = worksheet.get_all_values()
        print list_of_lists
        flag = 1
        for i in list_of_lists:
            if flag == 1:
                flag = 0
                continue
            if place == i[2]:
                messaging = client.messages.create(
                    to="+91" + i[1],
                    from_="",
                    body=message
                )
        final_message = "Your educational message was sent to  people in " + place + " region."
        mbox.showinfo("Educational Sent", final_message)

    def initUI(self):

     # title parameters
        self.parent.title("Landslide Risk Communication SMS Program")
        self.pack(fill=BOTH, expand=1)

        self.columnconfigure(0, pad=5)
        self.columnconfigure(1, pad=5)
        self.columnconfigure(2, pad=5)
        self.columnconfigure(3, pad=5)
        self.columnconfigure(4, pad=5)
        self.columnconfigure(5, pad=5)

        self.rowconfigure(0, pad=5)
        self.rowconfigure(1, pad=5)
        self.rowconfigure(2, pad=5)
        self.rowconfigure(3, pad=5)
        self.rowconfigure(4, pad=5)
        self.rowconfigure(5, pad=5)
     # text parameters

        lbl1 = Label(
            self, text="Welcome to the Landslide Risk SMS Communication program.", width=50)
        lbl1.grid(row=0, column=3)

        lbl2 = Label(
            self, text="Please select 'Alert Message' if you wish to alert \n a specific area of a landslide event that has already occured.", width=50)
        lbl2.grid(row=5, column=3)

        lbl3 = Label(
            self, text="\n Select 'Check Daily Risk' to send messages to warn risky areas \n or to send informaitonal messages.", width=50)
        lbl3.grid(row=7, column=3)

      # title style parameters
        self.parent.title("Landslide Risk Communication SMS Program")
        self.style = Style()
        self.style.theme_use("default")

      # button parameters

        alertButton = Button(self, text="Alert Message", command=self.alertMessage)
        alertButton.grid(row=5, column=0)

        riskButton = Button(self, text="Check Daily Risk", command=self.riskMessage)
        riskButton.grid(row=7, column=0)

    def onSelect(self, val):

        sender = val.widget
        idx = sender.curselection()
        value = sender.get(idx)

        self.var.set(value)


def main():

    root = Tk()
    ex = Example(root)
    root.geometry("700x250+400+100")
    root.mainloop()


if __name__ == '__main__':
    main()
