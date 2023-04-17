import turtle
import pandas as pd
from collections import defaultdict
from src.constants import MAG, PROPER, X, Y, DIST, BAYER
from src.constellation_drawing_utils import draw_orion_constellation
from src.constellation_dataset import constellation_dataset
from src.constants import (
    Betelgeuse, 
    Bellatrix, 
    Meissa, 
    Alnitak, 
    Alnilam, 
    Mintaka, 
    Saiph, 
    Rigel
)


class StarData:
    def __init__(self):
        self.STAR_DATA_PATH = "etc/hygdata_v3.csv"
        self.load_data()

    def load_data(self):
        df = pd.read_csv(self.STAR_DATA_PATH, index_col=-1)
        self.proper_to_magnitude = self.create_dict(df, key=PROPER, values=[MAG])
        self.proper_to_coordination = self.create_dict(df, key=PROPER, values=[X, Y])
        self.proper_to_dist = self.create_dict(df, key=PROPER, values=[DIST])
        self.proper_to_bayer = self.create_dict(df, key=PROPER, values=[BAYER])

    def get_magnitude_by_proper(self, proper):
        return self.proper_to_magnitude[proper][MAG] if proper in self.proper_to_magnitude else None

    def get_coordination_by_proper(self, proper):
        return self.proper_to_coordination[proper] if proper in self.proper_to_coordination else None
    
    def get_dist_by_proper(self, proper):
        return self.proper_to_dist[proper][DIST]*3.262 if proper in self.proper_to_dist else None
    
    def get_bayer_by_proper(self, proper):
        return self.proper_to_bayer[proper][BAYER] if proper in self.proper_to_bayer and BAYER in self.proper_to_bayer[proper] else None

    @staticmethod
    def search_by_value(df, target_col, search_value):
        row = df[df[target_col] == search_value]
        if not row.empty:
            return row
        return None
    
    @staticmethod
    def create_dict(df, key, values):
        non_proper_df = df.dropna(subset=key)
        key_values = defaultdict(dict)
        for iter, row in non_proper_df.iterrows():
            for val in values:
                if row[val]:
                    key_values[row[key]][val] = row[val]
        return key_values
    

class ConstellationData:
    def __init__(self) -> None:
        self.star_data = StarData()
        self.constellation_main_stars = {
            "Orion": (
                (Meissa, Betelgeuse),
                (Meissa, Bellatrix),
                (Betelgeuse, Bellatrix), 
                (Betelgeuse, Alnitak), 
                (Alnitak, Saiph), 
                (Alnitak, Alnilam), 
                (Alnilam, Mintaka), 
                (Bellatrix, Mintaka), 
                (Mintaka, Rigel), 
                (Saiph, Rigel),
                (Bellatrix, "pi-3"), 
                ("pi-3", "pi-2"), 
                ("pi-2", "pi-1"), 
                ("pi-3", "pi-4"), 
                ("pi-4", "pi-5"), 
                ("pi-5", "pi-6"), 
            )
        }

    def fetch_constellation_info(self, constellation):
        if constellation == "Orion":
            return constellation_dataset["Orion"]["info"]
        else:
            return None
        
    def fetch_constellation_map(self, constellation):
        if constellation == "Orion":
            return constellation_dataset["Orion"]["map_url"]
        else:
            return None

    def get_coordinates(self, constellation):
        """
        Get the coordination of each star in a constellation.
        """
        stars = set()
        collected_coordinations = []
        if constellation not in self.constellation_main_stars:
            raise ValueError(f"Unknown constellation name. We currently only support {self.constellation_main_stars.keys()}")
        star_connections = self.constellation_main_stars[constellation]
        for star_connection in star_connections:
            stars.add(star_connection[0])
            stars.add(star_connection[1])
        for star in stars:
            coordination = self.star_data.get_coordination_by_proper(star)
            if coordination:
                collected_coordinations.append([coordination["x"], coordination["y"]])
        return collected_coordinations

    def draw_constellation(self, constellation):
        if constellation == "Orion":
            draw_orion_constellation()



if __name__ == "__main__":
    # star_data = StarData()
    # star = ""
    # while star not in ["exit", "stop"]:
    #     star = input("\n> ")
    #     val = star_data.get_magnitude_by_proper(star)
    #     coordination = star_data.get_coordination_by_proper(star)
    #     dist = star_data.get_dist_by_proper(star)
    #     bayer = star_data.get_bayer_by_proper(star)
    #     print(val)
    #     print(coordination)
    #     print(dist)
    #     print(bayer)

    constellation_data = ConstellationData()
    constellation = ""
    while constellation not in ["exit", "stop"]:
        constellation = input("\n> ")
        constellation_data.draw_constellation(constellation)