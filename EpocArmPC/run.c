#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <unistd.h>

int main()
{
   char wrkpth[2048];
   char full_wrk[2048];
   getcwd(wrkpth, sizeof(wrkpth));
   sprintf(full_wrk,"%s/main.sh",wrkpth);
   setuid( 0 );
   system(full_wrk);
   return 0;
}
