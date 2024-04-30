from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cf02cebb930880d06cf1aaa7926b0199'
app.config['MAIL_SERVER'] = 'smtp.yandex.ru'  # Укажите SMTP-сервер
app.config['MAIL_PORT'] = 465  # Порт SMTP-сервера (обычно 587 для TLS)
app.config['MAIL_USE_TLS'] = True  # Использовать ли TLS для шифрования соединения
app.config['MAIL_USERNAME'] = 'savvmuhin@yandex.ru'  # Укажите имя пользователя SMTP
app.config['MAIL_PASSWORD'] = 'safxvfvdrfedsddfsdhdrds143132rwfw'  # Укажите пароль SMTP
app.config['MAIL_DEFAULT_SENDER'] = 'savvmuhin@yandex.ru'  # Укажите адрес отправителя по умолчанию

mail = Mail(app)

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

    # Отправка электронной почты
    msg = Message('Новая заявка на консультацию', recipients=['savvmuhin@yandex.ru'])  # Укажите адрес получателя
    msg.body = f'Имя: {first_name}\nФамилия: {last_name}\nОтчество: {middle_name}\nEmail: {email}\nЦель консультации: {purpose}'
    mail.send(msg)

    # Перенаправление на страницу с сообщением о том, что заявка отправлена
    return redirect(url_for('consultation_success'))


@app.route('/consultation_success')
def consultation_success():
    return render_template('consultation_success.html', title='Заявка отправлена')


if __name__ == '__main__':
    app.run(debug=True)

