#include <sys/stat.h>
#include <fcntl.h>
#include <ctype.h>
#include <signal.h>
#include <string.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int
main(int argc, char *argv[])
{
    size_t len;
    off_t offset=500;
    int fd, ap, j;
    char *buf;
    ssize_t numRead, numWritten;
    int i;
    int ssd;

    fd = open("p", O_RDWR|O_APPEND); 
    

    lseek(fd, 0, SEEK_SET);
    write(fd, "hello\0", 5);
    
    sleep(30);
    close(fd);

}

