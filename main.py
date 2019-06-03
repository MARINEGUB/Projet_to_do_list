class App:
  def __init__(self, to_do_list):
    self.to_do_list = to_do_list
    self.running = False

  def start(self):
    self.running = True
    while self.running:
      answer = input("Voulez-vous ajouter un item? --> Ecrivez OUI ou NON: ")
      answer = answer.upper()

      if answer == "OUI":
        a = input("Que voulez-vous rajouter d'autre ?")
        self.to_do_list.insert(-1,a)
        print("Voici votre to-do list maj:")
        self.print()
   
      elif answer == "NON":
        answer = input("Voulez-vous supprimer un item? --> Ecrivez OUI ou NON: ")
        answer = answer.upper()
        if answer == "OUI":
          a = input ("Quel item voulez-vous supprimer ?")
          self.to_do_list.remove(a)
          print("Voici votre to-do list maj:")
          self.print()
        elif answer == "NON":
          print("Vous avez terminé votre to-do list")
          print("Voici votre to-do list:")
          self.print()
          self.running = False
        else:
          print("Ceci n'est pas une réponse par OUI ou par NON") 

      else:
        print("Ceci n'est pas une réponse par OUI ou par NON")

  def print(self):
    [print(i) for i in self.to_do_list] 


app = App(["manger", "boire", "dormir"])

app.start()

