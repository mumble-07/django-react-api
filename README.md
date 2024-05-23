# THIS IS MY NOTES LOOK AWAY >,<
```
##   ##  ##  ###  ##   ##  ### ##   ####     ### ###  
 ## ##   ##   ##   ## ##    ##  ##   ##       ##  ##  
# ### #  ##   ##  # ### #   ##  ##   ##       ##      
## # ##  ##   ##  ## # ##   ## ##    ##       ## ##   
##   ##  ##   ##  ##   ##   ##  ##   ##       ##      
##   ##  ##   ##  ##   ##   ##  ##   ##  ##   ##  ##  
##   ##   ## ##   ##   ##  ### ##   ### ###  ### ###  
```
                                      

`pip install django djangorestframework`
`django-admin startproject <project-name>`
`cd <project-name>`
`django-admin startapp <app-name>`
`python \manage.py makemigrations`
`python manage.py migrate`
`python \manage.py runserver`


1. Create project
2. Create app
3. Create endpoint
4. Create Model
5. Alway make migrations when making changes (on models, endpoints?, etc.)
* 6. Setup API view, this is diff from HTML view (since we're programming backend)


=======================

> add the your app to project --> go to settings

file-path: `A:\GH-Repositories\django-react\music_app\music_app\settings.py`
code: `'api.apps.ApiConfig',`

> this is what you're referencing: 

file-path: `A:\GH-Repositories\django-react\music_app\api\apps.py`
it has a class in it which is the class ApiConfig

> add `'rest_framework`

> go inside api

> views is where you write all of your endpoints
`/hello`
`/home`

e.g. will return response
`def main(request):
return HttpResponse("<h1>Hello World</h1>")`

> configuring URLS/path

create a file in api folder
project urls.py: `A:\GH-Repositories\django-react\music_app\music_app\urls.py`
app urls.py: `A:\GH-Repositories\django-react\music_app\api\urls.py`

e.g. `path('api/', include('api.urls'))`

> models
`A:\GH-Repositories\django-react\music_app\api\models.py`

Room Models > where people can host and others can join and control music

Create serializers.py 
It will take the model and translate it into a json response.
serializer: `A:\GH-Repositories\django-react\music_app\api\serializers.py`
in fields include what fields you want to serialize

Primary key > unique integer automatically created 

Go to view and add the class RoomView (allow us to view and create a room)

Go to URLS
now we import the RoomView class


> ADDING REACT/FRONTEND

cd music_app
npm

create new app inside the project
`django-admin startapp frontend`
cd frontend
create new folders
folder: 
* templates
*static > all static files
- frontend > bundle of all javascript
- css
- images
*src 
- components

inside frontend 
`npm init -y`

next is install bunch of stuff in npm

**⌨ NPM Setup Commands ⌨**
```npm init -y```
```npm i webpack webpack-cli --save-dev```
```npm i @babel/core babel-loader @babel/preset-env @babel/preset-react --save-dev```
```npm i react react-dom --save-dev```
```npm install @material-ui/core```
```npm install @babel/plugin-proposal-class-properties```
```npm install react-router-dom```
```npm install @material-ui/icons```


=====================


create babel file: `A:\GH-Repositories\django-react\music_app\frontend\babel`
next create anopther file: 
webpack.config.js

what webpack does is bundle all js and makes a bundle into 1 file.
`A:\GH-Repositories\django-react\music_app\frontend\webpack.config.js`

