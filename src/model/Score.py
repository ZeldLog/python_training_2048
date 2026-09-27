class Score:
    def __init__(self):
        self.score = 0
        self.high_score = [("", 0)] * 10  # Liste des 10 meilleurs scores
        self.file_path = "high_scores.txt"
        self.player_name = ""
        
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
    
    def insert_high_score(self):
        """
        Insère un nouveau score dans la liste des meilleurs scores.
        """
        if self.player_name == "":
            self.player_name = input("Entrez votre nom : ")
        else:
            new_player = input("Nouveau joueur ? (o/n) ")
            if new_player.lower() == 'o':
                self.player_name = input("Entrez votre nom : ")
        self.high_score.append((self.player_name, self.score))
        self.high_score.sort(key=lambda x: x[1], reverse=True)  # Trie les scores par ordre décroissant
        self.high_score = self.high_score[:10]  # Garde seulement les 10 meilleurs scores