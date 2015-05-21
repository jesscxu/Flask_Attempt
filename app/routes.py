from flask import Flask, render_template
  
app = Flask(__name__)
  
@app.route('/')
def home():
  return render_template('home.html')
  
@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/dataviz')
def dataviz():
  return render_template('dataviz.html')

#Sending the us.json file
@app.route('/glassbeadlabs/')
def glassbeadlabs():
    return "<a href=%s>file</a>" % url_for('static', filename='glass-bead-labs.json')
  
if __name__ == '__main__':
  app.run(debug=True)