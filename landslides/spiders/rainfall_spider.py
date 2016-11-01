# -*- coding: utf-8 -*-
# @Author: sagar
# @Date:   2016-04-21 23:55:55
# @Last Modified by:   Sagar Ghai
# @Last Modified time: 2016-05-01 00:27:16
import scrapy
import datetime
import math

day=(int)(datetime.date.today().day)
month=(int)(datetime.date.today().month)
yr=(int)(datetime.date.today().year)
month_name=(str)(datetime.datetime.now().strftime("%B").lower())

class RainfallSpider(scrapy.Spider):
    global day
    global month
    global yr
    global month_name
    name = "rainfall"
    allowed_domains = ["accuweather.com"]
    url="http://www.accuweather.com/en/in/tehri/201478/"+month_name+"-weather/188527?monyr="+(str)(month)+"/1/"+(str)(yr)+"&view=table"
    start_urls = []
    start_urls.append(url)

    def parse(self, response):
    	path='//*[@id="panel-main"]/div[2]/div/div/table/tbody/tr['+(str)(day)+']/td[3]/text()'
        value_rainfall = response.xpath(path).extract()
        rainfall=(float)(value_rainfall[0].encode('utf-8')[0])
        fp=open('/Users/sagar/Desktop/istp/landslides/landslides/spiders/rainfall1.txt')
        data=[]
        for f in fp:
            data.append((float)(f))
        year_days=[0,31,59,90,120,151,181,212,243,273,304,334]
        day_number=year_days[month-1]+day
        # print day_number
        day_3_cum=0
        day_30_cum=0
        for i in range(day_number-3, day_number):
            day_3_cum+=data[i]
        for i in range(day_number-33,day_number-3):
                day_30_cum+=data[i]
        z_score=3.817-(0.077*rainfall)-(0.058*day_3_cum)-(0.009*day_30_cum)
        # print z_score
        probability=1/(1+math.exp(z_score))
        print probability
