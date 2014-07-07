Title: Empêcher l'extinction des périphériques USB sur batterie avec laptop_mode_tools (XUbuntu)
Date: 2014-07-07 20:14
Author: Quack1
Category: Linux
Tags: Linux, Ubuntu, XUbuntu, USB, planet-libre, planet-ubuntu
Slug: xubuntu_usb_no_sleep
Summary: Sur XUbuntu 14.04 avec `laptop_mode_tools`, les périphériques USB qui ne sont pas utilisés pendant quelques secondes sont automatiquement éteints. C'est le cas des souris par exemple, ce qui est très génant. Il est cependant possible de modifier la configuration de `laptop_mode_tools` pour désactiver ce comportement.
Lang: fr

Sur XUbuntu 14.04 avec `laptop_mode_tools`, les périphériques USB qui ne sont pas utilisés pendant quelques secondes sont automatiquement éteints. C'est le cas des souris par exemple, ce qui est très génant. Il est cependant possible de modifier la configuration de `laptop_mode_tools` pour désactiver ce comportement.

On modifie le fichier `/etc/laptop-mode/conf.d/usb-autosuspend.conf` pour lui demander de _blacklister_ du processus d'extinction plusieurs types de périphériques USB. Dans mon cas, les souris et les clés USB.

	:::bash
	$ grep 'AUTOSUSPEND_USBTYPE_BLACKLIST' /etc/laptop-mode/conf.d/usb-autosuspend.conf
	AUTOSUSPEND_USBTYPE_BLACKLIST="usbhid usb-storage" 

La modification est effective après sauvegarde du fichier.

[Via AskUbuntu](http://askubuntu.com/questions/141832/usb-mouse-sleeping-after-5-seconds-when-on-battery)