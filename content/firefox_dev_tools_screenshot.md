Title: Faire des screenshots de sites web directement depuis Firefox
Date: 2013-04-02 13:46
Author: Quack1
Category: Geek
Slug: firefox_dev_tools_screenshots
Tags: screenshot, web, page, firefox
Summary: Prendre des captures d'écran de sites Web depuis Firefox en utilisant les outils de développeur.

&nbsp;
<div align=center><img src="static/upload/firefox_dev_tools_screenshot.png" width="600" height="250" align=center /></div>

Si vous êtes utilisateur de [Firefox](https://www.mozilla.org/fr/firefox/fx/ "Mozilla Firefox") et que vous réalisez souvent des captures d'écran, vous âvez sûrement un outil comme Shutter (pour Linux) ou des outils spécifiques pour votre OS.

Cependant, tous n'intègrent pas la capture de site web. Et bien Mozilla a intégré cette fonctionnalité au sein de ses outils pour développeurs afin d'accélerer et faciliter cette utilisation!

Pour cela, il faut accéder à la _Barre de Développement_ dans _Outils_ > _Développeur Web_, ou bien en pressant _Maj+F2_.

Ensuite, on appelle la commande `screenshot`. Pour voir les options dispo, commencez à écrire un ou deux tirets, et un menu les affichera.

<div align=center><a href="static/upload/firefox_screenshot_opt.png"><img src="static/upload/firefox_screenshot_opt.png" align="center"/></a></div>

Les deux que je retiens sont : 

- `--fullpage` pour prendre la page complète
- `--chrome` pour prendre la totalité de la fenêtre de Firefox

Si vous ne mettez aucune option, Firefox prendre simplement une screenshot du contenu de la page affiché, et enregistrera le tout dans `${HOME}/Téléchargements/Capture d'écran du XX/XX/20XX à XXhXX.png`

Vous pouvez donner un nom à la capture d'écran en le rajoutant à la fin de la commande!


<div align=center><code>screenshot --chrome screen1.png</code><br/><a href="static/upload/firefox_screenshot_chrome.png"><img src="static/upload/firefox_screenshot_chrome.png" align="center" width="500px"/></a></div>
&nbsp;
<div align=center><code>screenshot --fullpage screen1.png</code><br/><a href="static/upload/firefox_screenshot_fullpage.png"><img src="static/upload/firefox_screenshot_fullpage.png" align="center" width="500px"/></a></div>

Enjoy ;-)

Source : [@jonobacon](https://twitter.com/jonobacon/status/317495735203528704 "Source : @jonobacon")
