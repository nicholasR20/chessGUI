import tkinter as tk;
import positions



def play():

    # create a Window called "root"
    root = tk.Tk();
    root.configure(bg="blue");
    root.title("Chess");
    root.geometry("800x600");

    # set black piece images
    bBishop1 = tk.PhotoImage(file="blackBishop1.gif");
    bBishop2 = tk.PhotoImage(file="blackBishop2.gif");
    bKing = tk.PhotoImage(file="blackKing.gif");
    bKnight1 = tk.PhotoImage(file="blackKnight1.gif");
    bKnight2 = tk.PhotoImage(file="blackKnight2.gif");
    bPawn1 = tk.PhotoImage(file="blackPawn1.gif");
    bPawn2 = tk.PhotoImage(file="blackPawn2.gif");
    bPawn3 = tk.PhotoImage(file="blackPawn3.gif");
    bPawn4 = tk.PhotoImage(file="blackPawn4.gif");
    bPawn5 = tk.PhotoImage(file="blackPawn5.gif");
    bPawn6 = tk.PhotoImage(file="blackPawn6.gif");
    bPawn7 = tk.PhotoImage(file="blackPawn6.gif");
    bPawn8 = tk.PhotoImage(file="blackPawn6.gif");
    bPromotedPawn1 = tk.PhotoImage(file="blackPromotedPawn1.gif");
    bPromotedPawn2 = tk.PhotoImage(file="blackPromotedPawn2.gif");
    bPromotedPawn3 = tk.PhotoImage(file="blackPromotedPawn3.gif");
    bPromotedPawn4 = tk.PhotoImage(file="blackPromotedPawn4.gif");
    bPromotedPawn5 = tk.PhotoImage(file="blackPromotedPawn5.gif");
    bPromotedPawn6 = tk.PhotoImage(file="blackPromotedPawn6.gif");
    bPromotedPawn7 = tk.PhotoImage(file="blackPromotedPawn7.gif");
    bPromotedPawn8 = tk.PhotoImage(file="blackPromotedPawn8.gif");
    bQueen = tk.PhotoImage(file="blackQueen.gif");
    bRook1 = tk.PhotoImage(file="blackRook1.gif");
    bRook2 = tk.PhotoImage(file="blackRook2.gif");

    # set white piece images
    wBishop1 = tk.PhotoImage(file="whiteBishop1.gif");
    wBishop2 = tk.PhotoImage(file="whiteBishop2.gif");
    wKing = tk.PhotoImage(file="whiteKing.gif");
    wKnight1 = tk.PhotoImage(file="whiteKnight1.gif");
    wKnight2 = tk.PhotoImage(file="whiteKnight2.gif");
    wPawn1 = tk.PhotoImage(file="whitePawn1.gif");
    wPawn2 = tk.PhotoImage(file="whitePawn2.gif");
    wPawn3 = tk.PhotoImage(file="whitePawn3.gif");
    wPawn4 = tk.PhotoImage(file="whitePawn4.gif");
    wPawn5 = tk.PhotoImage(file="whitePawn5.gif");
    wPawn6 = tk.PhotoImage(file="whitePawn6.gif");
    wPawn7 = tk.PhotoImage(file="whitePawn6.gif");
    wPawn8 = tk.PhotoImage(file="whitePawn6.gif");
    wPromotedPawn1 = tk.PhotoImage(file="whitePromotedPawn1.gif");
    wPromotedPawn2 = tk.PhotoImage(file="whitePromotedPawn2.gif");
    wPromotedPawn3 = tk.PhotoImage(file="whitePromotedPawn3.gif");
    wPromotedPawn4 = tk.PhotoImage(file="whitePromotedPawn4.gif");
    wPromotedPawn5 = tk.PhotoImage(file="whitePromotedPawn5.gif");
    wPromotedPawn6 = tk.PhotoImage(file="whitePromotedPawn6.gif");
    wPromotedPawn7 = tk.PhotoImage(file="whitePromotedPawn7.gif");
    wPromotedPawn8 = tk.PhotoImage(file="whitePromotedPawn8.gif");
    wQueen = tk.PhotoImage(file="whiteQueen.gif");
    wRook1 = tk.PhotoImage(file="whiteRook1.gif");
    wRook2 = tk.PhotoImage(file="whiteRook2.gif");

    none = tk.PhotoImage(file="none.gif");

    row8 = [bRook1, bKnight1, bBishop1, bQueen, bKing, bBishop2, bKnight2, bRook2]
    row7 = [bPawn1, bPawn2, bPawn3, bPawn4, bPawn5, bPawn6, bPawn7, bPawn8]
    row6 = [none, none, none, none, none, none, none, none]
    row5 = [none, none, none, none, none, none, none, none]
    row4 = [none, none, none, none, none, none, none, none]
    row3 = [none, none, none, none, none, none, none, none]
    row2 = [wPawn1, wPawn2, wPawn3, wPawn4, wPawn5, wPawn6, wPawn7, wPawn8]
    row1 = [wRook1, wKnight1, wBishop1, wQueen, wKing, wBishop2, wKnight2, wRook2]

    whitePawns = [wPawn1, wPawn2, wPawn3, wPawn4, wPawn5, wPawn6, wPawn7, wPawn8]  # List of white pawns
    whiteNp = [wRook1, wKnight1, wBishop1, wQueen, wKing, wBishop2, wKnight2,
               wRook2]  # List of white non-pawn pieces
    blackPawns = [bPawn1, bPawn2, bPawn3, bPawn4, bPawn5, bPawn6, bPawn7, bPawn8]  # List of black pawns
    blackNp = [bRook1, bKnight1, bBishop1, bQueen, bKing, bBishop2, bKnight2,
               bRook2]  # List of black non-pawns

    places = [row1, row2, row3, row4, row5, row6, row7, row8]

    whitePieces = [whitePawns, whiteNp]  # puts all white pieces in a list
    blackPieces = [blackPawns, blackNp]  # puts all black pieces in a list
    allPieces = [whitePieces, blackPieces]  # Puts all pieces in a list

    def printBoard():
        print("")
        print(row8)
        print(row7)
        print(row6)
        print(row5)
        print(row4)
        print(row3)
        print(row2)
        print(row1)
        print("")

    # organize the difficulty buttons using a frame
    dbframe = tk.Frame(root);  # frame is placed inside window 'root'
    dbframe.pack(side="left", padx=30, pady=0);  # padx and pady are set margins for the frame
    dbframe.configure(bg="black");

    #set label font and colors
    labelFont = ("tkDefaultFont", 18);
    labelBgColor = "blue";
    labelFgColor = "white";

    #set button font and color and text
    buttonFont = ("tkDefaultFont", 12);
    placeButton1BgColor = "red";
    placeButton1FgColor = "white";
    placeButton2BgColor = "pink";
    placeButton2FgColor = "white";
    placeButtonText = "          \n";


    def placeButtonClicked(letter, number): #when a place on the board is clicked
        print(letter + ",", number);


    #set button sizes
    buttonHeight = 10;
    buttonWidth = 10;

    #create column a buttons
    a1 = tk.Button(dbframe, image=row1[0], command=placeButtonClicked("a", 1), font=buttonFont, bg=placeButton1BgColor, fg=placeButton1FgColor);
    a2 = tk.Button(dbframe, image=row2[0], command=placeButtonClicked("a", 2), font=buttonFont, bg=placeButton2BgColor, fg=placeButton2FgColor);
    a3 = tk.Button(dbframe, image=row3[0], command=placeButtonClicked("a", 3), font=buttonFont, bg=placeButton1BgColor, fg=placeButton1FgColor);
    a4 = tk.Button(dbframe, image=row4[0], command=placeButtonClicked("a", 4), font=buttonFont, bg=placeButton2BgColor, fg=placeButton2FgColor);
    a5 = tk.Button(dbframe, image=row5[0], command=placeButtonClicked("a", 5), font=buttonFont, bg=placeButton1BgColor, fg=placeButton1FgColor);
    a6 = tk.Button(dbframe, image=row6[0], command=placeButtonClicked("a", 6), font=buttonFont, bg=placeButton2BgColor, fg=placeButton2FgColor);
    a7 = tk.Button(dbframe, image=row7[0], command=placeButtonClicked("a", 7), font=buttonFont, bg=placeButton1BgColor, fg=placeButton1FgColor);
    a8 = tk.Button(dbframe, image=row8[0], command=placeButtonClicked("a", 8), font=buttonFont, bg=placeButton2BgColor, fg=placeButton2FgColor);

    # create column b buttons
    b1 = tk.Button(dbframe, image=row1[1], command=placeButtonClicked("b", 1), font=buttonFont, bg=placeButton2BgColor, fg=placeButton2FgColor);
    b2 = tk.Button(dbframe, image=row2[1], command=placeButtonClicked("b", 2), font=buttonFont, bg=placeButton1BgColor, fg=placeButton1FgColor);
    b3 = tk.Button(dbframe, image=row3[1], command=placeButtonClicked("b", 3), font=buttonFont, bg=placeButton2BgColor, fg=placeButton2FgColor);
    b4 = tk.Button(dbframe, image=row4[1], command=placeButtonClicked("b", 4), font=buttonFont, bg=placeButton1BgColor, fg=placeButton1FgColor);
    b5 = tk.Button(dbframe, image=row5[1], command=placeButtonClicked("b", 5), font=buttonFont, bg=placeButton2BgColor, fg=placeButton2FgColor);
    b6 = tk.Button(dbframe, image=row6[1], command=placeButtonClicked("b", 6), font=buttonFont, bg=placeButton1BgColor, fg=placeButton1FgColor);
    b7 = tk.Button(dbframe, image=row7[1], command=placeButtonClicked("b", 7), font=buttonFont, bg=placeButton2BgColor, fg=placeButton2FgColor);
    b8 = tk.Button(dbframe, image=row8[1], command=placeButtonClicked("b", 8), font=buttonFont, bg=placeButton1BgColor, fg=placeButton1FgColor);

    # create column c buttons
    c1 = tk.Button(dbframe, image=row1[2], command=placeButtonClicked("c", 1), font=buttonFont,
                   bg=placeButton1BgColor, fg=placeButton1FgColor);
    c2 = tk.Button(dbframe, image=row2[2], command=placeButtonClicked("c", 2), font=buttonFont,
                   bg=placeButton2BgColor, fg=placeButton2FgColor);
    c3 = tk.Button(dbframe, image=row3[2], command=placeButtonClicked("c", 3), font=buttonFont,
                   bg=placeButton1BgColor, fg=placeButton1FgColor);
    c4 = tk.Button(dbframe, image=row4[2], command=placeButtonClicked("c", 4), font=buttonFont,
                   bg=placeButton2BgColor, fg=placeButton2FgColor);
    c5 = tk.Button(dbframe, image=row5[2], command=placeButtonClicked("c", 5), font=buttonFont,
                   bg=placeButton1BgColor, fg=placeButton1FgColor);
    c6 = tk.Button(dbframe, image=row6[2], command=placeButtonClicked("c", 6), font=buttonFont,
                   bg=placeButton2BgColor, fg=placeButton2FgColor);
    c7 = tk.Button(dbframe, image=row7[2], command=placeButtonClicked("c", 7), font=buttonFont,
                   bg=placeButton1BgColor, fg=placeButton1FgColor);
    c8 = tk.Button(dbframe, image=row8[2], command=placeButtonClicked("c", 8), font=buttonFont,
                   bg=placeButton2BgColor, fg=placeButton2FgColor);

    # create column d buttons
    d1 = tk.Button(dbframe, image=row1[3], command=placeButtonClicked("d", 1), font=buttonFont,
                   bg=placeButton2BgColor, fg=placeButton2FgColor);
    d2 = tk.Button(dbframe, image=row2[3], command=placeButtonClicked("d", 2), font=buttonFont,
                   bg=placeButton1BgColor, fg=placeButton1FgColor);
    d3 = tk.Button(dbframe, image=row3[3], command=placeButtonClicked("d", 3), font=buttonFont,
                   bg=placeButton2BgColor, fg=placeButton2FgColor);
    d4 = tk.Button(dbframe, image=row4[3], command=placeButtonClicked("d", 4), font=buttonFont,
                   bg=placeButton1BgColor, fg=placeButton1FgColor);
    d5 = tk.Button(dbframe, image=row5[3], command=placeButtonClicked("d", 5), font=buttonFont,
                   bg=placeButton2BgColor, fg=placeButton2FgColor);
    d6 = tk.Button(dbframe, image=row6[3], command=placeButtonClicked("d", 6), font=buttonFont,
                   bg=placeButton1BgColor, fg=placeButton1FgColor);
    d7 = tk.Button(dbframe, image=row7[3], command=placeButtonClicked("d", 7), font=buttonFont,
                   bg=placeButton2BgColor, fg=placeButton2FgColor);
    d8 = tk.Button(dbframe, image=row8[3], command=placeButtonClicked("d", 8), font=buttonFont,
                   bg=placeButton1BgColor, fg=placeButton1FgColor);

    # create column e buttons
    e1 = tk.Button(dbframe, image=row1[4], command=placeButtonClicked("e", 1), font=buttonFont,
                   bg=placeButton1BgColor, fg=placeButton1FgColor);
    e2 = tk.Button(dbframe, image=row2[4], command=placeButtonClicked("e", 2), font=buttonFont,
                   bg=placeButton2BgColor, fg=placeButton2FgColor);
    e3 = tk.Button(dbframe, image=row3[4], command=placeButtonClicked("e", 3), font=buttonFont,
                   bg=placeButton1BgColor, fg=placeButton1FgColor);
    e4 = tk.Button(dbframe, image=row4[4], command=placeButtonClicked("e", 4), font=buttonFont,
                   bg=placeButton2BgColor, fg=placeButton2FgColor);
    e5 = tk.Button(dbframe, image=row5[4], command=placeButtonClicked("e", 5), font=buttonFont,
                   bg=placeButton1BgColor, fg=placeButton1FgColor);
    e6 = tk.Button(dbframe, image=row6[4], command=placeButtonClicked("e", 6), font=buttonFont,
                   bg=placeButton2BgColor, fg=placeButton2FgColor);
    e7 = tk.Button(dbframe, image=row7[4], command=placeButtonClicked("e", 7), font=buttonFont,
                   bg=placeButton1BgColor, fg=placeButton1FgColor);
    e8 = tk.Button(dbframe, image=row8[4], command=placeButtonClicked("e", 8), font=buttonFont,
                   bg=placeButton2BgColor, fg=placeButton2FgColor);

    # create column f buttons
    f1 = tk.Button(dbframe, image=row1[5], command=placeButtonClicked("f", 1), font=buttonFont,
                   bg=placeButton2BgColor, fg=placeButton2FgColor);
    f2 = tk.Button(dbframe, image=row2[5], command=placeButtonClicked("f", 2), font=buttonFont,
                   bg=placeButton1BgColor, fg=placeButton1FgColor);
    f3 = tk.Button(dbframe, image=row3[5], command=placeButtonClicked("f", 3), font=buttonFont,
                   bg=placeButton2BgColor, fg=placeButton2FgColor);
    f4 = tk.Button(dbframe, image=row4[5], command=placeButtonClicked("f", 4), font=buttonFont,
                   bg=placeButton1BgColor, fg=placeButton1FgColor);
    f5 = tk.Button(dbframe, image=row5[5], command=placeButtonClicked("f", 5), font=buttonFont,
                   bg=placeButton2BgColor, fg=placeButton2FgColor);
    f6 = tk.Button(dbframe, image=row6[5], command=placeButtonClicked("f", 6), font=buttonFont,
                   bg=placeButton1BgColor, fg=placeButton1FgColor);
    f7 = tk.Button(dbframe, image=row7[5], command=placeButtonClicked("f", 7), font=buttonFont,
                   bg=placeButton2BgColor, fg=placeButton2FgColor);
    f8 = tk.Button(dbframe, image=row8[5], command=placeButtonClicked("f", 8), font=buttonFont,
                   bg=placeButton1BgColor, fg=placeButton1FgColor);

    # create column g buttons
    g1 = tk.Button(dbframe, image=row1[6], command=placeButtonClicked("g", 1), font=buttonFont,
                   bg=placeButton1BgColor, fg=placeButton1FgColor);
    g2 = tk.Button(dbframe, image=row2[6], command=placeButtonClicked("g", 2), font=buttonFont,
                   bg=placeButton2BgColor, fg=placeButton2FgColor);
    g3 = tk.Button(dbframe, image=row3[6], command=placeButtonClicked("g", 3), font=buttonFont,
                   bg=placeButton1BgColor, fg=placeButton1FgColor);
    g4 = tk.Button(dbframe, image=row4[6], command=placeButtonClicked("g", 4), font=buttonFont,
                   bg=placeButton2BgColor, fg=placeButton2FgColor);
    g5 = tk.Button(dbframe, image=row5[6], command=placeButtonClicked("g", 5), font=buttonFont,
                   bg=placeButton1BgColor, fg=placeButton1FgColor);
    g6 = tk.Button(dbframe, image=row6[6], command=placeButtonClicked("g", 6), font=buttonFont,
                   bg=placeButton2BgColor, fg=placeButton2FgColor);
    g7 = tk.Button(dbframe, image=row7[6], command=placeButtonClicked("g", 7), font=buttonFont,
                   bg=placeButton1BgColor, fg=placeButton1FgColor);
    g8 = tk.Button(dbframe, image=row8[6], command=placeButtonClicked("g", 8), font=buttonFont,
                   bg=placeButton2BgColor, fg=placeButton2FgColor);

    # create column h buttons
    h1 = tk.Button(dbframe, image=row1[7], command=placeButtonClicked("h", 1), font=buttonFont,
                   bg=placeButton2BgColor, fg=placeButton2FgColor);
    h2 = tk.Button(dbframe, image=row2[7], command=placeButtonClicked("h", 2), font=buttonFont,
                   bg=placeButton1BgColor, fg=placeButton1FgColor);
    h3 = tk.Button(dbframe, image=row3[7], command=placeButtonClicked("h", 3), font=buttonFont,
                   bg=placeButton2BgColor, fg=placeButton2FgColor);
    h4 = tk.Button(dbframe, image=row4[7], command=placeButtonClicked("h", 4), font=buttonFont,
                   bg=placeButton1BgColor, fg=placeButton1FgColor);
    h5 = tk.Button(dbframe, image=row5[7], command=placeButtonClicked("h", 5), font=buttonFont,
                   bg=placeButton2BgColor, fg=placeButton2FgColor);
    h6 = tk.Button(dbframe, image=row6[7], command=placeButtonClicked("h", 6), font=buttonFont,
                   bg=placeButton1BgColor, fg=placeButton1FgColor);
    h7 = tk.Button(dbframe, image=row7[7], command=placeButtonClicked("h", 7), font=buttonFont,
                   bg=placeButton2BgColor, fg=placeButton2FgColor);
    h8 = tk.Button(dbframe, image=row8[7], command=placeButtonClicked("h", 8), font=buttonFont,
                   bg=placeButton1BgColor, fg=placeButton1FgColor);

    #place a buttons
    a1.grid(row=8, column=2, padx=1, pady=1);
    a2.grid(row=7, column=2, padx=1, pady=1);
    a3.grid(row=6, column=2, padx=1, pady=1);
    a4.grid(row=5, column=2, padx=1, pady=1);
    a5.grid(row=4, column=2, padx=1, pady=1);
    a6.grid(row=3, column=2, padx=1, pady=1);
    a7.grid(row=2, column=2, padx=1, pady=1);
    a8.grid(row=1, column=2, padx=1, pady=1);

    # place b buttons
    b1.grid(row=8, column=3, padx=1, pady=1);
    b2.grid(row=7, column=3, padx=1, pady=1);
    b3.grid(row=6, column=3, padx=1, pady=1);
    b4.grid(row=5, column=3, padx=1, pady=1);
    b5.grid(row=4, column=3, padx=1, pady=1);
    b6.grid(row=3, column=3, padx=1, pady=1);
    b7.grid(row=2, column=3, padx=1, pady=1);
    b8.grid(row=1, column=3, padx=1, pady=1);

    # place c buttons
    c1.grid(row=8, column=4, padx=1, pady=1);
    c2.grid(row=7, column=4, padx=1, pady=1);
    c3.grid(row=6, column=4, padx=1, pady=1);
    c4.grid(row=5, column=4, padx=1, pady=1);
    c5.grid(row=4, column=4, padx=1, pady=1);
    c6.grid(row=3, column=4, padx=1, pady=1);
    c7.grid(row=2, column=4, padx=1, pady=1);
    c8.grid(row=1, column=4, padx=1, pady=1);

    # place d buttons
    d1.grid(row=8, column=5, padx=1, pady=1);
    d2.grid(row=7, column=5, padx=1, pady=1);
    d3.grid(row=6, column=5, padx=1, pady=1);
    d4.grid(row=5, column=5, padx=1, pady=1);
    d5.grid(row=4, column=5, padx=1, pady=1);
    d6.grid(row=3, column=5, padx=1, pady=1);
    d7.grid(row=2, column=5, padx=1, pady=1);
    d8.grid(row=1, column=5, padx=1, pady=1);

    #place e buttons
    e1.grid(row=8, column=6, padx=1, pady=1);
    e2.grid(row=7, column=6, padx=1, pady=1);
    e3.grid(row=6, column=6, padx=1, pady=1);
    e4.grid(row=5, column=6, padx=1, pady=1);
    e5.grid(row=4, column=6, padx=1, pady=1);
    e6.grid(row=3, column=6, padx=1, pady=1);
    e7.grid(row=2, column=6, padx=1, pady=1);
    e8.grid(row=1, column=6, padx=1, pady=1);

    # place f buttons
    f1.grid(row=8, column=7, padx=1, pady=1);
    f2.grid(row=7, column=7, padx=1, pady=1);
    f3.grid(row=6, column=7, padx=1, pady=1);
    f4.grid(row=5, column=7, padx=1, pady=1);
    f5.grid(row=4, column=7, padx=1, pady=1);
    f6.grid(row=3, column=7, padx=1, pady=1);
    f7.grid(row=2, column=7, padx=1, pady=1);
    f8.grid(row=1, column=7, padx=1, pady=1);

    # place g buttons
    g1.grid(row=8, column=8, padx=1, pady=1);
    g2.grid(row=7, column=8, padx=1, pady=1);
    g3.grid(row=6, column=8, padx=1, pady=1);
    g4.grid(row=5, column=8, padx=1, pady=1);
    g5.grid(row=4, column=8, padx=1, pady=1);
    g6.grid(row=3, column=8, padx=1, pady=1);
    g7.grid(row=2, column=8, padx=1, pady=1);
    g8.grid(row=1, column=8, padx=1, pady=1);

    # place h buttons
    h1.grid(row=8, column=9, padx=1, pady=1);
    h2.grid(row=7, column=9, padx=1, pady=1);
    h3.grid(row=6, column=9, padx=1, pady=1);
    h4.grid(row=5, column=9, padx=1, pady=1);
    h5.grid(row=4, column=9, padx=1, pady=1);
    h6.grid(row=3, column=9, padx=1, pady=1);
    h7.grid(row=2, column=9, padx=1, pady=1);
    h8.grid(row=1, column=9, padx=1, pady=1);




    root.mainloop();



