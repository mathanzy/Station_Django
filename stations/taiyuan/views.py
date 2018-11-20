from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from taiyuan import models
import datetime
import time
import re


# Create your views here.
def queue_fresh(request):
    alarmdata_org = models.QueueInfo.objects.order_by('-alarm_time')[0].alarm_data
    alarmdata = list(map(int,alarmdata_org.split(',')))
    context = {'data': alarmdata}
    return JsonResponse(context)

def queue_length(request):
    return render(request, 'ticket_queue.html')

def hall_fresh(request):
    count1 = int(models.RegioncountInfo.objects.filter(camera_id='3').order_by('-alarm_time')[0].alarm_data)
    count2 = int(0)
    count3 = int(0)
    count4 = int(0)
    context = {'hct1':count1,
               'hct2':count2,
               'hct3':count3,
               'hct4':count4,}
    return JsonResponse(context)

def stationhall_count(request):
    return render(request, 'stationhall_count.html')

def flow_yesterday(request):
    yesterday_data_fake = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 75.6, 82.2, 48.7, 18.8, 6.0, 2.3,
                 5.5, 3.4, 15.3, 17.2, 23.4, 36.8, 54.2, 37.6, 18.2, 10.3, 8.9, 1.2]
    context_fake = {'yesterday':yesterday_data_fake}
    date_yesterday = (datetime.datetime.now()-datetime.timedelta(days=1)).strftime("%Y-%m-%d ")
    yesterday_data = []
    for i in range(24):
        start_data = 0
        end_data = 0
        if i < 10:
            hour_yesterday_start = date_yesterday + "0%d:00" % (i)
            hour_yesterday_end = date_yesterday + "0%d:59"%(i)
        else:
            hour_yesterday_start = date_yesterday + "%d:00" % (i)
            hour_yesterday_end = date_yesterday + "%d:59"%(i)
        start_data_list = models.FlowcountInfo.objects.filter(camera_id='9', alarm_time__contains=hour_yesterday_start)
        end_data_list = models.FlowcountInfo.objects.filter(camera_id='9', alarm_time__contains=hour_yesterday_end)
        if len(start_data_list) == 0:
            hour_yesterday_plus1 = re.sub(":00",":01",hour_yesterday_start)
            start_data_list = models.FlowcountInfo.objects.filter(camera_id='9',
                                                                    alarm_time__contains=hour_yesterday_plus1)
            if len(start_data_list) == 0:
                hour_yesterday_plus2 = re.sub(":00", ":02", hour_yesterday_start)
                start_data_list = models.FlowcountInfo.objects.filter(camera_id='9',
                                                                        alarm_time__contains=hour_yesterday_plus2)
                if len(start_data_list) == 0:
                    start_data = 0
                else:
                    start_data = my_mean(start_data_list)
            else:
                start_data = my_mean(start_data_list)
        else:
            start_data = my_mean(start_data_list)
        if len(end_data_list) == 0:
            hour_yesterday_minus1 = re.sub(":59",":58",hour_yesterday_end)
            end_data_list = models.FlowcountInfo.objects.filter(camera_id='9',
                                                                  alarm_time__contains=hour_yesterday_minus1)
            if len(end_data_list) == 0:
                end_yesterday_minus2 = re.sub(":59", ":57", hour_yesterday_end)
                end_data_list = models.FlowcountInfo.objects.filter(camera_id='9',
                                                                      alarm_time__contains=end_yesterday_minus2)
                if len(end_data_list) == 0:
                    end_data = 0
                else:
                    end_data = my_mean(end_data_list)
            else:
                end_data = my_mean(end_data_list)
        else:
            end_data = my_mean(end_data_list)
        # temp_data = end_data - start_data
        # if temp_data < 0:
        #     temp_data = end_data
        hour_max_data = models.FlowcountInfo.objects.max_count(hour_yesterday_start, hour_yesterday_end)
        if hour_max_data == end_data:
            temp_data = end_data - start_data
        else:
            temp_data = hour_max_data - start_data + end_data
        yesterday_data.append(temp_data)
    context = {'yesterday':yesterday_data}
    return JsonResponse(context_fake)

def my_mean(list):
    sum = 0
    for i in list:
        sum += int(i.flowcount)
    mean_value = sum // len(list)
    return mean_value

def flow_today(request):
    today_data_fake = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 35.6, 62.2, 32.6, 20.0, 6.4, 3.3, 9.9,10]
    context_fake = {'today':today_data_fake}
    date_today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    hour_ = time.localtime().tm_hour
    minute_ = time.localtime().tm_min
    today_data =  []
    for i in range(hour_):
        if i < 10:
            hour_today_start = date_today[:-5] + "0%d:00" % (i)
            hour_today_end = date_today[:-5] + "0%d:59" % (i)
        else:
            hour_today_start = date_today[:-5] + "%d:00" % (i)
            hour_today_end = date_today[:-5] + "%d:59" % (i)
        start_data_list = models.FlowcountInfo.objects.filter(camera_id='9',
                                                                alarm_time__contains=hour_today_start)
        end_data_list = models.FlowcountInfo.objects.filter(camera_id='9',
                                                              alarm_time__contains=hour_today_end)
        if len(start_data_list) == 0:
            hour_today_plus1 = re.sub(":00", ":01", hour_today_start)
            start_data_list = models.FlowcountInfo.objects.filter(camera_id='9',
                                                                    alarm_time__contains=hour_today_plus1)
            if len(start_data_list) == 0:
                hour_today_plus2 = re.sub(":00", ":02", hour_today_start)
                start_data_list = models.FlowcountInfo.objects.filter(camera_id='9',
                                                                        alarm_time__contains=hour_today_plus2)
                if len(start_data_list) == 0:
                    start_data = 0
                else:
                    start_data = my_mean(start_data_list)
            else:
                start_data = my_mean(start_data_list)
        else:
            start_data = my_mean(start_data_list)
        if len(end_data_list) == 0:
            hour_today_minus1 = re.sub(":59", ":58", hour_today_end)
            end_data_list = models.FlowcountInfo.objects.filter(camera_id='9',
                                                                  alarm_time__contains=hour_today_minus1)
            if len(end_data_list) == 0:
                end_today_minus2 = re.sub(":59", ":57", hour_today_end)
                end_data_list = models.FlowcountInfo.objects.filter(camera_id='9',
                                                                      alarm_time__contains=end_today_minus2)
                if len(end_data_list) == 0:
                    end_data = 0
                else:
                    end_data = my_mean(end_data_list)
            else:
                end_data = my_mean(end_data_list)
        else:
            end_data = my_mean(end_data_list)
        hour_max_data = models.FlowcountInfo.objects.max_count(hour_today_start, hour_today_end)
        if hour_max_data == end_data:
            temp_data = end_data - start_data
        else:
            temp_data = hour_max_data - start_data + end_data
        # temp_data = end_data - start_data
        # if temp_data < 0:
        #     temp_data = end_data
        # if start_data==0 and end_data==0:
        #     hour_max_data = models.FlowcountInfo.objects.max_count(hour_today_start,hour_today_end)
        #     temp_data = hour_max_data
        today_data.append(temp_data)
    today_data.append(0)
    if minute_ < 5:
        latest_data = 0
        today_data[-1] = latest_data
    else:
        latest_start_data = 0
        latest_end_data = 0
        hour_latest_start = date_today[:-2]+"00"
        start_data_list = models.FlowcountInfo.objects.filter(camera_id='9',
                                                                alarm_time__contains=hour_latest_start)
        if len(start_data_list) == 0:
            hour_latest_plus1 = re.sub(":00", ":01", hour_latest_start)
            start_data_list = models.FlowcountInfo.objects.filter(camera_id='9',
                                                                    alarm_time__contains=hour_latest_plus1)
            if len(start_data_list) == 0:
                hour_latest_plus2 = re.sub(":00", ":02", hour_latest_start)
                start_data_list = models.FlowcountInfo.objects.filter(camera_id='9',
                                                                        alarm_time__contains=hour_latest_plus2)
                if len(start_data_list) == 0:
                    latest_start_data = 0
                else:
                    latest_start_data = my_mean(start_data_list)
            else:
                latest_start_data = my_mean(start_data_list)
        else:
            latest_start_data = my_mean(start_data_list)

        try:
            latest_end_data = models.FlowcountInfo.objects.filter(camera_id='9',
                                                                    alarm_time__contains=date_today[:-2]).order_by("-alarm_time")[0].flowcount
        except Exception as e:
            latest_end_data = 0
        if latest_end_data == 0:
            latest_data = 0
        else:
            latest_data = latest_end_data - latest_start_data
            if latest_data < 0:
                latest_data = latest_end_data

        today_data[-1] = latest_data
    context = {'today': today_data}
    return JsonResponse(context_fake)

def flow_count(request):
    return render(request, 'flow_count.html')

def buffer_before(request):
    sum = 0
    data_before = []
    date_before = []
    for i in range(60):
        sum = 0
        time_str = (datetime.datetime.now()-datetime.timedelta(minutes=i)).strftime("%Y-%m-%d %H:%M")
        date_before.append(time_str+":00")
        temp_data_list = models.RegioncountInfo.objects.filter(camera_id='1',alarm_time__contains=time_str)
        if len(temp_data_list) == 0:
            temp_data = 0
            data_before.append(temp_data)
        else:
            for i in temp_data_list:
                sum += int(i.alarm_data)
            temp_data = sum // len(temp_data_list)
            data_before.append(temp_data)
    data_before.reverse()
    date_before.reverse()
    date = date_before
    data = data_before
    context = {'date':date,'data':data}
    return JsonResponse(context)

def buffer_fresh(request):
    sum = 0
    time_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    data_list = models.RegioncountInfo.objects.filter(camera_id='1', alarm_time__contains=time_str)
    if len(data_list) == 0:
        data = 0
    else:
        for i in data_list:
            sum += int(i.alarm_data)
        data = sum // len(data_list)
    date_new = time_str+":00"
    data_new = data
    context = {'date_new':date_new,'data_new':data_new}
    return JsonResponse(context)

def bufferroom_count(request):
    return render(request,'buffer_test.html')


