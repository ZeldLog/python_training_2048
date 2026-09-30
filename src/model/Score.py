import pandas as pd
class Score:
    def __init__(self):
        self.score = 0
        self.high_score = [("", 0)] * 10  # Liste des 10 meilleurs scores
        self.file_path = "high_scores.txt"
        
    def __str__(self):
        result = f"Votre score : {self.score}\n\n" 
        result += "Meilleurs scores :\n"
        for i, (name, score) in enumerate(self.high_score):
            result += f"{i + 1}. {name}: {score}\n"
        return result

    def add_points(self, points):
        self.score += points

    def get_score(self):
        return self.score
    
    def reset_score(self):
        self.score = 0
    
    def insert_high_score(self,name):
        """
        Insère un nouveau score dans la liste des meilleurs scores.
        :param name: Le nom du joueur.
        """
        
        self.high_score.append((name, self.score))
        self.high_score.sort(key=lambda x: x[1], reverse=True)  # Trie les scores par ordre décroissant
        self.high_score = self.high_score[:10]  # Garde seulement les 10 meilleurs scores
        
    def save_high_scores(self):
        """
        Sauvegarde les meilleurs scores dans un fichier CSV.
        :param score: L'instance de la classe Score pour suivre le score.
        """
        df = pd.DataFrame(self.high_score, columns=["Nom", "Score"])
        df = df[df["Nom"] != ""] # Filtrer les scores vides
        df.to_csv(self.file_path, index=False)
    
    def load_high_scores(self):
        """
        Charge les meilleurs scores depuis un fichier CSV.
        :param score: L'instance de la classe Score pour suivre le score.
        """
        try:
            df = pd.read_csv(self.file_path)
            self.high_score = list(df.itertuples(index=False, name=None))
        except FileNotFoundError:
            self.high_score = [("", 0)] * 10  # Si le fichier n'existe pas, initialise avec des scores vides