WDIR=pwd
sudo rm /etc/nginx/sites-enabled/default
sudo ln -s $WDIR/etc/nginx.conf  /etc/nginx/sites-enabled/test
sudo /etc/init.d/nginx restart
sudo bash $WDIR/gunicorn_start.sh


