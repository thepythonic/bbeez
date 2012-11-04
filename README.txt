1 Install image library
sudo apt-get install build-dep python-imaging python-dev libjpeg8 libjpeg62-dev libfreetype6 libfreetype6-dev libjpeg8-dev 

2- Install django-cms 
pip install -r reqs/dev.txt

3- Create database
python manage.py syncdb --all

4- Fake migration
python manage.py migrate --fake




