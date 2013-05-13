Title: Tester Linux dans un émulateur javascript
Date: 2012-05-12 18:45
Author: Quack1
Category: Linux
Tags: emulation, javascript, linux, planet-libre, planet-ubuntu
Summary: Tester GNU/Linux simple dans un émulateur écrit en Javascript.

<div align=center><a href="static/upload/jslinux.png"><img src="static/upload/jslinux.png" width="600" align=center /></a></div>

Cette info va avoir 1 an dans quelques jours mais j'avais quand même
envie d'en parler ici.

[Fabrice Bellard][] (qui est également à l'origine de [ffmpeg][]) a
développé un système Linux entièrement en Javascript, basé sur le noyau
2.6.20, et une machine 32 bits.

Il possède donc toutes les commandes Linux, un compilateur tcc (Tiny C
Compiler, aussi développé par le monsieur, plus rapide que gcc, qui est
aussi présent), vi, QEmacs (un clone d'Emacs plus léger, aussi l'oeuvre
de Mr Bellard). Vous pouvez donc compiler vos propres programmes C et
les tester en ligne. Attention cependant, c'est plutôt long, même avec
tcc. Ici, un simple "Hello World" a nécéssité 19s de compil avec gcc,
pour 1 sur ma machine.

Bref, je pense pas non plus que vous alliez développer dessus, mais pour
essayer deux trois commandes Linux et s'y former sans installer de
système complet, ça peut être intéressant ;-) Vous pouvez le trouver
[ici][].

Pour info, ce n'est pas un coup d'essai pour le monsieur en terme
d'émulation, il est aussi le créateur du logiciel d'émulation de
machines [Qemu][]!

  [Fabrice Bellard]: http://bellard.org "Bellard.org"
  [ffmpeg]: https://quack1.wordpress.com/tag/ffmpeg/ "FFmpeg"
  [ici]: http://bellard.org/jslinux/ "JsLinux"
  [Qemu]: http://wiki.qemu.org "Qemu"
