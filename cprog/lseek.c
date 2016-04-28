#include <sys/stat.h>
#include <fcntl.h>
#include <ctype.h>

int
main(int argc, char *argv[])
{
    size_t len;
    off_t offset=5000;
    int fd, ap, j;
    char *buf;
    ssize_t numRead, numWritten;


    fd = open("hole", O_RDWR); 

    lseek(fd, offset, SEEK_END);

    write(fd, "hello\0", 5);

    close(fd);

}

