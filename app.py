from flask import Flask, render_template


app = Flask(__name__)
"""
Создать базовый шаблон для интернет-магазина, 
содержащий общие элементы дизайна (шапка, меню, подвал), 
и дочерние шаблоны для страниц категорий товаров и отдельных товаров. 
Например, создать страницы «Одежда», «Обувь» и «Куртка», 
используя базовый шаблон.
"""


@app.route('/')
def index():
    title = 'Главная'
    return render_template('index.html', title=title)



@app.route('/clothes/')
def clothes():
    title = 'Одежда'
    _clothes= [{
        'name': 'шапка',
        'price': '300р',
    }]
    return render_template('clothes.html', clothes=_clothes, title=title)

@app.route('/shoes/')
def shoes():
    title = 'Обувь'
    _shoes = [{
        'name': 'обувь',
        'price': '3000p',
    }]
    return render_template('shoes.html', shoes=_shoes, title=title)
@app.route('/jacket/')
def jacket():
    title = 'Куртка'
    _jacket = [{
        'name': 'Куртка',
        'price': '3000p',
    }]
    return render_template('jacket.html', jacket=_jacket, title=title)



if __name__ == '__main__':
    app.run(debug=True)