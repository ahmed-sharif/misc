from daemonize import daemonize
import time
import sys
    def mod_5_watcher():
        i = 10
        while True:
            time.time(5)
            i += 1
            i %= 10

if __name__ == '__main__':
    daemonize(stdout='/tmp/stdout.log', stderr='/tmp/stderr.log')
    mod_5_watcher()
