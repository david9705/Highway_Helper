import time, DAN, requests, random

ServerURL = 'http://140.113.199.188:9999' #with no secure connection
Reg_addr = '0516215_weather_out' #if None, Reg_addr = MAC address

# DAN.profile['dm_name'] = 'Dummy_Device'
# DAN.profile['df_list'] = ['Dummy_Sensor', 'Dummy_Control']
DAN.profile['dm_name'] = '0516215_Weather_out'
DAN.profile['df_list'] = ['0516215_Temperature_out', '0516215_Humidity_out']
DAN.profile['d_name'] = None # None for autoNaming
DAN.device_registration_with_retry(ServerURL, Reg_addr)

# DAN.deregister()
# exit()

while True:
    try:
    #Pull data from a device feature called "Dummy_Control"
        value1 = DAN.pull('0516215_Temperature_out')
        if value1 != None:
            print (value1[0])
        value2 = DAN.pull('0516215_Humidity_out')
        if value2 != None:
            print (value2[0])


    except Exception as e:
        print(e)
        if str(e).find('mac_addr not found:') != -1:
            print('Reg_addr is not found. Try to re-register...')
            DAN.device_registration_with_retry(ServerURL, Reg_addr)
        else:
            print('Connection failed due to unknow reasons.')
            time.sleep(1)    

    time.sleep(5)

