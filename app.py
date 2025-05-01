from flask import Flask, render_template

app = Flask(__name__)

@app.route('/distribution')
def distribute():
    astronauts = ['Иван Иванов', 'Сергей Смирнов', 'Анна Каренина', 'Юрий Гагарин']
    return render_template('distribution.html', astronauts=astronauts)

if __name__ == '__main__':
    app.run(debug=True)
