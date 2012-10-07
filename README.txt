1 Install image library
sudo apt-get build-dep python-imaging install python-dev libjpeg8 libjpeg62-dev libfreetype6 libfreetype6-dev libjpeg8-dev install libjpeg62-dev

2- Install django-cms 
pip install -r requirements.txt

3- create new django project

4- Create database
python manage.py syncdb --all

5- Fake migration
python manage.py migrate --fake




