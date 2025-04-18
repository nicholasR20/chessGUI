import tkinter as tk;
import positions;
pieceSelected=False;


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

    #set the image for an empty space
    none = tk.PhotoImage(file="none.gif");
    
    #set the piece names in each row
    row8 = [bRook1, bKnight1, bBishop1, bQueen, bKing, bBishop2, bKnight2, bRook2];
    row7 = [bPawn1, bPawn2, bPawn3, bPawn4, bPawn5, bPawn6, bPawn7, bPawn8];
    row6 = [none, none, none, none, none, none, none, none];
    row5 = [none, none, none, none, none, none, none, none];
    row4 = [none, none, none, none, none, none, none, none];
    row3 = [none, none, none, none, none, none, none, none];
    row2 = [wPawn1, wPawn2, wPawn3, wPawn4, wPawn5, wPawn6, wPawn7, wPawn8];
    row1 = [wRook1, wKnight1, wBishop1, wQueen, wKing, wBishop2, wKnight2, wRook2];

    #list of pieces by color and catagory
    whitePawns = [wPawn1, wPawn2, wPawn3, wPawn4, wPawn5, wPawn6, wPawn7, wPawn8];  # List of white pawns
    whiteNp = [wRook1, wKnight1, wBishop1, wQueen, wKing, wBishop2, wKnight2,
               wRook2];  # List of white non-pawn pieces
    blackPawns = [bPawn1, bPawn2, bPawn3, bPawn4, bPawn5, bPawn6, bPawn7, bPawn8];  # List of black pawns
    blackNp = [bRook1, bKnight1, bBishop1, bQueen, bKing, bBishop2, bKnight2,
               bRook2];  # List of black non-pawns
    

    letters = ["a", "b", "c", "d", "e", "f", "g", "h"]; #list of letters used a board coordinates
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]; #list of numbers used as board coordinates
    # dead = [none, none, none, none]; #

    #lists of queens that can be used to promote a pawn
    promoteWhite = [wPromotedPawn1, wPromotedPawn2, wPromotedPawn3, wPromotedPawn4, wPromotedPawn5, wPromotedPawn6, wPromotedPawn7, wPromotedPawn8];
    promoteBlack = [bPromotedPawn1, bPromotedPawn2, bPromotedPawn3, bPromotedPawn4, bPromotedPawn5, bPromotedPawn6, bPromotedPawn7, bPromotedPawn8]

    #a big list of all the pieces on the board
    places = [row1, row2, row3, row4, row5, row6, row7, row8];


    whitePieces = [whitePawns, whiteNp];  # puts all white pieces in a list
    blackPieces = [blackPawns, blackNp];  # puts all black pieces in a list
    allPieces = [whitePieces, blackPieces];  # Puts all pieces in a list


    def printBoard(): #function to test the places of the board
        print(""); 
        print(row8);
        print(row7);
        print(row6);
        print(row5);
        print(row4);
        print(row3);
        print(row2);
        print(row1);
        print("");

    dbframe = tk.Frame(root);  # frame is placed inside window 'root'
    dbframe.pack(side="left", padx=30, pady=0);  # padx and pady are set margins for the frame
    dbframe.configure(bg="black");

    dbframe1 = tk.Frame(root);  # frame is placed inside window 'root'
    dbframe1.pack(side="right", padx=30, pady=0);  # padx and pady are set margins for the frame
    dbframe1.configure(bg="black");

    insideFrame = tk.Frame(dbframe1);  # frame is placed inside window 'root'
    insideFrame.pack(side="top", padx=0, pady=0);  # padx and pady are set margins for the frame
    insideFrame.configure(bg="black");

    insideFrame1 = tk.Frame(dbframe1);  # frame is placed inside window 'root'
    insideFrame1.pack(side="top", padx=0, pady=0);  # padx and pady are set margins for the frame
    insideFrame1.configure(bg="black");

    insideFrame2 = tk.Frame(dbframe1);  # frame is placed inside window 'root'
    insideFrame2.pack(side="top", padx=0, pady=0);  # padx and pady are set margins for the frame
    insideFrame2.configure(bg="black");

    insideFrame3 = tk.Frame(dbframe1);  # frame is placed inside window 'root'
    insideFrame3.pack(side="top", padx=0, pady=0);  # padx and pady are set margins for the frame
    insideFrame3.configure(bg="black");


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
    placeButton3BgColor = "black";
    placeButton3FgColor = "white";

    def updateSidePanel(): #updates the buttons on the side panel
        text1 = tk.Button(insideFrame, text="Promote A Pawn:", font=("tkDefaultFont", 18), bg=placeButton3BgColor, fg=placeButton3FgColor);
        text1.grid(row=1, column=1, padx=1, pady=1);
        promoteWhiteButton = tk.Button(insideFrame1, image=promoteWhite[0], command=lambda: promoteButtonClicked(promoteWhite[0], "White"), font=buttonFont, bg=placeButton1BgColor, fg=placeButton1FgColor);
        promoteWhiteButton.grid(row=1, column=1, padx=1, pady=1);
        promotBlackButton = tk.Button(insideFrame1, image=promoteBlack[0], command=lambda: promoteButtonClicked(promoteBlack[0], "Black"), font=buttonFont, bg=placeButton1BgColor, fg=placeButton1FgColor);
        promotBlackButton.grid(row=1, column=2, padx=1, pady=1);
    

        # text1 = tk.Button(insideFrame2, text="Undo A Move:", font=("tkDefaultFont", 18), bg=placeButton3BgColor, fg=placeButton3FgColor);
        # text1.grid(row=1, column=1, padx=1, pady=1);
        # undo1 = tk.Button(insideFrame3, image=dead[0], command=lambda: undoButtonClicked(dead[0]), font=buttonFont, bg=placeButton1BgColor, fg=placeButton1FgColor);
        # undo1.grid(row=1, column=1, padx=1, pady=1);
        # undo2 = tk.Button(insideFrame3, image=dead[1], font=buttonFont, bg=placeButton1BgColor, fg=placeButton1FgColor);
        # undo2.grid(row=1, column=2, padx=1, pady=1);
        # undo3 = tk.Button(insideFrame3, image=dead[2], font=buttonFont, bg=placeButton1BgColor, fg=placeButton1FgColor);
        # undo3.grid(row=1, column=3, padx=1, pady=1);

    
    updateSidePanel();



    def updateButtons(): #updates the board
        #create column a buttons
        a1 = tk.Button(dbframe, image=row1[0], command=lambda: placeButtonClicked("a", 1, row1[0]), font=buttonFont, bg=placeButton1BgColor, fg=placeButton1FgColor);
        a2 = tk.Button(dbframe, image=row2[0], command=lambda: placeButtonClicked("a", 2, row2[0]), font=buttonFont, bg=placeButton2BgColor, fg=placeButton2FgColor);
        a3 = tk.Button(dbframe, image=row3[0], command=lambda: placeButtonClicked("a", 3, row3[0]), font=buttonFont, bg=placeButton1BgColor, fg=placeButton1FgColor);
        a4 = tk.Button(dbframe, image=row4[0], command=lambda: placeButtonClicked("a", 4, row4[0]), font=buttonFont, bg=placeButton2BgColor, fg=placeButton2FgColor);
        a5 = tk.Button(dbframe, image=row5[0], command=lambda: placeButtonClicked("a", 5, row5[0]), font=buttonFont, bg=placeButton1BgColor, fg=placeButton1FgColor);
        a6 = tk.Button(dbframe, image=row6[0], command=lambda: placeButtonClicked("a", 6, row6[0]), font=buttonFont, bg=placeButton2BgColor, fg=placeButton2FgColor);
        a7 = tk.Button(dbframe, image=row7[0], command=lambda: placeButtonClicked("a", 7, row7[0]), font=buttonFont, bg=placeButton1BgColor, fg=placeButton1FgColor);
        a8 = tk.Button(dbframe, image=row8[0], command=lambda: placeButtonClicked("a", 8, row8[0]), font=buttonFont, bg=placeButton2BgColor, fg=placeButton2FgColor);

        # create column b buttons
        b1 = tk.Button(dbframe, image=row1[1], command=lambda: placeButtonClicked("b", 1, row1[1]), font=buttonFont, bg=placeButton2BgColor, fg=placeButton2FgColor);
        b2 = tk.Button(dbframe, image=row2[1], command=lambda: placeButtonClicked("b", 2, row2[1]), font=buttonFont, bg=placeButton1BgColor, fg=placeButton1FgColor);
        b3 = tk.Button(dbframe, image=row3[1], command=lambda: placeButtonClicked("b", 3, row3[1]), font=buttonFont, bg=placeButton2BgColor, fg=placeButton2FgColor);
        b4 = tk.Button(dbframe, image=row4[1], command=lambda: placeButtonClicked("b", 4, row4[1]), font=buttonFont, bg=placeButton1BgColor, fg=placeButton1FgColor);
        b5 = tk.Button(dbframe, image=row5[1], command=lambda: placeButtonClicked("b", 5, row5[1]), font=buttonFont, bg=placeButton2BgColor, fg=placeButton2FgColor);
        b6 = tk.Button(dbframe, image=row6[1], command=lambda: placeButtonClicked("b", 6, row6[1]), font=buttonFont, bg=placeButton1BgColor, fg=placeButton1FgColor);
        b7 = tk.Button(dbframe, image=row7[1], command=lambda: placeButtonClicked("b", 7, row7[1]), font=buttonFont, bg=placeButton2BgColor, fg=placeButton2FgColor);
        b8 = tk.Button(dbframe, image=row8[1], command=lambda: placeButtonClicked("b", 8, row8[1]), font=buttonFont, bg=placeButton1BgColor, fg=placeButton1FgColor);

        # create column c buttons
        c1 = tk.Button(dbframe, image=row1[2], command=lambda: placeButtonClicked("c", 1, row1[2]), font=buttonFont,
                    bg=placeButton1BgColor, fg=placeButton1FgColor);
        c2 = tk.Button(dbframe, image=row2[2], command=lambda: placeButtonClicked("c", 2, row2[2]), font=buttonFont,
                    bg=placeButton2BgColor, fg=placeButton2FgColor);
        c3 = tk.Button(dbframe, image=row3[2], command=lambda: placeButtonClicked("c", 3, row3[2]), font=buttonFont,
                    bg=placeButton1BgColor, fg=placeButton1FgColor);
        c4 = tk.Button(dbframe, image=row4[2], command=lambda: placeButtonClicked("c", 4, row4[2]), font=buttonFont,
                    bg=placeButton2BgColor, fg=placeButton2FgColor);
        c5 = tk.Button(dbframe, image=row5[2], command=lambda: placeButtonClicked("c", 5, row5[2]), font=buttonFont,
                    bg=placeButton1BgColor, fg=placeButton1FgColor);
        c6 = tk.Button(dbframe, image=row6[2], command=lambda: placeButtonClicked("c", 6, row6[2]), font=buttonFont,
                    bg=placeButton2BgColor, fg=placeButton2FgColor);
        c7 = tk.Button(dbframe, image=row7[2], command=lambda: placeButtonClicked("c", 7, row7[2]), font=buttonFont,
                    bg=placeButton1BgColor, fg=placeButton1FgColor);
        c8 = tk.Button(dbframe, image=row8[2], command=lambda: placeButtonClicked("c", 8, row8[2]), font=buttonFont,
                    bg=placeButton2BgColor, fg=placeButton2FgColor);

        # create column d buttons
        d1 = tk.Button(dbframe, image=row1[3], command=lambda: placeButtonClicked("d", 1, row1[3]), font=buttonFont,
                    bg=placeButton2BgColor, fg=placeButton2FgColor);
        d2 = tk.Button(dbframe, image=row2[3], command=lambda: placeButtonClicked("d", 2, row2[3]), font=buttonFont,
                    bg=placeButton1BgColor, fg=placeButton1FgColor);
        d3 = tk.Button(dbframe, image=row3[3], command=lambda: placeButtonClicked("d", 3, row3[3]), font=buttonFont,
                    bg=placeButton2BgColor, fg=placeButton2FgColor);
        d4 = tk.Button(dbframe, image=row4[3], command=lambda: placeButtonClicked("d", 4, row4[3]), font=buttonFont,
                    bg=placeButton1BgColor, fg=placeButton1FgColor);
        d5 = tk.Button(dbframe, image=row5[3], command=lambda: placeButtonClicked("d", 5, row5[3]), font=buttonFont,
                    bg=placeButton2BgColor, fg=placeButton2FgColor);
        d6 = tk.Button(dbframe, image=row6[3], command=lambda: placeButtonClicked("d", 6, row6[3]), font=buttonFont,
                    bg=placeButton1BgColor, fg=placeButton1FgColor);
        d7 = tk.Button(dbframe, image=row7[3], command=lambda: placeButtonClicked("d", 7, row7[3]), font=buttonFont,
                    bg=placeButton2BgColor, fg=placeButton2FgColor);
        d8 = tk.Button(dbframe, image=row8[3], command=lambda: placeButtonClicked("d", 8, row8[3]), font=buttonFont,
                    bg=placeButton1BgColor, fg=placeButton1FgColor);

        # create column e buttons
        e1 = tk.Button(dbframe, image=row1[4], command=lambda: placeButtonClicked("e", 1, row1[4]), font=buttonFont,
                    bg=placeButton1BgColor, fg=placeButton1FgColor);
        e2 = tk.Button(dbframe, image=row2[4], command=lambda: placeButtonClicked("e", 2, row2[4]), font=buttonFont,
                    bg=placeButton2BgColor, fg=placeButton2FgColor);
        e3 = tk.Button(dbframe, image=row3[4], command=lambda: placeButtonClicked("e", 3, row3[4]), font=buttonFont,
                    bg=placeButton1BgColor, fg=placeButton1FgColor);
        e4 = tk.Button(dbframe, image=row4[4], command=lambda: placeButtonClicked("e", 4, row4[4]), font=buttonFont,
                    bg=placeButton2BgColor, fg=placeButton2FgColor);
        e5 = tk.Button(dbframe, image=row5[4], command=lambda: placeButtonClicked("e", 5, row5[4]), font=buttonFont,
                    bg=placeButton1BgColor, fg=placeButton1FgColor);
        e6 = tk.Button(dbframe, image=row6[4], command=lambda: placeButtonClicked("e", 6, row6[4]), font=buttonFont,
                    bg=placeButton2BgColor, fg=placeButton2FgColor);
        e7 = tk.Button(dbframe, image=row7[4], command=lambda: placeButtonClicked("e", 7, row7[4]), font=buttonFont,
                    bg=placeButton1BgColor, fg=placeButton1FgColor);
        e8 = tk.Button(dbframe, image=row8[4], command=lambda: placeButtonClicked("e", 8, row8[4]), font=buttonFont,
                    bg=placeButton2BgColor, fg=placeButton2FgColor);

        # create column f buttons
        f1 = tk.Button(dbframe, image=row1[5], command=lambda: placeButtonClicked("f", 1, row1[5]), font=buttonFont,
                    bg=placeButton2BgColor, fg=placeButton2FgColor);
        f2 = tk.Button(dbframe, image=row2[5], command=lambda: placeButtonClicked("f", 2, row2[5]), font=buttonFont,
                    bg=placeButton1BgColor, fg=placeButton1FgColor);
        f3 = tk.Button(dbframe, image=row3[5], command=lambda: placeButtonClicked("f", 3, row3[5]), font=buttonFont,
                    bg=placeButton2BgColor, fg=placeButton2FgColor);
        f4 = tk.Button(dbframe, image=row4[5], command=lambda: placeButtonClicked("f", 4, row4[5]), font=buttonFont,
                    bg=placeButton1BgColor, fg=placeButton1FgColor);
        f5 = tk.Button(dbframe, image=row5[5], command=lambda: placeButtonClicked("f", 5, row5[5]), font=buttonFont,
                    bg=placeButton2BgColor, fg=placeButton2FgColor);
        f6 = tk.Button(dbframe, image=row6[5], command=lambda: placeButtonClicked("f", 6, row6[5]), font=buttonFont,
                    bg=placeButton1BgColor, fg=placeButton1FgColor);
        f7 = tk.Button(dbframe, image=row7[5], command=lambda: placeButtonClicked("f", 7, row7[5]), font=buttonFont,
                    bg=placeButton2BgColor, fg=placeButton2FgColor);
        f8 = tk.Button(dbframe, image=row8[5], command=lambda: placeButtonClicked("f", 8, row8[5]), font=buttonFont,
                    bg=placeButton1BgColor, fg=placeButton1FgColor);

        # create column g buttons
        g1 = tk.Button(dbframe, image=row1[6], command=lambda: placeButtonClicked("g", 1, row1[6]), font=buttonFont,
                    bg=placeButton1BgColor, fg=placeButton1FgColor);
        g2 = tk.Button(dbframe, image=row2[6], command=lambda: placeButtonClicked("g", 2, row2[6]), font=buttonFont,
                    bg=placeButton2BgColor, fg=placeButton2FgColor);
        g3 = tk.Button(dbframe, image=row3[6], command=lambda: placeButtonClicked("g", 3, row3[6]), font=buttonFont,
                    bg=placeButton1BgColor, fg=placeButton1FgColor);
        g4 = tk.Button(dbframe, image=row4[6], command=lambda: placeButtonClicked("g", 4, row4[6]), font=buttonFont,
                    bg=placeButton2BgColor, fg=placeButton2FgColor);
        g5 = tk.Button(dbframe, image=row5[6], command=lambda: placeButtonClicked("g", 5, row5[6]), font=buttonFont,
                    bg=placeButton1BgColor, fg=placeButton1FgColor);
        g6 = tk.Button(dbframe, image=row6[6], command=lambda: placeButtonClicked("g", 6, row6[6]), font=buttonFont,
                    bg=placeButton2BgColor, fg=placeButton2FgColor);
        g7 = tk.Button(dbframe, image=row7[6], command=lambda: placeButtonClicked("g", 7, row7[6]), font=buttonFont,
                    bg=placeButton1BgColor, fg=placeButton1FgColor);
        g8 = tk.Button(dbframe, image=row8[6], command=lambda: placeButtonClicked("g", 8, row8[6]), font=buttonFont,
                    bg=placeButton2BgColor, fg=placeButton2FgColor);

        # create column h buttons
        h1 = tk.Button(dbframe, image=row1[7], command=lambda: placeButtonClicked("h", 1, row1[7]), font=buttonFont,
                    bg=placeButton2BgColor, fg=placeButton2FgColor);
        h2 = tk.Button(dbframe, image=row2[7], command=lambda: placeButtonClicked("h", 2, row2[7]), font=buttonFont,
                    bg=placeButton1BgColor, fg=placeButton1FgColor);
        h3 = tk.Button(dbframe, image=row3[7], command=lambda: placeButtonClicked("h", 3, row3[7]), font=buttonFont,
                    bg=placeButton2BgColor, fg=placeButton2FgColor);
        h4 = tk.Button(dbframe, image=row4[7], command=lambda: placeButtonClicked("h", 4, row4[7]), font=buttonFont,
                    bg=placeButton1BgColor, fg=placeButton1FgColor);
        h5 = tk.Button(dbframe, image=row5[7], command=lambda: placeButtonClicked("h", 5, row5[7]), font=buttonFont,
                    bg=placeButton2BgColor, fg=placeButton2FgColor);
        h6 = tk.Button(dbframe, image=row6[7], command=lambda: placeButtonClicked("h", 6, row6[7]), font=buttonFont,
                    bg=placeButton1BgColor, fg=placeButton1FgColor);
        h7 = tk.Button(dbframe, image=row7[7], command=lambda: placeButtonClicked("h", 7, row7[7]), font=buttonFont,
                    bg=placeButton2BgColor, fg=placeButton2FgColor);
        h8 = tk.Button(dbframe, image=row8[7], command=lambda: placeButtonClicked("h", 8, row8[7]), font=buttonFont,
                    bg=placeButton1BgColor, fg=placeButton1FgColor);
        
        aLabel = tk.Button(dbframe, text="A", font=buttonFont, bg="black", fg="white");
        bLabel = tk.Button(dbframe, text="B", font=buttonFont, bg="black", fg="white");
        cLabel = tk.Button(dbframe, text="C", font=buttonFont, bg="black", fg="white");
        dLabel = tk.Button(dbframe, text="D", font=buttonFont, bg="black", fg="white");
        eLabel = tk.Button(dbframe, text="E", font=buttonFont, bg="black", fg="white");
        fLabel = tk.Button(dbframe, text="F", font=buttonFont, bg="black", fg="white");
        gLabel = tk.Button(dbframe, text="G", font=buttonFont, bg="black", fg="white");
        hLabel = tk.Button(dbframe, text="H", font=buttonFont, bg="black", fg="white");

        label1 = tk.Button(dbframe, text="1", font=buttonFont, bg="black", fg="white");
        label2 = tk.Button(dbframe, text="2", font=buttonFont, bg="black", fg="white");
        label3 = tk.Button(dbframe, text="3", font=buttonFont, bg="black", fg="white");
        label4 = tk.Button(dbframe, text="4", font=buttonFont, bg="black", fg="white");
        label5 = tk.Button(dbframe, text="5", font=buttonFont, bg="black", fg="white");
        label6 = tk.Button(dbframe, text="6", font=buttonFont, bg="black", fg="white");
        label7 = tk.Button(dbframe, text="7", font=buttonFont, bg="black", fg="white");
        label8 = tk.Button(dbframe, text="8", font=buttonFont, bg="black", fg="white");


        #place a buttons
        aLabel.grid(row=0, column=2, padx=1, pady=1);
        a1.grid(row=8, column=2, padx=1, pady=1);
        a2.grid(row=7, column=2, padx=1, pady=1);
        a3.grid(row=6, column=2, padx=1, pady=1);
        a4.grid(row=5, column=2, padx=1, pady=1);
        a5.grid(row=4, column=2, padx=1, pady=1);
        a6.grid(row=3, column=2, padx=1, pady=1);
        a7.grid(row=2, column=2, padx=1, pady=1);
        a8.grid(row=1, column=2, padx=1, pady=1);

        # place b buttons
        bLabel.grid(row=0, column=3, padx=1, pady=1);
        b1.grid(row=8, column=3, padx=1, pady=1);
        b2.grid(row=7, column=3, padx=1, pady=1);
        b3.grid(row=6, column=3, padx=1, pady=1);
        b4.grid(row=5, column=3, padx=1, pady=1);
        b5.grid(row=4, column=3, padx=1, pady=1);
        b6.grid(row=3, column=3, padx=1, pady=1);
        b7.grid(row=2, column=3, padx=1, pady=1);
        b8.grid(row=1, column=3, padx=1, pady=1);

        # place c buttons
        cLabel.grid(row=0, column=4, padx=1, pady=1);
        c1.grid(row=8, column=4, padx=1, pady=1);
        c2.grid(row=7, column=4, padx=1, pady=1);
        c3.grid(row=6, column=4, padx=1, pady=1);
        c4.grid(row=5, column=4, padx=1, pady=1);
        c5.grid(row=4, column=4, padx=1, pady=1);
        c6.grid(row=3, column=4, padx=1, pady=1);
        c7.grid(row=2, column=4, padx=1, pady=1);
        c8.grid(row=1, column=4, padx=1, pady=1);

        # place d buttons
        dLabel.grid(row=0, column=5, padx=1, pady=1);
        d1.grid(row=8, column=5, padx=1, pady=1);
        d2.grid(row=7, column=5, padx=1, pady=1);
        d3.grid(row=6, column=5, padx=1, pady=1);
        d4.grid(row=5, column=5, padx=1, pady=1);
        d5.grid(row=4, column=5, padx=1, pady=1);
        d6.grid(row=3, column=5, padx=1, pady=1);
        d7.grid(row=2, column=5, padx=1, pady=1);
        d8.grid(row=1, column=5, padx=1, pady=1);

        #place e buttons
        eLabel.grid(row=0, column=6, padx=1, pady=1);
        e1.grid(row=8, column=6, padx=1, pady=1);
        e2.grid(row=7, column=6, padx=1, pady=1);
        e3.grid(row=6, column=6, padx=1, pady=1);
        e4.grid(row=5, column=6, padx=1, pady=1);
        e5.grid(row=4, column=6, padx=1, pady=1);
        e6.grid(row=3, column=6, padx=1, pady=1);
        e7.grid(row=2, column=6, padx=1, pady=1);
        e8.grid(row=1, column=6, padx=1, pady=1);

        # place f buttons
        fLabel.grid(row=0, column=7, padx=1, pady=1);
        f1.grid(row=8, column=7, padx=1, pady=1);
        f2.grid(row=7, column=7, padx=1, pady=1);
        f3.grid(row=6, column=7, padx=1, pady=1);
        f4.grid(row=5, column=7, padx=1, pady=1);
        f5.grid(row=4, column=7, padx=1, pady=1);
        f6.grid(row=3, column=7, padx=1, pady=1);
        f7.grid(row=2, column=7, padx=1, pady=1);
        f8.grid(row=1, column=7, padx=1, pady=1);

        # place g buttons
        gLabel.grid(row=0, column=8, padx=1, pady=1);
        g1.grid(row=8, column=8, padx=1, pady=1);
        g2.grid(row=7, column=8, padx=1, pady=1);
        g3.grid(row=6, column=8, padx=1, pady=1);
        g4.grid(row=5, column=8, padx=1, pady=1);
        g5.grid(row=4, column=8, padx=1, pady=1);
        g6.grid(row=3, column=8, padx=1, pady=1);
        g7.grid(row=2, column=8, padx=1, pady=1);
        g8.grid(row=1, column=8, padx=1, pady=1);

        # place h buttons
        hLabel.grid(row=0, column=9, padx=1, pady=1);
        h1.grid(row=8, column=9, padx=1, pady=1);
        h2.grid(row=7, column=9, padx=1, pady=1);
        h3.grid(row=6, column=9, padx=1, pady=1);
        h4.grid(row=5, column=9, padx=1, pady=1);
        h5.grid(row=4, column=9, padx=1, pady=1);
        h6.grid(row=3, column=9, padx=1, pady=1);
        h7.grid(row=2, column=9, padx=1, pady=1);
        h8.grid(row=1, column=9, padx=1, pady=1);

        label1.grid(row=8, column=0, padx=1, pady=1);
        label2.grid(row=7, column=0, padx=1, pady=1);
        label3.grid(row=6, column=0, padx=1, pady=1);
        label4.grid(row=5, column=0, padx=1, pady=1);
        label5.grid(row=4, column=0, padx=1, pady=1);
        label6.grid(row=3, column=0, padx=1, pady=1);
        label7.grid(row=2, column=0, padx=1, pady=1);
        label8.grid(row=1, column=0, padx=1, pady=1);
        

    updateButtons();


    def removePiece(letter, number): #removes a piece from a place on the board
        places[numbers.index(number)][letters.index(letter)] = none;
        updateButtons();
        
    def placePiece(letter, number, piece): #adds a piece at a certain place
        places[numbers.index(number)][letters.index(letter)] = piece;
        updateButtons();
    
    def label(text): #adds a label at (30, 20)
            var = tk.StringVar();  # method needed to update strings when buttons are clicked
            var.set(text);  # setting the variable var to numStr (puts value in label)
            label = tk.Label(root, textvariable=var, font=labelFont, bg=labelBgColor, fg=labelFgColor);
            label.place(x=30, y=20);  # label is in the window but not the frame
            label.config(text=text)

    def promoteButtonClicked(piece, color): #when the button to promote a pawn is clicked
        global pieceSelected;
        global pieceSelectedLocation;
        if piece != none:
            label("Click On A " + color + " Pawn To Promote it \n "); #create label  
            pieceSelected = piece;
            pieceSelectedLocation = False;
    
    # def undoButtonClicked(piece): #when a place on the board is clicked
    #     global pieceSelected;
    #     global pieceSelectedLocation;
    #     if piece != none:
    #         #create label
    #         label("Undo", piece, "selected.\nClick on board to place it");  
    #         pieceSelected = piece;

    def placeButtonClicked(letter, number, piece): #when a place on the board is clicked
        global pieceSelected;
        global pieceSelectedLocation;
        print(letter + ",", number);
        if not pieceSelected: #if there is not already a selected piece
            if piece != none: #is the square has a piece in it
                #create label
                label(letter+str(number)+" has been selected.\nNow click on the square you want to move this piece to.");  
                pieceSelected = piece;
                pieceSelectedLocation = (letter, number);
        else: #if a piece hasd been selected
            # if piece != none:
            #     dead.insert(0, piece);
            #     print(dead)
            #     updateSidePanel()
            removePiece(letter, number); 
            if pieceSelectedLocation: 
                removePiece(pieceSelectedLocation[0], pieceSelectedLocation[1]);
            else: #if the selected piece is a queen to promote a pawn
                if pieceSelected in promoteWhite:
                    promoteWhite.remove(pieceSelected)
                elif pieceSelected in promoteBlack:
                    promoteBlack.remove(pieceSelected)
            placePiece(letter, number, pieceSelected);
            label("No Piece Selected\n                                 Click on a Piece to select it!                                 ")
            print("!");var = tk.StringVar();  # method needed to update strings when buttons are clicked

            pieceSelected = piece;
            pieceSelected = False;


    

    #set button sizes
    buttonHeight = 10;
    buttonWidth = 10;

    

    root.mainloop();



