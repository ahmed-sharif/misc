#include <unistd.h>

#include <stdio.h>

int main()
{
  if(fork()>0)
  {
    abort();
    printf("Parent\n");
    wait(0);
  }
  else
  {
    printf("Child\n");
    if(execv("/bin/ls", "ls", "-l", "/etc/passwd", NULL) < 0)
    {
      printf("failed\n");
    }
  }
  return 0;
}
