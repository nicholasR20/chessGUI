import tkinter as tk;
import game



def welcomeWindow():
    # create a Window called "root"
    root = tk.Tk();
    root.configure(bg="blue");
    root.title("Welcome Screen");
    root.geometry("400x300");

    dbframe = tk.Frame(root);  # frame is placed inside window 'root'
    dbframe.pack(side="left", padx=30, pady=10);  # padx and pady are set margins for the frame
    dbframe.configure(bg="black");

    #set label fonts and colors
    labelFont = ("tkDefaultFont", 18);
    labelBgColor = "blue";
    labelFgColor = "white";

    #set label fonts and color
    buttonFont = ("tkDefaultFont", 12);
    frameBgColor = "red";
    frameFgColor = "white";

    def startGame(): #destory welcome screen window and open game window
        root.destroy()
        game.play()


    # defines and sets up the buttons
    play = tk.Button(dbframe, text="      PLAY      ", command=startGame, font=buttonFont, bg=frameBgColor, fg=frameFgColor);

    play.grid(row=1, column=1, padx=5, pady=5);

    #create label
    var = tk.StringVar();  # method needed to update strings when buttons are clicked
    var.set("Welcome To Chess!");  # setting the variable var to numStr (puts value in label)
    label = tk.Label(root, textvariable=var, font=labelFont, bg=labelBgColor, fg=labelFgColor);
    label.place(x=30, y=40);  # label is in the window but not the frame

    #create second label
    var = tk.StringVar();  # method needed to update strings when buttons are clicked
    var.set("Click Below To Begin:");  # setting the variable var to numStr (puts value in label)
    label = tk.Label(root, textvariable=var, font=labelFont, bg=labelBgColor, fg=labelFgColor);
    label.place(x=30, y=85);  # label is in the window but not the frame

    root.mainloop();