#Import relevant modules
import psutil
import time

def get_interface_bytes(interface):
    #retive  network I/O counters for all interfaces
    counters = psutil.net_io_counters(pernic=True)

    #check if the speciefied interface exists in counters
    if interface in counters:
        #return the number of bytes sent and received on the interface
        return counters[interface].bytes_sent, counters[interface].bytes_recv
    else:
        #Raise an exception if the interface is not found
        raise ValueError(f" Interface '{interface}' not found.")
    

def monitor_bandwidth(interface, interval=1):
    try:
        while True:
            #get the initial number of bytes sent and received
            sent_start, recv_start = get_interface_bytes(interface)

            #wait for the specified interval 
            time.sleep(interval)

            #get the final number of bytes sent and received
            sent_end, recv_end = get_interface_bytes(interface)

            #Calculate the upload and download speed 
            sent_speed = (sent_end -sent_start) / interval
            recv_speed = (recv_end - recv_start) / interval

            #Print the results
            print(f"Interface: {interface}")
            print(f"Upload Speed: {sent_speed} bytes/sec")
            print(f"Download Speed: {recv_speed} bytes/sec")
            
    except KeyboardInterrupt:
        #handle keyboard interrupt to stop monitoring 
        print("Monitoring stopped. ")

monitor_bandwidth("eth0") #Specified interface is eth0 and can be replaced with the name of your netword
