Title: Tunnelize GPG into a SOCKS proxy
Date: 2013-05-24 09:12
Author: Quack1
Category: Linux
Slug: gpg_proxy_socks
Tags: Linux, GPG, SOCKS, en
Summary: Options to add to GPG to make all its trafic go through a SOCKS proxy.
Lang: en

&nbsp;
<div align=center><img src="upload/matrix.png" width="600" height="250" align=center /></div>

At day work, don't ask me why, the firewall is blocking the _hkp_ port (11371/tcp) that is commonly used to get GPG keys from the Internet (but, contrairiwise, we can access to Mega...). Anyway, it's kind of a pain in he ass when you have to fetcg some keys and update the APT repository on my Ubuntu, since _apt_ needs GPG keys in order to authenticate servers.

The solution I thought about was to make GPG communications went through my SOCKS proxy (mounted with ssh, more [informations here [fr]](http://artisan.karma-lab.net/faire-passer-trafic-tunnel-ssh)). To do that, you only have to add a simple _gpg_ option to set the SOCKS proxy URI.

	:::zsh
	╭────<quack@spiderman >───< ~ >  
	╰───[17:13:13] $ gpg --keyserver-options http-proxy=socks5-hostname://127.0.0.1:1080

And, to come back to the first problem, to import a _gpg_ key from _apt_, we just add the same option as for _gpg_ : 

	::zsh
	╭────<quack@spiderman >───<  /etc/apt/sources.list.d >  
	╰───[17:25:35] $ sudo apt-key adv --keyserver-options http-proxy=socks5-hostname://127.0.0.1:1080 --keyserver keyserver.ubuntu.com --recv-keys C383CF524EE6B458

[Source](http://lists.gnupg.org/pipermail/gnupg-devel/2012-September/026930.html)