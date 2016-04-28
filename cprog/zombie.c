#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
int main ()
{
  pid_t child_pid;
  /* Create a child process. */
  child_pid = fork ();
  if (child_pid > 0) {
    /* This is the parent process. Sleep for a minute. */
    printf("parent before sleeping\n");
    sleep (60);
    printf("parent after sleeping\n");
    /* wait(0); */
  }
  else 
  {
    /* This is the child process. Exit immediately. */
    printf("child before sleeping\n");
    sleep (10);
    printf("child after sleeping\n");
    exit (0);
  }
  return 0;
}
