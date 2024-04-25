from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title='Главная')


@app.route('/projects')
def projects():
    return render_template('projects.html', title='Проекты')


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Контакты')


if __name__ == '__main__':
    app.run(debug=True)
