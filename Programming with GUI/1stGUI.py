from guizero import App, Text

app = App(title =  "This is my first GUI")

firstmessage = Text(app, text = "GUIS are cool!")
secondmessage   =   Text(app, text = "This is green")
thridmessage    =   Text(app, text = "this is the challenge")

firstmessage.text_size  =   40
secondmessage.bg    =   "green"
thridmessage.font   =   "Arial Bold"

app.display()