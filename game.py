import tkinter as tk;


def play():

    # create a Window called "root"
    root = tk.Tk();
    root.configure(bg="blue");
    root.title("Chess");
    root.geometry("400x300");

    # organize the difficulty buttons using a frame
    dbframe = tk.Frame(root);  # frame is placed inside window 'root'
    dbframe.pack(side="left", padx=30, pady=10);  # padx and pady are set margins for the frame
    dbframe.configure(bg="black");

    labelFont = ("tkDefaultFont", 18);
    labelBgColor = "blue";
    labelFgColor = "white";

    buttonFont = ("tkDefaultFont", 12);
    frameBgColor = "red";
    frameFgColor = "white";

    placeButtonText = "      ";


    def placeButtonClicked(letter, number):
        print(letter + ",", number);

    #create column a buttons
    a1 = tk.Button(dbframe, text="      ", command=placeButtonClicked("a", 1), font=buttonFont, bg=frameBgColor, fg=frameFgColor);
    a2 = tk.Button(dbframe, text="      ", command=placeButtonClicked("a", 2), font=buttonFont, bg=frameBgColor, fg=frameFgColor);
    a3 = tk.Button(dbframe, text="      ", command=placeButtonClicked("a", 3), font=buttonFont, bg=frameBgColor, fg=frameFgColor);
    a4 = tk.Button(dbframe, text="      ", command=placeButtonClicked("a", 4), font=buttonFont, bg=frameBgColor, fg=frameFgColor);
    a5 = tk.Button(dbframe, text="      ", command=placeButtonClicked("a", 5), font=buttonFont, bg=frameBgColor, fg=frameFgColor);
    a6 = tk.Button(dbframe, text="      ", command=placeButtonClicked("a", 6), font=buttonFont, bg=frameBgColor, fg=frameFgColor);
    a7 = tk.Button(dbframe, text="      ", command=placeButtonClicked("a", 7), font=buttonFont, bg=frameBgColor, fg=frameFgColor);
    a8 = tk.Button(dbframe, text="      ", command=placeButtonClicked("a", 8), font=buttonFont, bg=frameBgColor, fg=frameFgColor);

    a1.place(x=10, y=250);
    a1.place(x=10, y=250);
    a1.place(x=10, y=250);


    root.mainloop();



