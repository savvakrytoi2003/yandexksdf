from views import app as views_app
from reg import app as reg_app

if __name__ == "__main__":
    views_app.run(debug=True)
    reg_app.run(debug=True)