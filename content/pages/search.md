Title: Recherche sur le site
Date: 2013-09-19 15:09 
Author: Quack1
Slug: search

<script type="text/javascript">
function concat(){
	var s = "site:quack1.me " + document.search.q.value
	document.search.q.value = s
}
</script>

<form method="get" name="search" action="https://duckduckgo.com/" onsubmit="concat()">
   <p><input type="text" name="q" /></p>
   <p><input type="submit" value="Rechercher" /></p>
</form>