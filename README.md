# Tạo trang xác thực người dùng với Django

Xem chi tiết bài viết tại [Tạo trang xác thực người dùng với Django ]()


## Cài đặt

Đầu tiên, tải repository về máy tính:

```bash
git clone http://github.com/djangobat/django-authentication.git
```

Cài đặt requirements:

```bash
cd django-authentication
pip install -r requirements.txt
```

Tạo database:

```bash
python manage.py makemigrations users
python manage.py migrate
```

Chạy development server:

```bash
python manage.py runserver
```

Mở Chrome hay FireFox : **127.0.0.1:8000**



