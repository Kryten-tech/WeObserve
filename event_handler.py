import watchdog.events, watchdog.observers, os.path, time, socket, datetime

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)


# Handles Events:
class Events(watchdog.events.PatternMatchingEventHandler): 

    fucky_endings = {"swp","swx", "swpx"}

    def __init__(self):

        # Search for a specific file extension (in this case it searches for all)
        watchdog.events.PatternMatchingEventHandler.__init__(self, patterns=['*'], 
                                                             ignore_directories=True, case_sensitive=False)

        # File creation event:
    def on_created(self, event):
        if event.src_path[-3:] in self.fucky_endings:
            return
        c_notification = "Received modification event - % s - % s - % s" % (event.src_path, time.ctime(os.path.getctime(event.src_path)), IPAddr)
        #print(c_notification) # Prints immediately
        print(c_notification, file=open("output.txt", "a")) # Prints into specified txt file
        
        # File modification event:
    def on_modified(self, event):
        if event.src_path[-3:] in self.fucky_endings:
            return 
        m_notification = "Received modification event - % s - % s - % s" % (event.src_path, time.ctime(os.path.getmtime(event.src_path)), IPAddr)
        #print(m_notification) 
        print(m_notification, file=open("output.txt", "a"))

        # File deletion event:
    def on_deleted(self, event):
        if event.src_path[-3:] in self.fucky_endings:
            return
        d_notification = "File/Directory was deleted - % s - % s - % s" % (event.src_path, datetime.datetime.now(), IPAddr)
        #print(d_notification)
        print(d_notification, file=open("output.txt", "a"))

if __name__ == "__main__":
    src_path = "test_directory" # /path/to/directory
    event_handler = Events()
    observer = watchdog.observers.Observer()
    observer.schedule(event_handler, path=src_path, recursive=True)
    observer.start()   
    try:
        while True: 
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop() 
    observer.join()
