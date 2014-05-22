Title: Pelican : Automatically add 'id' HTML attributes to titles
Date: 2014-05-22 19:43
Author: Quack1
Category: Blog
Tags: Blog, Pelican, Markdown, HTML, en
Slug: pelican_title_id
Summary: 
Lang: en

By default, with [the blog engine Pelican [fr]](/tag/pelican.html), in the output HTML code, title (`<h1>`, `<h2>`, `<h3>`, ...) are generated without `id` attributes.

For example, if I have the following in my [Markdown [fr]](/tag/markdown.html) source: 

	:::markdown
	Text

	# A title

	More text

the following HTML code will be generated:

	:::html
	<p>Text</p>
	<h1>A title</h1>
	<p>More text</p>

The bad thing is, without the `id` attributes, it's impossible to link directly to a specific part of the article. For instance, the link `/article.html#a-title` will not be valid.

It's possible with Pelican and Markdown to automate this, by activating in Pelican a Markdown extension, named `headerid`. It is integrated by default with every Pelican installation (at least in my Ubuntu), and it does not need any new installation.

To activate it, simply add the extension in the `pelicanconf.py` file:

	:::python
	MD_EXTENSIONS = ['headerid']

_Et voilà_. During each blog generation, the title will have an `id` attribute generated from the title text. And if two titles are the same, a number will be add at the end of the attribute.

	:::html
	<p>Text</p>
	<h1 id="a-title">A title</h1>
	<p>More text</p>

Now, I can link [to a precise part of an article [fr]](/homemade_guitar_rex.html#et-alors-on-fait-quoi-avec-tout-ca).

&nbsp;

For more info: 

- [Pelican documentation](http://pelican.readthedocs.org/en/latest/settings.html) ;
- [headerid extension in the Markdown documentation](http://pythonhosted.org/Markdown/extensions/header_id.html)