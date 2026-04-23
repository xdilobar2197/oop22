# oop22

class light:
    def __init__(self, state):
        self.state = state

    def statust(self):
        if self.state == None:
            print(False)
        else:
            print(True)


res = light(0)
res.statust()
