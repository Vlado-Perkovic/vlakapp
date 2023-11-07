#!/usr/bin/python3
import datetime
import requests
import re


def run(direction):
    if (direction == "doma"):
        destID = 72401
        startID = 72480
    elif (direction == "faks"):
        startID = 72401
        destID = 72480
    else:
        print("Wrong direction. Exiting...")
        exit(1)
    today = datetime.date.today()
    link = f'https://prodaja.hzpp.hr/hr/Ticket/Journey?StartId={startID}&DestId={destID}&ReturnTrip=false&DepartureDate={today}&ReturnDepartureDate={today}'
    page = requests.get(link)
    if (page.status_code != 200):
        print("FAILED! Exiting...")
        exit(1)
    # print(page.text)
    startTime = re.findall("col-1-7 cell\">[0-9]{2}:[0-9]{2}", page.text)
    trainID = re.findall("detailsid=\"[0-9]{4}\"", page.text)
    startTime1 = [t[14:] for t in startTime]
    trainID1 = [t.strip('detailsid=') for t in trainID]
    # datetime object containing current date and time
    now = datetime.datetime.now()
    dt_string = now.strftime("%H:%M")
    res = ''
    for i, time in enumerate(startTime1):
        if time > dt_string:
            res += f"Iduci vlak ti je u {time} i to {trainID1[i]}\n"
            if i != len(startTime1)-1:
                res += f"Onaj iza njega je u {startTime1[i+1]} i to {trainID1[i+1]}"
            break
    return res


if __name__ == "__main__":
    run("doma")
