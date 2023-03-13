from flask import Flask, render_template, flash, redirect, url_for, Blueprint
from forms import AddDiscountForm, AddProductForm
from models import db, Discounts, Products
from flask_wtf.csrf import CSRFProtect
from PIL import Image
from io import BytesIO
from werkzeug.utils import secure_filename
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'irk7IFD9ZP4keef78'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
csrf = CSRFProtect()
csrf.init_app(app)
db.init_app(app)

migrate = Migrate(app, db)

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'irk7IFD9ZP4keef78'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/posdb'
# csrf = CSRFProtect()
# csrf.init_app(app)
# db.init_app(app)

@app.route("/")
def index():
    return redirect(url_for('product'))

@app.route('/product')
def product():
    # Query all products from the database
    products = Products.query.all()
    form = AddDiscountForm()
    return render_template('product.html', products=products, form=form)

@app.route('/add-product', methods=['GET', 'POST'])
def add_product():
    form = AddProductForm()
    if form.validate_on_submit():
        name = form.name.data
        price = form.price.data
        tax = form.tax.data

        # Get the uploaded image
        image_file = form.image.data
        image_data = image_file.read()
        image_name = secure_filename(image_file.filename)
        # Save the image to disk
        image = Image.open(BytesIO(image_data))
        image.save('static/images/' + image_file.filename)

        product_add = Products(name=name, price=price, tax=tax, image=image_name)
        db.session.add(product_add)
        db.session.commit()
        flash('product has been added successfully!', 'success')
        return redirect(url_for('product'))
    flash('Error in product , insert valide name or price or tax or image', 'error')
    return redirect(url_for('product'))

@app.route('/add_discount', methods=['GET', 'POST'])
def add_discount():
    form = AddDiscountForm()
    if form.validate_on_submit():
        name = form.name.data
        percentage = form.percentage.data
        discount_action = Discounts(name=name, percentage=percentage)
        db.session.add(discount_action)
        db.session.commit()
        flash('Discount action has been added successfully!', 'success')
        return redirect(url_for('product'))
    flash('Error in Discount , insert valide name or percentage', 'error')
    return redirect(url_for('product'))

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    products = Products.query.all()
    
    discounts = Discounts.query.all()
    discounts_list = []
    for discount in discounts:
        discount_dict = {
            'id': discount.id,
            'name': discount.name,
            'percentage': discount.percentage
        }
        discounts_list.append(discount_dict)

    return render_template('checkout.html', products=products, discounts=discounts_list)

@app.route('/discount', methods=['GET'])
def discount():
    discounts = Discounts.query.all()
    discounts_list = []
    for discount in discounts:
        discount_dict = {
            'id': discount.id,
            'name': discount.name,
            'percentage': discount.percentage
        }
        discounts_list.append(discount_dict)

    return render_template('discount.html', discounts=discounts_list)

if __name__ == "__main__":
    app.run(debug=True)

'''
@app.route('/discount')
def discount():
    # Query all discount actions from the database
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM discount_actions')
    discount_actions = cursor.fetchall()
    cursor.close()

    return render_template('discount.html', discount_actions=discount_actions)
'''

# db = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="",
#   database="posdb"
# )