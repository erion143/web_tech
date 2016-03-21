sudo rm /etc/nginx/sites-enabled/default
sudo ln -s $PWD/etc/nginx.conf  /etc/nginx/sites-enabled/test
sudo /etc/init.d/nginx restart

sudo ln -s $PWD/etc/gunicorn.conf /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn restart

sudo /etc/init.d/mysql start
mysql -uroot e 'create database qa;'

python $PWD/ask/manage.py migrate

