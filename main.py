from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('page.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    if 'инженер' in prof.lower():
        return render_template('train.html', arg='Инженерные тренажеры')
    elif 'строител' in prof.lower():
        return render_template('train.html', arg='Научные симуляторы')
    else:
        return render_template('train.html', arg='Базовый тренажёр')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
