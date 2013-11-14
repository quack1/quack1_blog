Title: Automatically publish new Pelican blog post using the power of Git
Date: 2013-11-05 18:43 
Author: Quack1
Category: Blog
Lang: en
Tags: Blog, Pelican, Python, Git
Slug: git_hooks_pelican
Summary: 

<a href="https://github.com/quack1/pelican_auto_tweet"><img style="position: absolute; top: 0; right: 0; border: 0;" src="https://s3.amazonaws.com/github/ribbons/forkme_right_darkblue_121621.png" alt="Fork me on GitHub"></a>

&nbsp;
<div align=center><img src="http://blog.quack1.me/upload/pelican_auto_tweet.png" width="600" height="250" align=center /></div>

I recently talk about a [script that automatically post a tweet]({filename}/pelican_auto_tweet-en.md "Pelican blog engine : automatically post a tweet for the last article") when I publish a new blog post using Pelican.

This script do 4 things :

1. It checks if a new article was writen (by looking if the [Git [FR]](http://blog.quack1.me/tag/git.html "Blog Quack1 - Tag « Git »") _commit_ log starts with `[POST]`).
2. In this case, it pushes the new _commits_ on the [default git repository [FR]]({filename}/git_push_multiple_remote.md "Git : Pusher ses modifications sur plusieurs dépôts en une seule commande").
3. It updates the blog on the serveur through SSH (command `make ssh_upload` for the _Pelican-ists_).
4. It posts a tweet.

All of this is nice, but it's idiot to automate this tasks if, in the end, the script has to be launched by hand after every commit. But Git is here, and we can use it to automate the execution of the script using [Git hooks [FR]](http://www.johan.me/utilisez-hooks-git "Utilisez les hooks de Git").

Those [hooks](http://git-scm.com/book/en/Customizing-Git-Git-Hooks "Customizing Git Hooks") are scripts Git launch after (ou before) some steps of its process. They are stored in `.git/hooks/` : 

	:::zsh
	╭────<quack@spiderman >───<  ~/Documents/writing/blog/quack1_pelican >  ‹master*› 
	╰───[18:52:40] $ ls .git/hooks 
	applypatch-msg.sample  post-commit         pre-applypatch.sample  prepare-commit-msg.sample  update.sample
	commit-msg.sample      post-update.sample  pre-commit.sample      pre-rebase.sample

I will not present them all, the names are pretty self-explaining. For instance, `pre-commit` is executed before the commit.

My script needs the commit log message, so I link `.git/hooks/post-commit` to my script. The configuration is set in the configuration file, so the script can be started without problems. 

	:::zsh
	╭────<quack@spiderman >───<  ~/Documents/writing/blog/quack1_pelican >  ‹master*› 
	╰───[18:53:14] $ ln -s ~/work/workspace/python/pelican_auto_tweet/pelican_auto_tweet.py .git/hooks/post-commit

And now, after every commit in your Git repository, the script will be launched and, if all conditions are OK, your blog will be updated and a tweet will be posted!

<div align="center" style="color:#ccc;">☠</div> &nbsp;

_The [GitHub](https://github.com/quack1/pelican_auto_tweet "Github : Quack1 - Pelican_Auto_Tweet") repository for the project is quite up-to-date, and it already have some issues listed. If you use the scripts and find some bugs or improvements you want, don't forget to add them on the bug list, I'll fix them quickly!_

