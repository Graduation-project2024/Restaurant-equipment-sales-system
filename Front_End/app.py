from flask import Flask, render_template

app = Flask(__name__)

# المسار للصفحة الرئيسية
@app.route('/')
def home():
  return render_template('home.html')

# المسار لصفحة البحث
@app.route('/search')
def search():
  return render_template('search_page.html')

# المسار لصفحة التسجيل
@app.route('/register')
def register():
  return render_template('user_register.html')

# المسار لصفحة تسجيل الدخول
@app.route('/login')
def login():
  return render_template('user_login.html')

# المسار لصفحة تحديث البيانات
@app.route('/update')
def update():
  return render_template('update_user.html')

# المسار لصفحة اتصل بنا
@app.route('/contact')
def contact():
  return render_template('contact.html')

# المسار لصفحة المتجر
@app.route('/shop')
def shop():
  return render_template('shop.html')

# المسار لصفحة معلومات عنا
@app.route('/about')
def about():
  return render_template('about.html')

# المسار لصفحة الطلبات
@app.route('/orders')
def orders():
  return render_template('orders.html')

# المسار لصفحة قائمة الرغبات
@app.route('/wishlist')
def wishlist():
  return render_template('wishlist.html')

# المسار لصفحة قائمة عربة التسوق
@app.route('/cart')
def cart():
  return render_template('cart.html')

# المسار لصفحة الفئات
@app.route('/category')
def category():
  return render_template('category.html')

# المسار لصفحة نظرة سريعة
@app.route('/quick')
def quick():
  return render_template('quick_view.html')

# المسار لصفحة نظرة سريعة
@app.route('/checkout')
def checkout():
  return render_template('checkout.html')

if __name__ == '__main__':
  app.run(debug=True)
