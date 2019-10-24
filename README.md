
# NSFW classification for URLS

__Technologies__

- Keras (Tensorflow)
- Flask
- Can be deployed to Heroku
- Uses RENDERTRON headless browser service for image extreaction.

__Model__

This version I only uploaded trained model(.h5). Code doesn't contain how  to train. I will release in next commit
- Trained on data generated in my PC
- Been through 3 epochs only
- 95% accuracy on almost all websites
- Needs documentation.


__Deployment__

LINUX:
```sh
pip install -r requirements.txt
python app.py 
firefox http://127.0.0.1:5000
```
WINDOWS:
```cmd ( as admin)
pip install -r requirements.txt
python app.py
http://127.0.0.1:5000 ( in fav browser)
