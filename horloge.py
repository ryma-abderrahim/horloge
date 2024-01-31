import time
import threading

class Horloge:
    def __init__(self, mode_12h=False):
        self.mode_12h = mode_12h
        self.pause = False
        self.heure_alarme = None

    def afficher_heure(self, heures, minutes, secondes):
        if self.mode_12h:
            suffixe = "AM" if heures < 12 else "PM"
            heures = heures % 12 or 12
        else:
            suffixe = ""
        heure_format = f"{heures:02d}:{minutes:02d}:{secondes:02d} {suffixe}"
        print(heure_format)

    def regler_heure(self, heures, minutes, secondes):
        self.afficher_heure(heures, minutes, secondes)

    def regler_alarme(self, heures, minutes, secondes):
        self.heure_alarme = (heures, minutes, secondes)

    def afficher_alarme(self):
        if self.heure_alarme:
            if time.localtime().tm_hour == self.heure_alarme[0] and \
               time.localtime().tm_min == self.heure_alarme[1] and \
               time.localtime().tm_sec == self.heure_alarme[2]:
                print("Alarme! Il est temps.")

    def changer_mode_affichage(self):
        self.mode_12h = not self.mode_12h

    def mettre_en_pause(self):
        self.pause = True

    def reprendre(self):
        self.pause = False
        self.actualiser_heure()

    def actualiser_heure(self):
        while not self.pause:
            temps_actuel = time.localtime()
            heures, minutes, secondes = temps_actuel.tm_hour, temps_actuel.tm_min, temps_actuel.tm_sec
            self.afficher_heure(heures, minutes, secondes)
            self.afficher_alarme()
            time.sleep(1)

# Exemple d'utilisation
horloge = Horloge()
horloge.regler_heure(16, 30, 0)
horloge.regler_alarme(16, 31, 0)

# Démarrer le thread d'actualisation de l'heure
thread_heure = threading.Thread(target=horloge.actualiser_heure)
thread_heure.start()

# Laisser l'horloge fonctionner pendant 10 secondes
time.sleep(10)

# Mettre en pause l'horloge pendant 5 secondes
horloge.mettre_en_pause()
time.sleep(5)

# Reprendre l'horloge pendant 5 secondes
horloge.reprendre()
time.sleep(5)

# Changer le mode d'affichage
horloge.changer_mode_affichage()

# Arrêter le thread
thread_heure.join()
