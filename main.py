from flask import Flask, render_template

app = Flask(__name__)


@app.route('/training/<prof>')
def training(prof):
    if 'инженер' in prof.lower():
        return render_template('page.html', arg='Инженерные тренажеры')
    else:
        return render_template('page.html', arg='Научные симуляторы')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
