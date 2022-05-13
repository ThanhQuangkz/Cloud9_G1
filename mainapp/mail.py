from flask import Flask
import smtplib

app=Flask(__name__)

@app.route('/')
def index():
    mes="hello"
    sever = smtplib.SMTP("smtp.gmail.com",587)
    sever.starttls()
    sever.login("tranthanhquang2704@gmail.com","ihjqezoqpnqxvlql")
    sever.sendmail("tranthanhquang2704@gmail.com","tranthanhquang2704@gmail.com",mes)
    return "Sent"

if __name__=="__main__":
    app.run()