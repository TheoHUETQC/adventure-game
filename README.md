# 🌳 Adventure Game

Un monde en 2D généré de manière procédurale, inspiré de Minecraft, développé avec Python et Pygame.
Ce projet, c’est plus qu’un simple jeu : c’est un rêve d’enfant. L’envie de rassembler tout ce que j’aime dans les jeux auxquels j’ai joué, d’en faire une œuvre personnelle dont je serais fier. Le jeu vidéo est une forme d’art, et j’aimerais un jour partager le mien.

Je débute petit, en partant de zéro, avec Python. J'aimerais à terme de passer au C++, un langage que je connais encore trop peu mais que j’aimerais maîtriser. Pour l’instant, j’ai créé une carte entièrement aléatoire et jouable en 2D.

Je rêve d’un jeu vivant, avec des personnages complexes, des émotions, des retournements, une physique cohérente. Pour l’instant, je construis les bases d’un jeu de survie en 2D, mais un jour peut-être j’ajouterai de la 3D, basculerai sur C++, créerai des PNJ profonds, des mondes cohérents, des boss marquants et des mécaniques plus ambitieuses.
J’avance pas à pas, en passionné et en rêveur, pleinement conscient que ce projet pourrait ne jamais être “fini”, mais qu’il mérite d’exister.

---

## Objectifs du Projet
- [X] generer une carte completement aléatoire
- [X] Intéragir avec l'environnement
- [ ] Affichage 2D avec Pygame
- [ ] Création d'une map cohérente en utilisant des bruits et une seed
- [ ] Passer en C++

---

## Carte Mentale du Projet (Mermaid)

Ces cartes mentales me permettent d’organiser toutes mes idées sans en perdre une seule. Elles séparent l’histoire, l’aspect artistique et la partie technique du jeu afin que mon projet reste cohérent, lisible et facile à développer au fil du temps.

### 1. Histoire
```mermaid
mindmap
  root((Histoire))
    autre
    point de depart
      méchant presente notre hero comme un fils de dieux capable de sauver le monde pour eviter de detruire le monde
      le dieu est tombé il faut le faire remonter au throne
        faut tuer les boss cest a cause d'eux
      on va mourir au debut et arriver dans le monde du passé, on va pouvoir discuter avec les pnj pour voir qu'il voue un culte au boss qu'on a tué
    objectif
      comprendre que le monde est inversé le méchant ne veux pas le sauver mais le laisser detruit et sans dieux, on l'aide depuis le depart en tuant les boss qui sont les derniers rampart
      deux choix
        laisser le monde comme ca pour aider le mechant et rester puissant mais laisser tout les habitant dans la detresse de la vie eternelle
          tuer les habitants pour etre le bras droit du méchant et dominer le monde
        aider le monde a revenir comme avant mais disparaitre parce qu il n y a pas de raison de venir
          mourir pour laisser les habitants en vie et vivre comme avant
    secondaire
      pnj
        opinion : pour avoir leur aide il faut etre du meme opignons
        mémoire : si tu les aides ou aide leur proche il t aideront
        leur vie
          habitude : tout les jours il rentre chez eux..
          travail : permet de les faire deplacer dans la map
          connaissance : il se transmette les infos sur toi et le monde
    personnage
      principale
      méchant
        se fait passer pour le gentil quand le héro arrive
        donne pour mission au héro d'aller tuer des boss qui sont gentil
      dieu
        guide le joueur
        donne la "quete"
      Boss
        mourir ne refait pas recommencer, tu es réanimé par le boss par exemple
        tu ne vas pas tué le boss final, tu finis par l'épargné parce qu il faut jouer avec les émotions du joueur, tu l'as detester pour finalement le laisser
        les bosses sont inofensif au depart, ils paraissent gentil ce qui fait douter le joueur, ref :shadow of colossus
        certain te font changer de methode de combat a chaque degat infligé pour te forcer a reflechir, ref : Mr freeze arkham city
```

### 2. Artistique
```mermaid
mindmap
  root((Artistique))
    autre
    couleur : change en fonction de l ambiance
      triste : bleu
      degout : vert
      joie : jaune orange
      rouge : enervement
    camera
      plan
        oblige le joueur a regarder certain detail
          exemple fumé ou brouillard pour obliger le joueur a regarder le ciel
          exemple couloir ou quand on sort on regarde devant
        plan large quand calme pour montrer le paysage
      vu 3eme personne
        plus de liberté pour les plans
        bien pour les combats et le realisme
    lumiere
      ilumine les objets et zone importante
    guidage du joueur
      terrain et objet de certaine couleur
      lumiere pour guider
      deplacement et mouvement, exemple un mec qui fuit le danger, indique la direction a prendre vu qu il vient du danger
    son
      musique
        change en fonction des actions du joueur et de l environement
      bruitage
        realiste
        s accorde avec la musique pour creer une nouvelle musique unique pour le joueur
```

### 3. Code
```mermaid
mindmap
  root((Code))
    autre
    entité
      Joueur
      Monstre
      Arbre
        peuvent etre detruit pour faire du bois
      Coffre
        permet de recuperer des items
    monde
      present
        dieux est tombé sur cette plaine, monde en ruine
        les habitants et etre vivants sont des demons
      passé/monde de la mort
        on arrive ici lorsque l'on "meurt" dans le jeu, ici on ne peut pas mourir, tout est inofensif
        reviens avant le desastre les habitants sont normaux
        ici que le joueur peut reparer le monde
    monde procédural
      chunk
        défini par la seed, le bruit
        chargé quand le joueur est proche
      monde generer aleatoirement
        mais delimiterpar une map precise
          entouré de montagne au nord ouest et mer au sud est
          ville et lieux dit obligatoire
          riviere avec des ponts a reparer qui traverse la map de nord ouest a sud est
        seed
    item
      ressource (pour reparer et craft)
        bois
        pierre
      outil
        hache
        épée
        pioche
      objet magique
        montre a gousset
          permet de passer dans l autre monde : passé ou present
            permet desquiver des ennemies ou modifier un chemain et que ca deviene pratiquable, comme titanfall
          en changeant de monde on a notre nous du passé, il y a 10sec, qu on voit
            peut etre utile pour affronter des mob ou se faire la courte echelle ou deplacer lourd objet a deux
    mécanique
      survie
        couper arbre
        fouiller coffre
        craft
      combat
        systeme d'épée comme chivalry
      changer de monde

```

