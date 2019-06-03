class App:
  def __init__(self, to_do_list):
    self.to_do_list = to_do_list
    
  def start(self):
    while True:
      answer = input("Voulez-vous ajouter un item? --> Ecrivez OUI ou NON: ")
      answer = answer.upper()

      if answer == "OUI":
        a = input("Que voulez-vous rajouter d'autre ?")
        self.to_do_list.insert(-1,a)
        print("Voici votre to-do list maj:")
        [print(i) for i in self.to_do_list] 
   
      elif answer == "NON":
        print("Vous avez terminé votre to-do list")
        print("Voici votre to-do list:")
        [print(i) for i in self.to_do_list] 
        break

      else:
        print("Ceci n'est pas une réponse par OUI ou par NON")

app = App(["manger", "boire", "dormir"])

app.start()

