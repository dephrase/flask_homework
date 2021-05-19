from flask import render_template
from app import app
from app.models.order_list import orders

@app.route('/orders')
def index():
    return render_template('index.html', title='Home', orders = orders)

@app.route('/orders/<index>')
def specific_order(index):
    return render_template('specific_order.html', title='Order f{index}', order = orders[int(index)], index = index)
