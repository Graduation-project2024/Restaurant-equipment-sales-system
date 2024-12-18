
# نظام بيع معدات المطاعم

## 📖 الوصف
**نظام بيع معدات المطاعم** هو منصة شاملة تهدف إلى تبسيط عمليات البيع، وإدارة المخزون، وتنظيم تجارة معدات المطاعم. يهدف النظام إلى تسهيل عملية الشراء لأصحاب المطاعم والفنادق والمصالح المختلفة وتوفير وسيلة فعالة للموردين لإدارة مخزونهم والتواصل مع العملاء.

### 🎯 الميزات الرئيسية:
- **إدارة العملاء**: واجهة سهلة الاستخدام لتصفح المنتجات، إدارة الطلبات، وتتبع الشحنات.
- **أدوات الموردين**: إدارة المخزون والتحليلات للموردين.
- **دورة حياة الطلب**: إدارة كاملة للطلبات من إنشاء الطلب إلى التسليم.
- **دمج الدفع**: طرق دفع آمنة (بطاقات ائتمان، PayPal، وغيرها).
- **إدارة الشحن**: تكامل مع مزودي الخدمات اللوجستية لتتبع عمليات التسليم.
- **التحليلات**: تقارير حول المبيعات، المخزون، وأداء النظام.

---

## 📋 المتطلبات
### متطلبات النظام:
- **نظام التشغيل**: بيئة قائمة على Linux أو Windows باستخدام WSL.
- **قاعدة البيانات**: MariaDB مثبتة بشكل منفصل للتوافق مع Django.
- **خادم الويب**: Apache (عبر XAMPP بدون MySQL).

### المتطلبات البرمجية (Python Dependencies):
مدرجة في ملف `requirement.txt`:
```plaintext
asgiref==3.8.1
blinker==1.9.0
click==8.1.7
colorama==0.4.6
Django==5.1.4
itsdangerous==2.2.0
Jinja2==3.1.4
MarkupSafe==3.0.2
mysqlclient==2.2.6
sqlparse==0.5.3
tzdata==2024.2
Werkzeug==3.1.3
```
تثبيت باستخدام:
```bash
pip install -r requirement.txt
```

---

## 🛠️ خطوات التثبيت
1. استنساخ المستودع:
   ```bash
   git clone https://github.com/Graduation-project2024/Restaurant-equipment-sales-system.git
   cd Restaurant-equipment-sales-system
   ```
2. تثبيت المتطلبات:
   ```bash
   pip install -r requirement.txt
   ```
3. إعداد قاعدة البيانات:
   - تأكد من تثبيت وتشغيل MariaDB.
   - قم بإنشاء قاعدة بيانات:
     ```sql
     CREATE DATABASE restaurant_equipment_sales_system;
     ```
   - قم بتحديث ملف `settings.py` ببيانات اعتماد قاعدة البيانات:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.mysql',
             'NAME': 'restaurant_equipment_sales_system',
             'USER': 'root',
             'PASSWORD': 'your_password',
             'HOST': 'localhost',
             'PORT': '3306',
         }
     }
     ```
4. تطبيق الترحيلات:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. تشغيل الخادم:
   ```bash
   python manage.py runserver
   ```

---

## 📂 هيكل المشروع
```
Restaurant-equipment-sales-system/
├── README.md              # توثيق المشروع
├── requirement.txt        # المتطلبات البرمجية
├── manage.py              # إدارة مشروع Django
├── database/              # السكربتات الاحتياطية لقاعدة البيانات
├── store/                 # تطبيق المتجر
├── static/                # الموارد الأمامية (CSS/JS/الصور)
├── templates/             # القوالب HTML
└── tests/                 # اختبارات المشروع الآلية
```

---

## 📊 المخططات
### مخطط الكيانات والعلاقات (ERD)
![Notations for Traditional ERD](https://github.com/user-attachments/assets/3c915fa6-225c-40e8-a688-51a8efa03234)


### مخطط تدفق البيانات (DFD)
![Restaurant equipment sales system](https://github.com/user-attachments/assets/1c5a4952-ba84-4aae-8dd5-b669fced92ac)

---

## 🤝 المساهمون
- **إسلام محمد جودة عبيد** (قائد الفريق، مصمم، مطور الواجهة الأمامية)
- **مصطفى السيد مصطفى** (مطوّر الواجهة الخلفية، مصمم)
- **عبد الله محمد عنتر** (مطوّر الواجهة الخلفية، محلل نظم، مصمم)
- **مصطفى محمد بسيوني** (مطوّر الواجهة الأمامية، مصمم)
- **مريم عبد الفتاح عبد المجيد** (مطوّر الواجهة الخلفية)
- **مهاد رجب حامد فرج** (مطوّر الواجهة الخلفية)
- **نصر الله خميس فرج** (مطوّر الواجهة الأمامية)
- **مينا فوزي فهمي** (مطوّر الواجهة الأمامية)
- **مريم عبد الغني عبد المجيد** (مطوّر الواجهة الأمامية)
- **أسماء حلمي السعيد** (مطوّر الواجهة الأمامية)

---

## 📝 الرخصة
هذا المشروع مرخص بموجب [رخصة MIT](LICENSE).
