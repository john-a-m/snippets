class APIThread(threading.Thread):

    def __init__(self, endpoint, auth_params):
        super(APIThread, self).__init__()
        self.endpoint = endpoint
        self.auth_params = auth_params
        self.is_running = threading.Event()
        self.is_running.set()


class HeartbeatThread(APIThread):
    """An asynchronous thread that keeps the user logged in."""

    def run(self):
        """
            Posts to heartbeat endpoint every 25 seconds.
            We pause 1 second at a time so we don't have to wait all 25 seconds
            for Thread.join to execute.
        """
        seconds = 0
        while self.is_running.is_set():
            #according to the API a heartbeat should happen every 30 seconds,
            #we'll do it every 25, giving us 5 seconds to account for
            #program/network overhead
            if seconds == 25:
                response = requests.post(
                    self.endpoint + "/heartbeats/", 
                    json=self.auth_params
                )
                seconds = 0
            time.sleep(1)
            seconds += 1

    def join(self, timeout=None):
        """
            Sends a delete to the heartbeat endpoint, which "logs" the user out
            and stops the loop in the run method
        """
        response = requests.delete(
            self.endpoint + "/sessions/", 
            json=self.auth_params
        )
        self.is_running.clear()
        super(HeartbeatThread, self).join(timeout)
