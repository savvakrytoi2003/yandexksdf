from flask import Flask, render_template, request

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


@app.route('/submit_consultation', methods=['POST'])
def submit_consultation():
    # Получение данных из формы
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    middle_name = request.form.get('middle_name')
    email = request.form.get('email')
    purpose = request.form.get('purpose')

    # Логика обработки данных формы

    # Возвращаем сообщение об успешной отправке консультации
    return render_template('consultation_success.html', title='Консультация отправлена')



if __name__ == '__main__':
    app.run(debug=True)
