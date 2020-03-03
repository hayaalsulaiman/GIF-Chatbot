import pyglet
from tkinter import *
import webbrowser
from random import *

file = open("words.txt", "r")
f = file.readlines()
print("frustrated\n" in f)
file.close()


def Animation(name):
    animation = pyglet.image.load_animation(name + '.gif')
    animSprite = pyglet.sprite.Sprite(animation)

    w = animSprite.width
    h = animSprite.height

    window = pyglet.window.Window(width=w, height=h)

    @window.event
    def on_draw():
        window.clear()
        animSprite.draw()

    pyglet.app.run()


window = Tk()
# window.geometry("600x400")
# window.title("GIFS")
# img = PhotoImage(file="gif.png")

window.geometry("180x275")
window.title("GIFS")
img = PhotoImage(file="gif2.png")
panel = Label(window, image=img)
panel.place(x=0, y=0)

lbl = Label(window, text="what's your mood like",font='impact 16 bold ', fg='White', bg='#D23636')
lbl.place(x=20, y=10)

t = Entry(window, width=15)
t.place(x=20, y=80)


def test(d):
    d=d.lower()
    if (d in ""):
        Animation("nothing")
    elif ("nope" in d) or("no" in d) :
        Animation("8_NopeRat")
    elif ("hi" in d)or ("hello" in d) :
        Animation("hi")
    elif ("yep" in d) or ("yup" in d):
        Animation("yup")
    elif ("yes" in d):
        Animation("yes")
    elif ("happy"in d)or("joy" in d) :
        Animation("happy")
    elif ("shocked" in d) :
        Animation("shocked")
    elif ("sad" in d) :
        Animation("sad")
    elif ("crying" in d)or("breakdown" in d):
        Animation("crying")
    else:

        file = open("words.txt", "r")
        f = file.readlines()
        file.close()

        if d+"\n" in f:
            webbrowser.open_new(r"https://giphy.com/search/" + d)

        else:

            l=["unkown","exp"]
            ran= randint(0, 2)
            Animation(l[ran])



imgg = PhotoImage(file="search.png")
tm=imgg.subsample(15,15)
btn = Button(window, text="enter!",image=tm ,command=lambda: test(t.get()))
btn.place(x=70, y=235)

window.mainloop()