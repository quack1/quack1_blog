Title: Dev. Android : Activity en plein écran
Date: 2012-02-19 19:15
Author: Quack1
Category: Geek
Tags: activity, android, code java, fullscreen, plein ecran
Summary: Permettre à des applications Android de se lancer en plein écran, en masquant la barre de statut.

Ce matin, j'avais besoin pour un projet de développement sur Android de
mettre une Activity en plein écran, c'est à dire supprimer la barre de
titre ainsi que la barre d'état du système. Je préfère noter ça ici,
j'en aurait sûrement besoin une autre fois et au moins je saurais où
chercher!!

Pour ça, j'ai trouvé 2 solutions. La première qui consiste à modifier le
code java, la deuxième qui se situe dans le AndroidManifest.xml. Perso,
j'ai utilisé la deuxième solution, mais je vais parler des deux, on sait
jamais, la première pourra peut être servir un jour ;-)

### La méthode Java :

Pour cette méthode on rajoute 2 lignes dans la méthode onCreate() de
l'Activity. Une ligne pour supprimer la barre de titre, et une autre
pour la barre d'état.

	:::java
	@Overridepublic void onCreate(Bundle savedInstanceState) {
	  super.onCreate(savedInstanceState);
	  // Pour cacher la barre de titre
	  requestWindowFeature(Window.FEATURE_NO_TITLE);
	  setContentView(R.layout.tabs1);
	  // Pour cacher la barre de statut et donc mettre votre application en plein écran
	  getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN,WindowManager.LayoutParams.FLAG_FULLSCREEN);
	}

### La méthode AndroidManifest.xml

Pour la deuxième méthode, on peut rajouter soit ceci pour supprimer la
barre de titre :


    <activity android:name=".LeNomDeVotreClasse" android:theme="@android:style/Theme.NoTitleBar"/>;


Soit ceci pour masquer la barre de titre et placer l'application en
plein écran :


    <activity  android:name=".LeNomDeVotreClasse" android:theme="@android:style/Theme.NoTitleBar.Fullscreen">;


[Source][]

  [Source]: http://www.tutomobile.fr/afficher-son-application-android-en-plein-ecran-tutoriel-android-n%C2%B013/30/07/2010/ "http://www.tutomobile.fr/afficher-son-application-android-en-plein-ecran-tutoriel-android-n%C2%B013/30/07/2010/"
