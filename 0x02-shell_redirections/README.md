# 0x02. Shell, I/O Redirections and filters

Shell, I/O Redirection

    What do the commands head, tail, find, wc, sort, uniq, grep, tr do
    How to redirect standard output to a file
    How to get standard input from a file instead of the keyboard
    How to send the output from one program to the input of another program
    How to combine commands and filters with redirections

General

    Allowed editors: vi, vim, emacs
    All your scripts will be tested on Ubuntu 20.04 LTS
    All your scripts should be exactly two lines long ($ wc -l file should print 2)
    All your files should end with a new line (why?)
    The first line of all your files should be exactly #!/bin/bash
    A README.md file, at the root of the folder of the project, describing what each script is doing
    You are not allowed to use backticks, &&, || or ;
    All your files must be executable
    You are not allowed to use sed or awk


# Task 1
Hello World
mandatory

Write a script that prints “Hello, World”, followed by a new line to the standard output.

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x02-shell_redirections
    File: 0-hello_world



# Task 2
Write a script that displays a confused smiley "(Ôo)'.

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x02-shell_redirections
    File: 1-confused_smiley



# Task 3
Display the content of the /etc/passwd file.

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x02-shell_redirections
    File: 2-hellofile



# Task 4
Display the content of /etc/passwd and /etc/hosts

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x02-shell_redirections
    File: 3-twofiles



# Tasks 5
Display the last 10 lines of /etc/passwd

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x02-shell_redirections
    File: 4-lastlines



# Task 6
Display the first 10 lines of /etc/passwd

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x02-shell_redirections
    File: 5-firstlines


# Task 7
Write a script that displays the third line of the file iacta.

The file iacta will be in the working directory

    You’re not allowed to use sed

Note: The output will differ, depending on the content of the file iacta.

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x02-shell_redirections
    File: 6-third_line


# Task 8
Write a shell script that creates a file named exactly \*\\'"Best School"\'\\*$\?\*\*\*\*\*:) containing the text Best School ending by a new line.

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x02-shell_redirections
    File: 7-file


# Task 9
Write a script that writes into the file ls_cwd_content the result of the command ls -la. If the file ls_cwd_content already exists, it should be overwritten. If the file ls_cwd_content does not exist, create it.

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x02-shell_redirections
    File: 8-cwd_state


# Task 10
Write a script that duplicates the last line of the file iacta

    The file iacta will be in the working directory

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x02-shell_redirections
    File: 9-duplicate_last_line


# Task 11
Write a script that deletes all the regular files (not the directories) with a .js extension that are present in the current directory and all its subfolders.

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x02-shell_redirections
    File: 10-no_more_js


# Task 12
Write a script that counts the number of directories and sub-directories in the current directory.

    The current and parent directories should not be taken into account
    Hidden directories should be counted

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x02-shell_redirections
    File: 11-directories


# Task 13
Create a script that displays the 10 newest files in the current directory.

Requirements:

    One file per line
    Sorted from the newest to the oldest

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x02-shell_redirections
    File: 12-newest_files


# Task 14
Create a script that takes a list of words as input and prints only words that appear exactly once.

    Input format: One line, one word
    Output format: One line, one word
    Words should be sorted

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x02-shell_redirections
    File: 13-unique


# Task 15
Display lines containing the pattern “root” from the file /etc/passwd

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x02-shell_redirections
    File: 14-findthatword


# Task 16
Display the number of lines that contain the pattern “bin” in the file /etc/passwd

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x02-shell_redirections
    File: 15-countthatword


# Task 17
Display lines containing the pattern “root” and 3 lines after them in the file /etc/passwd

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x02-shell_redirections
    File: 16-whatsnext


# Task 18
Display all the lines in the file /etc/passwd that do not contain the pattern “bin”

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x02-shell_redirections
    File: 17-hidethisword


# Task 19
Display all lines of the file /etc/ssh/sshd_config starting with a letter

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x02-shell_redirections
    File: 18-letteronly


# Task 20
Replace all characters A and c from input to Z and e respectively


Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x02-shell_redirections
    File: 19-AZ


# Task 21
Create a script that removes all letters c and C from input

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x02-shell_redirections
    File: 20-hiago


# Task 22
Write a script that reverse its input

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x02-shell_redirections
    File: 21-reverse


# Task 23
Write a script that displays all users and their home directories, sorted by users.

    Based on the the /etc/passwd file

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x02-shell_redirections
    File: 22-users_and_homes


# Task 24
Write a command that finds all empty files and directories in the current directory and all sub-directories.

    Only the names of the files and directories should be displayed (not the entire path)
    Hidden files should be listed
    One file name per line
    The listing should end with a new line
    You are not allowed to use basename, grep, egrep, fgrep or rgrep

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x02-shell_redirections
    File: 100-empty_casks


# Task 25
Write a script that lists all the files with a .gif extension in the current directory and all its sub-directories.

    Hidden files should be listed
    Only regular files (not directories) should be listed
    The names of the files should be displayed without their extensions
    The files should be sorted by byte values, but case-insensitive (file aaa should be listed before file bbb, file .b should be listed before file a, and file Rona should be listed after file jay)
    One file name per line
    The listing should end with a new line
    You are not allowed to use basename, grep, egrep, fgrep or rgrep


Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x02-shell_redirections
    File: 101-gifs


# Task 26
An acrostic is a poem (or other form of writing) in which the first letter (or syllable, or word) of each line (or paragraph, or other recurring feature in the text) spells out a word, message or the alphabet. The word comes from the French acrostiche from post-classical Latin acrostichis). As a form of constrained writing, an acrostic can be used as a mnemonic device to aid memory retrieval. Read more.

Create a script that decodes acrostics that use the first letter of each line.

    The ‘decoded’ message has to end with a new line
    You are not allowed to use grep, egrep, fgrep or rgrep

Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x02-shell_redirections
    File: 102-acrostic


# Task 27
Write a script that parses web servers logs in TSV format as input and displays the 11 hosts or IP addresses which did the most requests.

    Order by number of requests, most active host or IP at the top
    You are not allowed to use grep, egrep, fgrep or rgrep


Repo:

    GitHub repository: alx-system_engineering-devops
    Directory: 0x02-shell_redirections
    File: 103-the_biggest_fan

