import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    projects = [
        {
            "image": "static/images/CryptoBazaar.png",
            "title": "CyrptoBazaar",
            "description": "A blockchain-based marketplace for buying and selling digital goods. This application was built with React.js, NEAR Protocol, TypeScript, Javascript, and C",
            "github": "https://github.com/NeathRand/blockchain-marketplace"
        },
        {
            "image": "static/images/LaunchPad.png",
            "title": "Launch Pad",
            "description": "This is a launch Pad created to help navigate and save links to my fequently used webpages. This website is created with HTML, CSS, and Javascript",
            "github": "https://github.com/NeathRand/Launch-Pad"
        },
        {
            "image": "static/images/LaunchPad.png",
            "title": "Launch Pad",
            "description": "This is a launch Pad created to help navigate and save links to my fequently used webpages. This website is created with HTML, CSS, and Javascript",
            "github": "https://github.com/NeathRand/Launch-Pad"
        },
        # Add more projects when i have more
    ]
    return render_template('index.html', projects=projects)
    

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        message = request.form['message']

        sender_email = 'mywebsite53221@outlook.com' # This should be correct but im not sure why it doesn't work   mywebsite53221@outlook.com  Hello_1235   mwebsite232@gmail.com
        receiver_email = 'mywebsite53221@outlook.com'
        password = 'Hello_1235'

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = "New Contact Form Submission"

        body = f"First Name: {firstname}\nLast Name: {lastname}\nEmail: {email}\nMessage: {message}"
        msg.attach(MIMEText(body, 'plain'))

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)  # i'm not sure if this is the correct SMTP and port
            server.starttls()
            server.login(sender_email, password)
            text = msg.as_string()
            server.sendmail(sender_email, receiver_email, text)
            server.quit()
        except Exception as e:
            print(f"Failed to send email: {e}")
        
        return render_template('contact.html', firstname=firstname, lastname=lastname, email=email, message=message, submitted=True)
    return render_template('contact.html', submitted=False)


if __name__ == '__main__':
    app.run(debug=True, port=5001)

