Title: Set up a Development Environment for Mozilla Persona
Date: 2013-05-24 21:37
Author: Quack1
Category: Mozilla
Slug: persona_setup_ubuntu
Tags: Linux, Ubuntu, Mozilla, Persona, Dev, Nodejs
Summary: Steps to easily set up a complete development environment from scratch from Mozilla Persona (browserid project) on Ubuntu 13.04.
Lang: en

&nbsp;
<div align=center><img src="static/upload/persona.png" align=center /></div>

For many years I wanted to contribute to an Open-Source Project. Now, things are becoming true. I found **the** project I want to help : [Mozilla Persona](https://login.persona.org/about "Mozilla Persona About Page"). But I don't do the things in the right order, I'll write soon another post to present it more!

Here I'll just detail the steps to set up a complete development environment on a GNU/Linux system, especially on Ubuntu 13.04.

# Being friend with GitHub

The first thing to do if you want to contribute is to register on [GitHub](https://github.com "Github.com"), and then to fork the project.

When you have done that, clone the repository on your machine : 

	:::zsh
	╭────<quack@spiderman >───<  ~/work/workspace/mozilla >
	╰───[18:11:29] $ git clone https://github.com/quack1/browserid.git

Then, go on it and add a new remote host. The new one will be the _official_ repository we will pull new data from.

	:::zsh
	╭────<quack@spiderman >───<  ~/work/workspace/mozilla >
	╰───[18:13:49] $ cd browserid 
	╭────<quack@spiderman >───<  ~/work/workspace/mozilla/browserid >  ‹dev› 
	╰───[18:13:55] $ git remote add mozilla https://github.com/mozilla/browserid.git

This way, to update the sources we will simply do :

	:::zsh
	╭────<quack@spiderman >───<  ~/work/workspace/mozilla/browserid >  ‹dev› 
	╰───[18:14:12] $ git pull mozilla dev

And to push our modifications to our own repo : 

	:::zsh
	╭────<quack@spiderman >───<  ~/work/workspace/mozilla/browserid >  ‹dev› 
	╰───[18:14:20] $ git push origin dev

We will propose our commits to the Persona core development team with the Pull Request system included into GitHub.

# Working with Nodejs

Since Persona is written in [Node.js](http://nodejs.org/ "Node.js Website") for the server side, we need to install it in order to test our code.

Before installing Nodejs, we need some other tools : 

	:::zsh
	╭────<quack@spiderman >───<  ~/work/workspace/mozilla/browserid >  ‹dev› 
	╰───[18:15:02] $ sudo apt-get install python-software-properties git-core libgmp3-dev g++ libssl-dev

And now, we can install Node. But **don't** install nodejs directly from the Ubuntu repository or from the sources available on the official website, because the current version is the 0.10.*, and Persona is still only working with the 0.8.*.

The best way to do was given to me by [Shane Tomlinson](https://twitter.com/Shane_Tomlinson "Shane Tomlinson Twitter Page"), and it consists to delegate the management of the versions of Node.js to a simple program : **nvm**. This last one can install multiple versions of Node, and you can tell it which one you want to run a script with.

To install it, just follow the [instructions given on the website](https://github.com/creationix/nvm/). To make it easier, this is the command you have to type : 

	:::zsh
	╭────<quack@spiderman >───<  ~/work/softs > 
	╰───[18:17:47] $ git clone http://github.com/creationix/nvm.git nvm
	╭────<quack@spiderman >───<  ~/work/softs > 
	╰───[18:17:58] $ echo '. /home/quack/work/softs/nvm/nvm.sh' > ~/.zshrc

Don't forget to update the last command with the directory you cloned the repo into and with the configuration file of your shell (by default, in Ubuntu, it's `~/.bashrc`). Start a new terminal and the `nvm` command should work.

After that, install the latest working version of Node.js, and set it as the default version : 

	:::zsh
	╭────<quack@spiderman >───<  ~/work/workspace/mozilla/browserid >  ‹dev› 
	╰───[18:19:30] $ nvm install 0.8.12
	╭────<quack@spiderman >───<  ~/work/workspace/mozilla/browserid >  ‹dev› 
	╰───[18:19:49] $ nvm alias default 0.8.12

And now, we can install all the Node modules needed to make Persona work. Go to the root directory of the browserid repository, and launch the following command :

	:::zsh
	╭────<quack@spiderman >───<  ~/work/workspace/mozilla/browserid >  ‹dev› 
	╰───[18:20:15] $ npm install

And, normally, all the modules are installed and you can work well! If you want to start the examples given into the sources : 

	:::zsh
	╭────<quack@spiderman >───<  ~/work/workspace/mozilla/browserid >  ‹dev› 
	╰───[18:20:20] $ npm start

The example web application is available at [http://localhost:10001](http://localhost:10001), and the example Browserid server at [http://localhost:10002](http://localhost:10002).

# But `bcrypt` doesn't work...

If, during the `npm install` you add an error message that said something like _"can't import module 'bcrypt'"_, try to import the good version directly : 

	:::zsh
	╭────<quack@spiderman >───<  ~/work/workspace/mozilla/browserid >  ‹dev› 
	╰───[18:20:20] $ npm install bcrypt@0.7.3

Do a new `npm install`, and if that still doesn't work, you'll need to install it manually.

To make it simple, the following commands will : clone the sources, configure the compilation, compile the sources, and install them again with npm.

	:::zsh
	╭────<quack@spiderman >───<  /tmp > 
	╰───[18:20:20] $ git clone http://github.com/ncb000gt/node.bcrypt.js.git
	╭────<quack@spiderman >───<  /tmp > 
	╰───[18:21:20] $ cd node.bcrypt.js
	╭────<quack@spiderman >───<  /tmp > 
	╰───[18:22:20] $ npm install -g node-gyp
	╭────<quack@spiderman >───<  /tmp > 
	╰───[18:23:20] $ node-gyp configure
	╭────<quack@spiderman >───<  /tmp > 
	╰───[18:24:20] $ node-gyp build
	╭────<quack@spiderman >───<  /tmp > 
	╰───[18:25:20] $ cd ~/work/workspace/mozilla/browserid
	╭────<quack@spiderman >───<  /tmp > 
	╰───[18:25:22] $ rm -rf var node_modules
	╭────<quack@spiderman >───<  ~/work/workspace/mozilla/browserid >  ‹dev› 
	╰───[18:26:20] $ npm install

Normally, after that last step, everything should work with a `npm start`.

# Updating the sources

Now, everytime you will update the sources, you will need to re-install the Node modules to use the latest versions needed be Persona.

The update process will be :

	:::zsh
	╭────<quack@spiderman >───<  ~/work/workspace/mozilla/browserid >  ‹dev›  
	╰───[18:23:20] $ git pull mozilla dev
	╭────<quack@spiderman >───<  ~/work/workspace/mozilla/browserid >  ‹dev›  
	╰───[18:31:20] $ rm -rf var node_modules
	╭────<quack@spiderman >───<  ~/work/workspace/mozilla/browserid >  ‹dev› 
	╰───[18:32:20] $ npm install

And now, it's time to you to hack the code!

&nbsp;

_If you notice some mistakes, grammar mistakes made by the french guy I am, or if you want more precisions, don't hesitate to send me an [email](quack1blog@gmail.com), contact me via [Twitter](http://twitter.com/_Quack1) or join the IRC channel of the Identity team : [#identity@irc.mozilla.org](irc://irc.mozilla.org/identity). The guys from this chan are great and always ready to help you!_

Some particular thanks to [Shane Tomlinson](https://shanetomlinson.com/ "Shane Tomlinson Personal Website") who spent about the entire afternoon helping me out on IRC to install my dev. environment!

For more informations, you can read the [README available on the project GitHub repository](https://github.com/mozilla/browserid/blob/dev/README.md)