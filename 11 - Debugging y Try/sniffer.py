import argparse
import socket # for connecting
from threading import Thread, Lock
from queue import Queue

# number of threads, feel free to tune this parameter as you wish
N_THREADS = 200
# thread queue
q = Queue()
print_lock = Lock()

def port_scan(port):
    """
    Scan a port on the global variable `host`
    """
    try:
        s = socket.socket()
        s.connect((host, port))
    except:
        with print_lock:
            print(f"{host:15}:{port:5} is closed", end='\r')
    else:
        with print_lock:
            print(f"{host:15}:{port:5} is open")
    finally:
        s.close()

def scan_thread():
    global q
    while True:
        # get the port number from the queue
        worker = q.get()
        # scan that port number
        port_scan(worker)
        # tells the queue that the scanning for that port 
        # is done
        q.task_done()


def main(host, ports):
    global q
    for t in range(N_THREADS):
        # for each thread, start it
        t = Thread(target=scan_thread)
        # when we set daemon to true, that thread will end when the main thread ends
        t.daemon = True
        # start the daemon thread
        t.start()
    for worker in ports:
        # for each port, put that port into the queue
        # to start scanning
        q.put(worker)
    # wait the threads ( port scanners ) to finish
    q.join()

if __name__ == "__main__":
    # parse some parameters passed
    parser = argparse.ArgumentParser(description="Simple port scanner")
    parser.add_argument("host", help="Host to scan.")
    parser.add_argument("--ports", "-p", dest="port_range", default="1-65535", help="Port range to scan, default is 1-65535 (all ports)")
    args = parser.parse_args()
    host, port_range = args.host, args.port_range

    start_port, end_port = port_range.split("-")
    start_port, end_port = int(start_port), int(end_port)

    ports = [ p for p in range(start_port, end_port)]

    main(host, ports)

'''
try:
    s.connect((ip, port))
except:
    print("Could not connect.")
else:
    print("Sending evil buffer...")
    s.send(bytes(buffer + "\r\n", "latin-1"))
    print("Done!")
finally:
    s.close()
'''