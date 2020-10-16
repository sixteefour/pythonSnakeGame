class FAN:
    def cold(self):
        print(" AHHH! That is so cold now!!!!!!!!!!")
    def hot(self):
        print("AHHH! That is so hot now!!!!!!!!!!")


if __name__ == "__main__":
    print("Running the __init__ directly.")
    print("Calling Animals.living")
    f = FAN()
    f.cold()
else:
    print("__init__ is being called by something else!")

f = FAN()
f.cold()