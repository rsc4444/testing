class Fahrzeug():
    """ Klasse für das Erstellen von Fahrzeugen """

    def __init__(self, farbe, baujahr, kmstand, sitze, marke):
        """ Eigenschaften farbe, baujahr, kmstand, Sitzplätze, Marke erfassen """
        self.farbe   = farbe
        self.baujahr = baujahr
        self.kmstand = kmstand
        self.sitze   = sitze
        self.marke   = marke

    def hupen(self):
        """ hier sollte noch eine MP3-Datei ausgegeben werden """
        print("Trööt")

    def fahren(self, km):
        """ wie viele KM gefahren werden, was dem Tachostand aufaddiert wird """
        self.kmstand += km
        print("Ich fahre ", km, " Kilometer")
        print("Ich habe ", self.kmstand ," auf dem Tacho")

    def parken(self):
        """ neben fahren schon das größere Problem in Städten """
        print("Ich habe eine Parkplatz gefunden")

    def kilometerstand(self):
        """ Ausgabe des KM-Standes vom Tacho """
        print("Ich habe ", self.kmstand ," auf dem Tacho")

class Pkw(Fahrzeug):
    """ Klasse für das Erstellen von Personenkraftwagen """

    def __init__(self, farbe, baujahr, kmstand, sitze, marke):
        super().__init__(farbe, baujahr, kmstand, sitze, marke)

trabi = Pkw("rot", 1981, 143000, 4, "Trabi")
trabi.hupen()
trabi.kilometerstand()
trabi.fahren(5)