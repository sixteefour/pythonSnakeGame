class Animals:
    def species(self):
        print("HI, I AM A DINOSAUR")

    def eating(self):
        print("HI, I AM EATING")

    def moving(self):
        print("HI, I AM MOVING")

    def living(self):
        print("HI, I AM LIVING ON PLANET EARTH. WHERE ARE YOU LIVING RIGHT NOW?")

    def dying(self):
        print("HI, I AM DYING BECAUSE A METEOR HIT MY HEAD")


if __name__ == "__main__":
    print("Running the MYCREATION directly.")
    print("Calling Animals.living")
    a = Animals()
    a.living()
else:
    print("MYCREATION is being called by something else!")
