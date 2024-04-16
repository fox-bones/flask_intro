from flask import Flask, render_template, request
from encrypt import encrypt_with_shift
alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
@app.route('/user_message', methods=["GET", "POST"])
def user_message():    
    if request.method == "POST":
        message = request.form["text"]
        shift = int(request.form["shift"])
        encrypt = request.form["encryption"]
        if encrypt == "encrypt":
            if any(c.isalpha() for c in message) == True and message != "" and shift >= 1 and shift <= 25 and len(message) < 50:
                origin_text = "Original message: " + message
                cypher_text = "Altered message: " + encrypt_with_shift(message, shift)
            else: 
                cypher_text = ""
                origin_text = "Please check your inputs."
        elif encrypt == "decrypt":
            if any(c.isalpha() for c in message) == True and message != "" and shift >= 1 and shift <= 25 and len(message) < 50:
                origin_text = "Original message: " + encrypt_with_shift(message, -(shift))
                cypher_text = ""
            else: 
                cypher_text = ""
                origin_text = "Please check your inputs."
    elif request.method == "GET":
        print("Hello")
        cypher_text = ""

    return render_template('user_message.html', cypher_text = cypher_text, origin_text = origin_text)

if __name__ == '__main__':
    app.run()

# Instructions for this project can be found here:
# https://education.launchcode.org/lchs/chapters/flask-intro/project.html
