class Varasto:
    def __init__(self, tilavuus, alku_saldo=0):
        self.tilavuus = self._korjattu_tilavuus(tilavuus)
        self.saldo = self._korjattu_saldo(alku_saldo)

    def _korjattu_tilavuus(self, tilavuus):
        if tilavuus > 0:
            return tilavuus
        return 0.0

    def _korjattu_saldo(self, alku_saldo):
        if alku_saldo < 0:
            return 0.0
        if alku_saldo <= self.tilavuus:
            return alku_saldo
        return self.tilavuus

    def paljonko_mahtuu(self):
        return self.tilavuus - self.saldo

    def lisaa_varastoon(self, maara):
        if maara < 0:
            return

        tilaa_jaljella = self.paljonko_mahtuu()
        if maara <= tilaa_jaljella:
            self.saldo += maara
        else:
            self.saldo = self.tilavuus

    def ota_varastosta(self, maara):
        if maara < 0:
            return 0.0

        if maara > self.saldo:
            kaikki_mita_voidaan = self.saldo
            self.saldo = 0.0
            return kaikki_mita_voidaan

        self.saldo -= maara
        return maara

    def __str__(self):
        tilaa = self.paljonko_mahtuu()
        return f"saldo = {self.saldo}, vielä tilaa {tilaa}"
