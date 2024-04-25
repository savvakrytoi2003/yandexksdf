from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title='Главная')


@app.route('/contact_form')
def contact_form():
    return render_template('consultation_form.html', title='Получить консультацию')


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Контакты')


if __name__ == '__main__':
    app.run(debug=False)
