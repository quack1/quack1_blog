Title: Pelican blog engine : automatically post a tweet for the last article
Date: 2013-10-09 10:17
Author: Quack1
Category: Blog
Tags: Blog, Pelican, Python, en
Slug: pelican_auto_tweet
Lang: en
Summary: The only thing that the Pelican blog engine miss, it's the possibility to send a tweet automatically for the lasts posts. Then, now, there is a Python script for that! :)

<a href="https://github.com/quack1/pelican_auto_tweet"><img style="position: absolute; top: 0; right: 0; border: 0;" src="https://s3.amazonaws.com/github/ribbons/forkme_right_darkblue_121621.png" alt="Fork me on GitHub"></a>

For [this blog [fr]]({filename}/blog_v3.md), I use the [Pelican](http://getpelican.com) blog engine.

I will not, again, say why I love it, many blog posts already did it. I will just say that I like it because I can write my posts in Markdown, use Git to version them, and publish the blog through SSH on my server.

The only thing I miss, since I moved out of Wordpress, is the possibility to automatically post a [tweet](https://twitter.com/_Quack1) when I publish a new post.

To solve the problem, I developed [a little script](https://github.com/quack1/pelican_auto_tweet) that can do this rapidly.

Its usage is simple. It gets the last Git log from the project directory. If the commit message starts with `[POST]` (it is the convention I use for my commit messages when I publish a new post), the script sends a tweet. For this, it gets the title and the URL directly into the article source file. 

It does this : 

1. It checks if a new article was writen (by looking if the [Git [FR]](http://blog.quack1.me/tag/git.html "Blog Quack1 - Tag « Git »") _commit_ log starts with `[POST]`).
2. In this case, it pushes the new _commits_ on the [default git repository [FR]]({filename}/git_push_multiple_remote.md "Git : Pusher ses modifications sur plusieurs dépôts en une seule commande").
3. It updates the blog on the serveur through SSH (command `make ssh_upload` for the _Pelican-ists_).
4. It posts a tweet.

If you want more details on how to install it, to use it, etc, the best thing to do is to read the [README](https://github.com/quack1/pelican_auto_tweet) on Github ;).

The scripts are published under a BSD license, there are available on [Github](https://github.com/quack1/pelican_auto_tweet), and I'm waiting for your commentaries, issues and improvements ideas ;-)

\#Teasing : I will publish soon an article about the second script available in the Git repository, and about a trick to automate the usage of the script with Git.

<div align="center" style="color:#ccc;">☠</div> &nbsp;

**EDIT :** I post a new post, explaining how [automate the execution of the script after each commit]({filename}/git_hooks_pelican-en.md "Automatically publish new Pelican blog post using the power of Git").