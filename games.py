o
    P�.c$   �                   @   s6  d dl Z d dlZd dlZdd� Zed� e �d� e�d� ed� ed� ed	� e�d
� ed� e�d� ed� e�d� d dlZd dlZd dl Z dd� Zdd� Ze�  ed� ed� ed� ed� ed� ed� ed� ed� ed� ed� ed� ed� e�d� e	d�Z
e
d kr�ed!� e�d� e �d"� dS e
d#kr�ed$� e �d%� ed� ed&� ed	� e�d� ed'� ed	� e�d� e�  dS e
d(k�red$� e �d)� ed*� ed+� ed	� e�d� ed,� ed	� e�d� e�  dS e
d-k�r7ed$� e �d.� ed*� ed/� ed	� e�d� ed0� ed	� e�d� e�  dS e
d1k�rfed$� e �d2� ed*� ed3� ed	� e�d� ed4� e e�d� e�  dS e
d5k�r�ed$� e �d6� ed*� ed7� ed	� e�d� ed8� ed	� e�d� e�  dS e
d9k�r�ed$� e �d:� ed*� ed;� ed	� e�d� ed<� ed	� e�d� e�  dS e
d=k�r�ed$� e �d>� ed*� ed?� ed	� e�d� ed@� ed	� e�d� e�  dS e
dAk�r*ed$� e �dB� ed*� edC� ed	� e�d� edD� ed	� e�d� e�  dS e
dEk�r�ed$� e �dF� ed*� edG� ed	� edH� ed	� edI� e�dJ� edK� e�dJ� edL� e�dJ� edM� e�dJ� edN� e�dJ� edO� e�dJ� edP� e�dJ� edQ� e�d� ed	� edR� ed	� e�d� e�  dS e
dSk�r�e �d� edT� e �dU� ed	� edV� e�d� edW� e�d� edX� e�d
� edY� e�d� edZ� e�d� ed[� e�d
� ed\� e�d� ed]� e�d� ed^� e�d
� ed_� e�d� ed`� e�d� eda� e�d
� edb� e�d� edc� e�d� edd� e�d
� edb� e�d� ede� e�d� edf� e�d
� edg� e�d
� edh� e�d
� edi� e�d
� edj� e�d� edk� e�d� edl� e�d
� edm� e�d� edn� e�d� edo� e�d
� edp� e�d� edq� e�d� dS e
drk�reds� e�dt� e �du� e �dv� e �dw� e �dx� e �d� ed� e�  edy� e�d� e �d"� dS e
dzk�red{� e�d� e�  dS dS )|�    Nc                 C   �2   | d D ]}t j�|� t j��  t�d� qd S )N�
g���Q��?��sys�stdout�write�flush�time�sleep��z�e� r   �/sdcard/OK/games.py�psb   �
   
�r   �[92m�clearg�������?zy _____         _      _   _             _     
|_   _|____  _(_) ___| \ / 
                                              z0[3;90m  		      Security Is An Illusion [0;92mr   �333333�?z
[!] Loading...z
[!] Please Wait.....�   c                 C   r   )Nr   g�~j�t�h?r   r   r   r   r   �logopsb   r   r   c                   C   sN   t �d� td� td� td� t�d� t td� td� t�d� d S )	Nr   r   z� _____ ____                           
|_   _/ ___| __ _ _ __ ___   ___  ___ 
  | || |  _ / _` | '_ ` _ \ / _ \/ __|
  | || |_| | (_| | | | | | |  __/\__ \ 
  |_| \____|\__,_|_| |_| |_|\___||___/
                                      z'[3;90m			A Product Of WHOAMI-XD[0;92m�      �?a�  [34m
|****************************************************| 
|[3m Author   : WHOAMI-XD-KING                               [0;34m|
|[3m Tool     : Termux Games                            [0;34m|
|[3m Version  : 1.0                                     [0;34m|
|[3m Link     : https://www.github.com/WHOAMI-XD-KING/	     [0;34m|
|[3m Coded By : WHOAMI-XD        		     	     [0;34m|
|[3m Note     : Add Termux Extra Keys Before Playing    [0;34m|
******************************************************z[3;92mr   )�os�system�printr   r	   r
   r   r   r   r   �logo%   s   

r   z[01] Install PacMan Game.z[02] Install Tetris Game.z[03] Install Moon-Buggy Game.z[04] Install nInvaders Game.z[05] Install Snake Game.z[06] Install Greed Game.z[07] Install Nethack Game.z[08] Install Sudoku Game.z [09] Install All Games Together.z[10] Details About The Games.z[11] Add Extra Termux Keys.z[12] Exit Program.gffffff�?z

[*] Enter Your Choice:> � z&[31m
[*] Please Select an Option.....zpython Termux-games.py�1z[*] Please Wait Some Time....z+pkg install pacman4console > /dev/null 2>&1z%
[*] PacMan Installed Successfully...z;[*] To Play The Game, Type pacman in the Terminal...[0;37m�2z#pkg install bastet > /dev/null 2>&1z[92m
z$[*] Tetris Installed Successfully...z;[*] To Play The Game, Type bastet in the Terminal...[0;37m�3z'pkg install moon-buggy > /dev/null 2>&1z([*] Moon-Buggy Installed Successfully...z?[*] To Play The Game, Type moon-buggy in the Terminal...[0;37m�4z&pkg install ninvaders > /dev/null 2>&1z'[*] nInvaders Installed Successfully...z>[*] To Play The Game, Type ninvaders in the Terminal...[0;37m�5z#pkg install nsnake > /dev/null 2>&1z([*] Snake Game Installed Successfully...z;[*] To Play The Game, Type nsnake in the Terminal...[0;37m�6z"pkg install greed > /dev/null 2>&1z#[*] Greed Installed Successfully...z:[*] To Play The Game, Type greed in the Terminal...[0;37m�7z$pkg install nethack > /dev/null 2>&1z%[*] Nethack Installed Successfully...z<[*] To Play The Game, Type nethack in the Terminal...[0;37m�8zJpkg install nudoku > /dev/null 2>&1 && apt install nudoku > /dev/null 2>&1z$[*] Sudoku Installed Successfully...z;[*] To Play The Game, Type nudoku in the Terminal...[0;37m�9z�pkg install pacman4console bastet moon-buggy ninvaders nsnake greed nudoku > /dev/null 2>&1 && apt install nudoku > /dev/null 2>&1z$All Games Installed Successfully....zFor playing The Games....z[*] Type pacman to play PacMang�������?z[*] Type bastet to play Tetrisz&[*] Type moon-buggy to play Moon-Buggyz$[*] Type ninvaders to play nInvadersz"[*] Type nsnake to play Snake Gamez[*] Type greed to play Greedz [*] Type nethack to play Nethackz[*] Type nudoku to play Sudokuz[!] Enjoy.....[0;37mZ10z[0;92mzfiglet Detailsz1
[3;92m[#] Details About The Games are Below...
z
[01] PacMan Details:
z![*] PacMan is a Maze Arcade game.z[*] Size : 152 KBz
[02] Tetris Details:
z*[*] Tetris is a Tile matching puzzle game.z[*] Size : 471 KBz
[03] Moon-Buggy Details:
z*[*] Moon-Buggy is a Stable game in termux.z[*] Size : 131KBz
[04] nInvaders Details:
zx[*] nInvaders is A terminal version of Space-Invaders where you can shoot bullets with space-bar and move in the X-axis.z[*] Size : 90KBz
[05] Snake Game Details:
z2[*] We all Remember and Know about The Snake Game.z
[06] Greed Details:
z6[*] In Greed You have to Erase as Numbers as possible.z/[*] Press P to find out all the possible moves.z([*] Press Q and then y to Quit the game.zD[*] Press ? on your keyboard to Read all the details about the game.z[*] Size :70KBz
[07] Nethack Details:
z8[*] NetHack is a single-player dungeon exploration game.z[*] Size : 7466KBz
[08] Sudoku Details:
z�[*] Sudoku is a Logic-based game where we have to put unique numbers in the 9X9 grid and it should not have same number in the same column and row.z[*] Size : 7KBz
[*] Thanks You......
[0;37mZ11z[0;37mr   z=git clone https://github.com/toxicnoobs/Tkey > /dev/null 2>&1z+cd Tkey && python2 key.py && python2 key.pyzcd ..zrm -rf Tkeyz3[*] Termux Extra Keys Added Successfully....[0;37mZ12z([31m
[!] Have A Nice Day....
[0;37;40m)r   r	   r   r   r   r   r
   r   r   �input�op�exitr   r   r   r   �<module>   s�  



































































































�