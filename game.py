import tkinter as tk;


def play():

    # create a Window called "root"
    root = tk.Tk();
    root.configure(bg="blue");
    root.title("Chess");
    root.geometry("800x600");

    # organize the difficulty buttons using a frame
    dbframe = tk.Frame(root);  # frame is placed inside window 'root'
    dbframe.pack(side="left", padx=30, pady=0);  # padx and pady are set margins for the frame
    dbframe.configure(bg="black");

    labelFont = ("tkDefaultFont", 18);
    labelBgColor = "blue";
    labelFgColor = "white";

    buttonFont = ("tkDefaultFont", 12);

    placeButton1BgColor = "red";
    placeButton1FgColor = "white";

    placeButton2BgColor = "pink";
    placeButton2FgColor = "white";

    placeButtonText = "      ";


    def placeButtonClicked(letter, number):
        print(letter + ",", number);

    blackBishop1 = tk.PhotoImage(file="blackBishop1.gif")
    blackBishop2 = tk.PhotoImage(file="blackBishop2.gif")
    blackKing = tk.PhotoImage(file="blackKing.gif")
    blackKnight1 = tk.PhotoImage(file="blackKnight1.gif")
    blackKnight2 = tk.PhotoImage(file="blackKnight2.gif")
    blackPawn1 = tk.PhotoImage(file="blackPawn1.gif")
    blackPawn2 = tk.PhotoImage(file="blackPawn2.gif")
    blackPawn3 = tk.PhotoImage(file="blackPawn3.gif")
    blackPawn4 = tk.PhotoImage(file="blackPawn4.gif")
    photo = tk.PhotoImage(file="image.gif")
    photo = tk.PhotoImage(file="image.gif")

    #create column a buttons
    a1 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("a", 1), font=buttonFont, bg=placeButton1BgColor, fg=placeButton1FgColor);
    a2 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("a", 2), font=buttonFont, bg=placeButton2BgColor, fg=placeButton2FgColor);
    a3 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("a", 3), font=buttonFont, bg=placeButton1BgColor, fg=placeButton1FgColor);
    a4 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("a", 4), font=buttonFont, bg=placeButton2BgColor, fg=placeButton2FgColor);
    a5 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("a", 5), font=buttonFont, bg=placeButton1BgColor, fg=placeButton1FgColor);
    a6 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("a", 6), font=buttonFont, bg=placeButton2BgColor, fg=placeButton2FgColor);
    a7 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("a", 7), font=buttonFont, bg=placeButton1BgColor, fg=placeButton1FgColor);
    a8 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("a", 8), font=buttonFont, bg=placeButton2BgColor, fg=placeButton2FgColor);

    # create column b buttons
    b1 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("b", 1), font=buttonFont, bg=placeButton2BgColor, fg=placeButton2FgColor);
    b2 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("b", 2), font=buttonFont, bg=placeButton1BgColor, fg=placeButton1FgColor);
    b3 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("b", 3), font=buttonFont, bg=placeButton2BgColor, fg=placeButton2FgColor);
    b4 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("b", 4), font=buttonFont, bg=placeButton1BgColor, fg=placeButton1FgColor);
    b5 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("b", 5), font=buttonFont, bg=placeButton2BgColor, fg=placeButton2FgColor);
    b6 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("b", 6), font=buttonFont, bg=placeButton1BgColor, fg=placeButton1FgColor);
    b7 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("b", 7), font=buttonFont, bg=placeButton2BgColor, fg=placeButton2FgColor);
    b8 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("b", 8), font=buttonFont, bg=placeButton1BgColor, fg=placeButton1FgColor);

    # create column c buttons
    c1 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("c", 1), font=buttonFont,
                   bg=placeButton1BgColor, fg=placeButton1FgColor);
    c2 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("c", 2), font=buttonFont,
                   bg=placeButton2BgColor, fg=placeButton2FgColor);
    c3 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("c", 3), font=buttonFont,
                   bg=placeButton1BgColor, fg=placeButton1FgColor);
    c4 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("c", 4), font=buttonFont,
                   bg=placeButton2BgColor, fg=placeButton2FgColor);
    c5 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("c", 5), font=buttonFont,
                   bg=placeButton1BgColor, fg=placeButton1FgColor);
    c6 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("c", 6), font=buttonFont,
                   bg=placeButton2BgColor, fg=placeButton2FgColor);
    c7 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("c", 7), font=buttonFont,
                   bg=placeButton1BgColor, fg=placeButton1FgColor);
    c8 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("c", 8), font=buttonFont,
                   bg=placeButton2BgColor, fg=placeButton2FgColor);

    # create column d buttons
    d1 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("d", 1), font=buttonFont,
                   bg=placeButton2BgColor, fg=placeButton2FgColor);
    d2 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("d", 2), font=buttonFont,
                   bg=placeButton1BgColor, fg=placeButton1FgColor);
    d3 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("d", 3), font=buttonFont,
                   bg=placeButton2BgColor, fg=placeButton2FgColor);
    d4 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("d", 4), font=buttonFont,
                   bg=placeButton1BgColor, fg=placeButton1FgColor);
    d5 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("d", 5), font=buttonFont,
                   bg=placeButton2BgColor, fg=placeButton2FgColor);
    d6 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("d", 6), font=buttonFont,
                   bg=placeButton1BgColor, fg=placeButton1FgColor);
    d7 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("d", 7), font=buttonFont,
                   bg=placeButton2BgColor, fg=placeButton2FgColor);
    d8 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("d", 8), font=buttonFont,
                   bg=placeButton1BgColor, fg=placeButton1FgColor);

    # create column e buttons
    e1 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("e", 1), font=buttonFont,
                   bg=placeButton1BgColor, fg=placeButton1FgColor);
    e2 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("e", 2), font=buttonFont,
                   bg=placeButton2BgColor, fg=placeButton2FgColor);
    e3 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("e", 3), font=buttonFont,
                   bg=placeButton1BgColor, fg=placeButton1FgColor);
    e4 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("e", 4), font=buttonFont,
                   bg=placeButton2BgColor, fg=placeButton2FgColor);
    e5 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("e", 5), font=buttonFont,
                   bg=placeButton1BgColor, fg=placeButton1FgColor);
    e6 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("e", 6), font=buttonFont,
                   bg=placeButton2BgColor, fg=placeButton2FgColor);
    e7 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("e", 7), font=buttonFont,
                   bg=placeButton1BgColor, fg=placeButton1FgColor);
    e8 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("e", 8), font=buttonFont,
                   bg=placeButton2BgColor, fg=placeButton2FgColor);

    # create column f buttons
    f1 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("f", 1), font=buttonFont,
                   bg=placeButton2BgColor, fg=placeButton2FgColor);
    f2 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("f", 2), font=buttonFont,
                   bg=placeButton1BgColor, fg=placeButton1FgColor);
    f3 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("f", 3), font=buttonFont,
                   bg=placeButton2BgColor, fg=placeButton2FgColor);
    f4 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("f", 4), font=buttonFont,
                   bg=placeButton1BgColor, fg=placeButton1FgColor);
    f5 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("f", 5), font=buttonFont,
                   bg=placeButton2BgColor, fg=placeButton2FgColor);
    f6 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("f", 6), font=buttonFont,
                   bg=placeButton1BgColor, fg=placeButton1FgColor);
    f7 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("f", 7), font=buttonFont,
                   bg=placeButton2BgColor, fg=placeButton2FgColor);
    f8 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("f", 8), font=buttonFont,
                   bg=placeButton1BgColor, fg=placeButton1FgColor);

    # create column g buttons
    g1 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("g", 1), font=buttonFont,
                   bg=placeButton1BgColor, fg=placeButton1FgColor);
    g2 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("g", 2), font=buttonFont,
                   bg=placeButton2BgColor, fg=placeButton2FgColor);
    g3 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("g", 3), font=buttonFont,
                   bg=placeButton1BgColor, fg=placeButton1FgColor);
    g4 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("g", 4), font=buttonFont,
                   bg=placeButton2BgColor, fg=placeButton2FgColor);
    g5 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("g", 5), font=buttonFont,
                   bg=placeButton1BgColor, fg=placeButton1FgColor);
    g6 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("g", 6), font=buttonFont,
                   bg=placeButton2BgColor, fg=placeButton2FgColor);
    g7 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("g", 7), font=buttonFont,
                   bg=placeButton1BgColor, fg=placeButton1FgColor);
    g8 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("g", 8), font=buttonFont,
                   bg=placeButton2BgColor, fg=placeButton2FgColor);

    # create column h buttons
    h1 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("h", 1), font=buttonFont,
                   bg=placeButton2BgColor, fg=placeButton2FgColor);
    h2 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("h", 2), font=buttonFont,
                   bg=placeButton1BgColor, fg=placeButton1FgColor);
    h3 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("h", 3), font=buttonFont,
                   bg=placeButton2BgColor, fg=placeButton2FgColor);
    h4 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("h", 4), font=buttonFont,
                   bg=placeButton1BgColor, fg=placeButton1FgColor);
    h5 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("h", 5), font=buttonFont,
                   bg=placeButton2BgColor, fg=placeButton2FgColor);
    h6 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("h", 6), font=buttonFont,
                   bg=placeButton1BgColor, fg=placeButton1FgColor);
    h7 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("h", 7), font=buttonFont,
                   bg=placeButton2BgColor, fg=placeButton2FgColor);
    h8 = tk.Button(dbframe, text=placeButtonText, command=placeButtonClicked("h", 8), font=buttonFont,
                   bg=placeButton1BgColor, fg=placeButton1FgColor);

    #place a buttons
    a1.grid(row=8, column=2, padx=5, pady=5);
    a2.grid(row=7, column=2, padx=5, pady=5);
    a3.grid(row=6, column=2, padx=5, pady=5);
    a4.grid(row=5, column=2, padx=5, pady=5);
    a5.grid(row=4, column=2, padx=5, pady=5);
    a6.grid(row=3, column=2, padx=5, pady=5);
    a7.grid(row=2, column=2, padx=5, pady=5);
    a8.grid(row=1, column=2, padx=5, pady=5);

    # place b buttons
    b1.grid(row=8, column=3, padx=5, pady=5);
    b2.grid(row=7, column=3, padx=5, pady=5);
    b3.grid(row=6, column=3, padx=5, pady=5);
    b4.grid(row=5, column=3, padx=5, pady=5);
    b5.grid(row=4, column=3, padx=5, pady=5);
    b6.grid(row=3, column=3, padx=5, pady=5);
    b7.grid(row=2, column=3, padx=5, pady=5);
    b8.grid(row=1, column=3, padx=5, pady=5);

    # place c buttons
    c1.grid(row=8, column=4, padx=5, pady=5)
    c2.grid(row=7, column=4, padx=5, pady=5)
    c3.grid(row=6, column=4, padx=5, pady=5)
    c4.grid(row=5, column=4, padx=5, pady=5)
    c5.grid(row=4, column=4, padx=5, pady=5)
    c6.grid(row=3, column=4, padx=5, pady=5)
    c7.grid(row=2, column=4, padx=5, pady=5)
    c8.grid(row=1, column=4, padx=5, pady=5)

    # place d buttons
    d1.grid(row=8, column=5, padx=5, pady=5);
    d2.grid(row=7, column=5, padx=5, pady=5);
    d3.grid(row=6, column=5, padx=5, pady=5);
    d4.grid(row=5, column=5, padx=5, pady=5);
    d5.grid(row=4, column=5, padx=5, pady=5);
    d6.grid(row=3, column=5, padx=5, pady=5);
    d7.grid(row=2, column=5, padx=5, pady=5);
    d8.grid(row=1, column=5, padx=5, pady=5);

    #place e buttons
    e1.grid(row=8, column=6, padx=5, pady=5);
    e2.grid(row=7, column=6, padx=5, pady=5);
    e3.grid(row=6, column=6, padx=5, pady=5);
    e4.grid(row=5, column=6, padx=5, pady=5);
    e5.grid(row=4, column=6, padx=5, pady=5);
    e6.grid(row=3, column=6, padx=5, pady=5);
    e7.grid(row=2, column=6, padx=5, pady=5);
    e8.grid(row=1, column=6, padx=5, pady=5);

    # place f buttons
    f1.grid(row=8, column=7, padx=5, pady=5);
    f2.grid(row=7, column=7, padx=5, pady=5);
    f3.grid(row=6, column=7, padx=5, pady=5);
    f4.grid(row=5, column=7, padx=5, pady=5);
    f5.grid(row=4, column=7, padx=5, pady=5);
    f6.grid(row=3, column=7, padx=5, pady=5);
    f7.grid(row=2, column=7, padx=5, pady=5);
    f8.grid(row=1, column=7, padx=5, pady=5);

    # place g buttons
    g1.grid(row=8, column=8, padx=5, pady=5)
    g2.grid(row=7, column=8, padx=5, pady=5)
    g3.grid(row=6, column=8, padx=5, pady=5)
    g4.grid(row=5, column=8, padx=5, pady=5)
    g5.grid(row=4, column=8, padx=5, pady=5)
    g6.grid(row=3, column=8, padx=5, pady=5)
    g7.grid(row=2, column=8, padx=5, pady=5)
    g8.grid(row=1, column=8, padx=5, pady=5)

    # place h buttons
    h1.grid(row=8, column=9, padx=5, pady=5);
    h2.grid(row=7, column=9, padx=5, pady=5);
    h3.grid(row=6, column=9, padx=5, pady=5);
    h4.grid(row=5, column=9, padx=5, pady=5);
    h5.grid(row=4, column=9, padx=5, pady=5);
    h6.grid(row=3, column=9, padx=5, pady=5);
    h7.grid(row=2, column=9, padx=5, pady=5);
    h8.grid(row=1, column=9, padx=5, pady=5);




    root.mainloop();



