sudo rm /etc/nginx/sites-enabled/default
sudo ln -s $PWD/etc/nginx.conf  /etc/nginx/sites-enabled/test
sudo /etc/init.d/nginx restart

sudo /etc/init.d/mysql start
mysql -uroot e 'create databse qa'

python $PWD/ask/manage.py migrate

