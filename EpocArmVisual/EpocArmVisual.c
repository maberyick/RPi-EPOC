#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

int main()
{
   setuid( 0 );
   system("/home/maberyick/Dropbox/Self-Research_EEG/EpocArmVisual/main.sh");
   return 0;
}
