from customtkinter import CTk, CTkButton, CTkFrame, CTkLabel,X 
from tkinter import messagebox

class TicTacToy:
    winList = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]

    def __init__(self, winName: str = "Game") -> None:
        self.Ascore = 0
        self.Bscrose = 0
        self.win = CTk()
        self.win.title(winName)
        self.win.geometry("1000x600+200+200")
        # Name------------------------
        self.name = CTkLabel(self.win, text="-----Tic Tac Toe-----", font=("Arial", 60))
        self.name.pack(pady=(10, 2))
        self.user = "A"
        self.trunFrame = CTkFrame(self.win)
        self.userTrun = CTkLabel(
            self.trunFrame, text=f"Player {self.user} Turn---", font=("Arial", 30)
        )
        self.userTrun.pack(side="left", padx=5, pady=5)
        self.trunFrame.pack(padx=200, fill=X)
        # Main Frame With All Button--
        self.mainFrame = CTkFrame(self.win)

        # Button -  ---  - - - -  - - - -
        self.b0 = CTkButton(
            self.mainFrame,
            width=200,
            height=100,
            text="",
            command=lambda: self.playBord(0),
        )
        self.b1 = CTkButton(
            self.mainFrame,
            width=200,
            height=100,
            text="",
            command=lambda: self.playBord(1),
        )
        self.b2 = CTkButton(
            self.mainFrame,
            width=200,
            height=100,
            text="",
            command=lambda: self.playBord(2),
        )
        self.b3 = CTkButton(
            self.mainFrame,
            width=200,
            height=100,
            text="",
            command=lambda: self.playBord(3),
        )
        self.b4 = CTkButton(
            self.mainFrame,
            width=200,
            height=100,
            text="",
            command=lambda: self.playBord(4),
        )
        self.b5 = CTkButton(
            self.mainFrame,
            width=200,
            height=100,
            text="",
            command=lambda: self.playBord(5),
        )
        self.b6 = CTkButton(
            self.mainFrame,
            width=200,
            height=100,
            text="",
            command=lambda: self.playBord(6),
        )
        self.b7 = CTkButton(
            self.mainFrame,
            width=200,
            height=100,
            text="",
            command=lambda: self.playBord(7),
        )
        self.b8 = CTkButton(
            self.mainFrame,
            width=200,
            height=100,
            text="",
            command=lambda: self.playBord(8),
        )

        # Pack Button----------------
        self.b0.grid(row=0, column=0, padx=10, pady=10)
        self.b1.grid(row=0, column=1, padx=10, pady=10)
        self.b2.grid(row=0, column=2, padx=10, pady=10)

        self.b3.grid(row=1, column=0, padx=10, pady=10)
        self.b4.grid(row=1, column=1, padx=10, pady=10)
        self.b5.grid(row=1, column=2, padx=10, pady=10)

        self.b6.grid(row=2, column=0, padx=10, pady=10)
        self.b7.grid(row=2, column=1, padx=10, pady=10)
        self.b8.grid(row=2, column=2, padx=10, pady=10)

        self.mainFrame.pack(pady=(10, 30))

        # Score Frame-------------------------------------------
        self.ScoreFrame = CTkFrame(self.win, bg_color="transparent")
        self.scroeLabel = CTkLabel(
            self.ScoreFrame,
            text=f"Player A:- {self.Ascore}    Player B:- {self.Bscrose}",
            font=("Arial", 30),
        )
        self.scroeLabel.grid(row=0, column=0, padx=10, pady=10)
        self.reStartButton = CTkButton(
            self.ScoreFrame,
            text="Restart",
            command=self.reStart,
            width=200,
            height=40,
            font=("Arial", 23),
            state="disabled",
        )
        self.reStartButton.grid(row=0, column=1, padx=(40, 10))
        self.ScoreFrame.pack(padx=180)

        self.buttonCheckList = [True, True, True, True, True, True, True, True, True]
        self.Alist = [True, True, True, True, True, True, True, True, True]
        self.Blist = [True, True, True, True, True, True, True, True, True]
        self.win.mainloop()

    def playBord(self, button: int):
        self.buttonMatch = {
            0: self.b0,
            1: self.b1,
            2: self.b2,
            3: self.b3,
            4: self.b4,
            5: self.b5,
            6: self.b6,
            7: self.b7,
            8: self.b8,
        }
        if self.buttonCheckList[button]:
            if self.user == "A":
                self.buttonMatch.get(button).configure(text="X", font=("Arial", 40))
                self.Alist[button] = False
                self.user = "B"
            else:
                self.buttonMatch.get(button).configure(text="O", font=("Arial", 40))
                self.Blist[button] = False
                self.user = "A"
            self.buttonCheckList[button] = False
            self.userTrun.configure(text=f"Player {self.user} Turn---")
            self.checkWin()
        else:
            print("Not Allow To Press")
            print(self.Alist)
            print(self.Blist)

    def checkWin(self):
        for win in self.winList: 
            if (self.Alist[win[0]] + self.Alist[win[1]] + self.Alist[win[2]]) == 0:
                # messagebox.showinfo('Game',"A Wins The Game.")
                self.Ascore += 1
                self.userTrun.configure(text="Player A won the match.")
                self.changeColor(win)
                return 1
            elif (self.Blist[win[0]] + self.Blist[win[1]] + self.Blist[win[2]]) == 0:
                # messagebox.showinfo('Game',"B Wins The Game.")
                self.Bscrose += 1
                self.userTrun.configure(text="Player B won the match.")
                self.changeColor(win)
                return -1
        if   sum(self.buttonCheckList) == 0:
            # messagebox.showinfo('Game',"Match tie")
            self.userTrun.configure(text="The match is tie.")
            self.changeColor([0, 1, 2, 3, 4, 5, 6, 7, 8])
            return 2
        return 0

    def reStart(self):
        for i in range(9):
            self.buttonMatch.get(i).configure(
                text="", state="enabled", fg_color="#1f6aa5"
            )
        self.buttonCheckList = [True, True, True, True, True, True, True, True, True]
        self.Alist = [True, True, True, True, True, True, True, True, True]
        self.Blist = [True, True, True, True, True, True, True, True, True]
        self.reStartButton.configure(state="disabled")
        self.user="A"
        self.userTrun.configure(text=f"Player {self.user} Turn---")

    def changeColor(self, bList):
        for i in bList:
            self.buttonMatch.get(i).configure(fg_color="green")
        for i in range(9):
            self.buttonMatch.get(i).configure(state="disabled")
        self.scroeLabel.configure(
            text=f"Player A:- {self.Ascore}    Player B:- {self.Bscrose}"
        )
        self.reStartButton.configure(state="enabled")


a = TicTacToy()
