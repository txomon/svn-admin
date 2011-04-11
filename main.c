#include <unistd.h>

extern char **environ;

int main()
{
	if(fork()==0)
		execl("main.py","main.py",NULL);
	else
		wait();
	return 0;
}
