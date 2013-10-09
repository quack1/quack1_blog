Title: Pelican blog engine : automatically post a tweet for the last article
Date: 2013-10-09 10:17
Author: Quack1
Category: Blog
Tags: Blog, Pelican, Python, en
Slug: pelican_auto_tweet
Lang: en
Summary: The only thing that the Pelican blog engine miss, it's the possibility to send a tweet automatically for the lasts posts. Then, now, there is a Python script for that! :)

For [this blog [fr]]({filename}/blog_v3.md), I use the [Pelican](http://getpelican.com) blog engine.

I will not, again, say why I love it, many blog posts already did it. I will just say that I like it because I can write my posts in Markdown, use Git to version them, and publish the blog through SSH on my server.

The only thing I miss, since I moved out of Wordpress, is the possibility to automatically post a [tweet](https://twitter.com/_Quack1) when I publish a new post.

To solve the problem, I developed [a little script](https://github.com/quack1/pelican_auto_tweet) that can do this rapidly.

Its usage is simple. It gets the last Git log from the project directory. If the commit message starts with `[POST]` (it is the convention I use for my commit messages when I publish a new post), the script sends a tweet. For this, it gets le title and the URL directly into the article source file. 

If you want more details on how to install it, to use it, etc, the best thing to do is to read the [README](https://github.com/quack1/pelican_auto_tweet) on Github ;).

The scripts are published under a BSD license, there are available on [Github](https://github.com/quack1/pelican_auto_tweet), and I'm waiting for your commentaries, issues and improvements ideas ;-)

\#Teasing : I will publish soon an article about the second script available in the Git repository, and about a trick to automate the usage of the script with Git.