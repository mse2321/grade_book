#!/usr/bin/env python

Site = 'Demo Signup Form'

Timezone = 'Pacific/Honolulu'

Colors = '''
    base03:    #002b36;
    base02:    #073642;
    base01:    #586e75;
    base00:    #657b83;
     base0:    #839496;
     base1:    #93a1a1;
     base2:    #eee8d5;
     base3:    #fdf6e3;
    yellow:    #b58900;
    orange:    #cb4b16;
       red:    #dc322f;
   magenta:    #d33682;
    violet:    #6c71c4;
      blue:    #268bd2;
      cyan:    #2aa198;
     green:    #859900;
''' # - http://ethanschoonover.com/solarized

Analytics = '''<script>


</script>'''


# - HTML Page Code

main_page_html = '''<style>

</style>
<div class="page_html">
 <header class="hi"><span class="color_b">Hello</span></header>

</div><!-- - /page_html - -->'''

form_page_html = '''<style>
.form_wrap { margin-left: 55px; margin-top: 35px; outline: 1px solid #eee; width: 345px; padding: 45px; }
tr { height: 32px; }
td.label { font-size: 14px; text-align: right; padding-right: 10px; }
input[type="text"] { width: 200px; height: 16px; }
</style>
<div class="page_html">
 <header class="hi"><span class="color_b">Fill Out The Form</span></header>
  <article class="form_wrap">
    <form action="../../add_grade" enctype="multipart/form-data" method="post">
      <table>
        <tr>
          <td class="label">Student Name</td>
          <td class="input"><input type="text" name="student_name" /></td>
        </tr>
        <tr>
          <td class="label">Class Grade</td>
          <td class="input"><input type="text" name="class_grade" /></td>
        </tr>
        <tr>
          <td></td>
          <td style="text-align:right"><input type="submit" value="Add Grade" /></td>
        </tr>
      </table>
    </form>
  </article><!-- - /form_wrap - -->
</div><!-- - /page_html - -->'''


entries_page_html = '''<style>
.text_wrap { margin-left: 65px; }
</style>
<div class="page_html">
 <header class="hi"><span class="color_b">Form Entries</span></header>
  <article class="text_wrap">
    <p>Sign in as an &nbsp; <b><span class="color_a">Admin User</span></b> &nbsp; to view form data</p>
  </article><!-- - /form_wrap - -->
</div><!-- - /page_html - -->'''


entries_page_html_admin = '''<style>
.list_wrap { margin-left: 25px; margin-top: 45px; }
.item_wrap { width: 400px; border-bottom: 1px solid #eee; padding: 15px; padding-bottom: 10px; margin-top: 45px; }
.item_wrap:hover { border-bottom: 1px solid #657b83; }
.right_wrap { float: right; text-align: right; font-size: 12px; }
.right_wrap a { color: #cb4b16; }
.right_wrap a:hover { text-decoration: underline; }
.id_wrap { padding-top 40px; color: #839496; }
.email_address { font-size: 14px; line-height: 20px; }
.user_name { font-size: 22px; color: #073642; }
</style>
<div class="page_html">
 <header class="hi"><span class="color_b">Form Entries</span></header>
  <article class="list_wrap">
    <div class="item_wrap" ng-repeat="item in items">
      <div class="item_data">

        <div class="right_wrap">
          <p><a href ng-click="delete(item.data_id)">Delete</a></p>
          <div class="id_wrap">[!item.data_id!]</div>
        </div><!-- - /right_wrap - -->

        <p><span class="email_address">[!item.student_name!]</span>
        <br />
        <span class="user_name">[!item.class_grade!]</span></p>
        
      </div><!-- - /item_data - -->
    </div><!-- - /item_data - -->
  </article><!-- - /list_wrap - -->
</div><!-- - /page_html - -->'''


code_page_html = '''<style>
.link_wrap { margin-left: 85px; margin-top: 45px; }
</style>
<div class="page_html">
 <header class="hi"><span class="color_b">Code Link</span></header>
  <div class="link_wrap">
    <p>View on &nbsp; <a href="https://github.com/Kyle2501/App-Engine-Parts" target="_blank">GitHub</a></p>
  </div><!-- - /link_wrap - -->
</div><!-- - /page_html - -->'''

settings_page_html = '''<style>
.form_wrap { margin-left: 55px; margin-top: 35px; outline: 1px solid #eee; width: 345px; padding: 45px; }
tr { height: 32px; }
td.label { font-size: 14px; text-align: right; padding-right: 10px; }
input[type="text"] { width: 200px; height: 16px; }
</style>
<div class="page_html">
 <header class="hi"><span class="color_b">Fill Out The Form</span></header>
  <article class="form_wrap">
    <form action="../../add_settings" enctype="multipart/form-data" method="post">
      <table>
        <tr>
          <td class="label">User Name</td>
          <td class="input"><input type="text" name="user_name" /></td>
        </tr>
        <tr>
          <td class="label">Background Color</td>
          <td class="input">
            <input type="text" name="bg_color" />
            <div class="draw_colors"></div>
          </td>
        </tr>
        <tr>
          <td class="label">Profile Image</td>
          <td class="input"><input type="file" name="profile_img" /></td>
        </tr>
        <tr>
          <td></td>
          <td style="text-align:right"><input type="submit" value="Save" /></td>
        </tr>
      </table>
    </form>
  </article><!-- - /form_wrap - -->
</div><!-- - /page_html - -->

<script>

  // Stroke Color Selector: 

    var ColorPicker = function (defaultColor, colorScale) {
    var self = this;
    var rainbow = ["#FFD300", "#FFFF00", "#A2F300", "#00DB00", "#00B7FF", "#1449C4", "#4117C7", "#820AC3", "#DB007C", "#FF0000", "#FF7400", "#FFAA00"];
    colorScale = colorScale || rainbow;
    var color = function (i) {
        return colorScale[i];
    };
    defaultColor = defaultColor || color(0);

    self.pickedColor = defaultColor;
    self.picked = function (color) {};
    var clicked = function () {
        self.picked(self.pickedColor);
    };

    var chooseColor = function () {
      strokeColor = self.picked(self.pickedColor);
    }

    var pie = d3.layout.pie().sort(null);
    var arc = d3.svg.arc().innerRadius(50).outerRadius(105);

    var svg = d3.select(".draw_colors")
        .append("svg")
        .attr("width", 500)
        .attr("height", 500)
        .append("g")
        .attr("transform", "translate(150,120)");

    var plate = svg.append("circle")
        .attr("fill", defaultColor)
        .attr("stroke", "#fff")
        .attr("stroke-width", 4)
        .attr("r", 75)
        .attr("cx", 0)
        .attr("cy", 0)
        .on("click", clicked)
        .on("click", chooseColor);

    svg.datum([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
        .selectAll("path")
        .data(pie)
        .enter()
        .append("path")
        .attr("fill", function (d, i) {
        return color(i);
    })
        .attr("stroke", "#fff")
        .attr("stroke-width", 4)
        .attr("d", arc)
        .on("mouseover", function () {
        var fill = d3.select(this).attr("fill");
        self.pickedColor = fill;
        plate.attr("fill", fill);
    })
        .on("click", clicked);
  };

</script>


'''


# - System
import os
import urllib
import wsgiref.handlers
import webapp2
import json
# - 
from google.appengine.api import users
from google.appengine.api import mail
from google.appengine.api import images
# -
from google.appengine.ext import db
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
# -
from urlparse import urlparse
# -
import time
import datetime
from pytz.gae import pytz



class User_db(db.Model):
    addTime = db.DateTimeProperty(auto_now_add=True)
    data_id = db.StringProperty()
  #
    user_name = db.StringProperty()
    bg_color = db.StringProperty()
    profile_img = db.BlobProperty()


class addUser_db(webapp2.RequestHandler):
    def post(self):
        date_time = datetime.datetime.now(pytz.timezone(Timezone)).strftime("%Y%m%d_%H%M%S")
        data_id = date_time
        item = User_db(key_name=data_id)
        item.data_id = data_id
      # - -
        item.user_name = self.request.get('user_name')
        item.bg_color = self.request.get('bg_color')
        profile_img = self.request.get('profile_img')

        if profile_img:
          item.profile_img = images.resize(profile_img, 800, 600)
      #
        item.put()
        time.sleep(1)
        self.redirect('/settings')




class Grade_db(db.Model):
    addTime = db.DateTimeProperty(auto_now_add=True)
    data_id = db.StringProperty()
  #
    student_name = db.StringProperty()
    class_grade = db.StringProperty()



    email_address = db.StringProperty()
    email_address = db.StringProperty()
    email_address = db.StringProperty()
    email_address = db.StringProperty()
    email_address = db.StringProperty()




class addGrade_db(webapp2.RequestHandler):
    def post(self):
        date_time = datetime.datetime.now(pytz.timezone(Timezone)).strftime("%Y%m%d_%H%M%S")
        data_id = date_time
        item = Grade_db(key_name=data_id)
        item.data_id = data_id
      # - -
        item.student_name = self.request.get('student_name')
        item.class_grade = self.request.get('class_grade')
      #
        item.put()
        time.sleep(1)
        self.redirect('/entries')

class deleteData(webapp2.RequestHandler):
    def get(self):
        page_address = self.request.uri
        base = os.path.basename(page_address)
        data_id = base.split('?')[1]
        if users.is_current_user_admin():
            item = db.Query(Grade_db).filter('data_id =', data_id).get()
        item.delete()
        time.sleep(1)
        self.redirect('../../list/entries')


intro_html = '''
  <style>
    body { font-family: 'Arial', sans-serif; }
    #intro_wrap { background-color: green; color: white; text-align: center; }
  </style>
  <div id="intro_wrap">

  <header>
    <img src="#" alt="#" />
  </header>
  <section>
    <h1>GradeBook</h1>
    <p>tagline</p>
    <div class="button_wrap">
      <button>Login</button>
    </div>
  </section>
  <footer>
    <p>&copy;2016 ME Innovation</p>
  </footer>

</div> <!-- end of intro_wrap -- >
'''
dashboard_html = '''
  <div id="dashboard_wrap">
  
  <section>
    <button class="dash_button"></button>
    <p>Reporting</p>
    <button class="dash_button"></button>
    <p>Grade Entry</p>
    <button class="dash_button"></button>
    <p>Settings</p>
    <button class="dash_button"></button>
    <p>Import</p>
  </section>
  <footer>
    <h2>GradeBook</h2>
    <nav id="profile_nav">
      <ul>
        <li>item</li>
        <li>item</li>
        <li>item</li>
        <li>item</li>
      </ul>
    </nav>
    <div id="profile_wrap">
      <img src="#" alt="#" />
    </div>
  </footer>

</div> <!-- end of dashboard_wrap -- >
'''

grades_html = '''
  <div id="grade_wrap">

  <header>
    <h1>Category</h1>
  </header>
  <section>
    <table>
      <tbody>
        <tr>
          <td>Sample 1</td>
          <td>Sample 2</td>
        </tr>
      </tbody>
    </table>
    <button id="sensor_button"></button>
    <nav id="content_nav">
      <ul>
        <li>item</li>
        <li>item</li>
        <li>item</li>
        <li>item</li>
      </ul>
    </nav>
  </section>
  <footer>
    <h2>GradeBook</h2>
    <nav id="profile_nav">
      <ul>
        <li>item</li>
        <li>item</li>
        <li>item</li>
        <li>item</li>
      </ul>
    </nav>
    <div id="profile_wrap">
      <img src="#" alt="#" />
    </div>
  </footer>

</div> <!-- end of grade_wrap -->


<style>
.list_wrap { margin-left: 25px; margin-top: 45px; }
.item_wrap { width: 400px; border-bottom: 1px solid #eee; padding: 15px; padding-bottom: 10px; margin-top: 45px; }
.item_wrap:hover { border-bottom: 1px solid #657b83; }
.right_wrap { float: right; text-align: right; font-size: 12px; }
.right_wrap a { color: #cb4b16; }
.right_wrap a:hover { text-decoration: underline; }
.id_wrap { padding-top 40px; color: #839496; }
.email_address { font-size: 14px; line-height: 20px; }
.user_name { font-size: 22px; color: #073642; }
</style>
<div class="page_html">
 <header class="hi"><span class="color_b">Form Entries</span></header>
  <article class="list_wrap">
    <div class="item_wrap" ng-repeat="item in items">
      <div class="item_data">

        <div class="right_wrap">
          <p><a href ng-click="delete(item.data_id)">Delete</a></p>
          <div class="id_wrap">[!item.data_id!]</div>
        </div><!-- - /right_wrap - -->

        <p><span class="email_address">[!item.student_name!]</span>
        <br />
        <span class="user_name">[!item.class_grade!]</span></p>
        
      </div><!-- - /item_data - -->
    </div><!-- - /item_data - -->
  </article><!-- - /list_wrap - -->
</div><!-- - /page_html - -->


'''

login_html = '''
  <div id="login_wrap">

  <header>
    <h1>GradeBook</h1>
  </header>
  <section>
    <input type="text" name="username" placeholder="User Name">
    <input type="text" name="password" placeholder="Password">
    <button type="submit">Submit</button>
  </section>
  <footer>
    <p>&copy;2016 ME Innovation</p>
  </footer>

</div> <!-- end of login_wrap -- >
'''

import_html = '''
  <div id="import_wrap">

  <header>
    <h1>GradeBook</h1>
  </header>
  <section>

  </section>
  <footer>
    <p>&copy;2016 ME Innovation</p>
  </footer>

</div> <!-- end of import_wrap -- >
'''

settings_html = '''
  <div id="settings_wrap">

  <header>
    <h1>GradeBook</h1>
  </header>
  <section>

  </section>
  <footer>
    <p>&copy;2016 ME Innovation</p>
  </footer>

</div> <!-- end of settings_wrap -- >
'''

class RenderImg(webapp2.RequestHandler):
    def get(self):
        page_address = self.request.uri
        base = os.path.basename(page_address)
        data_set = base.split('?')[1]
        img_size = base.split('?')[2]
        data_id = base.split('?')[3]

        if data_set == 'user':
          item = User_db.get_by_id(data_id)
          img = images.Image(item.profile_img)

        if img_size == 'thumb':
            img.resize(width=100)
        if img_size == 'small':
            img.resize(width=250)
        if img_size == 'medium':
            img.resize(width=450)
        if img_size == 'large':
            img.resize(width=700)
        image = img.execute_transforms(output_encoding=images.JPEG)
        self.response.headers['Content-Type'] = 'image/jpeg'
        self.response.out.write(image)

class publicSite(webapp2.RequestHandler):
    def get(self):
      # - page url
        page_address = self.request.uri
        path_layer = urlparse(page_address)[2].split('/')[1]
        base = os.path.basename(page_address)
      # - user
        user = users.get_current_user()
        if users.get_current_user(): # - logged in
          login_key = users.create_logout_url(self.request.uri)
          gate = 'Sign out'
          user_name = user.nickname()
        else: # - logged out
          login_key = users.create_login_url(self.request.uri)
          gate = 'Sign in'
          user_name = 'No User'
      # - app data
        app = Site
        page_name = 'Main'
        page_id = 'main'
        analytics = Analytics
        page_html = main_page_html
        admin = ''
        if users.is_current_user_admin():
            admin = 'true' 

        if path_layer == 'form':
            page_id = 'form'
            page_name = 'Form'
            page_html = form_page_html

        if path_layer == 'entries':
            page_id = 'entries'
            page_name = 'Entries'
            if admin == 'true':         
                page_html = entries_page_html_admin #!
            else:
                page_html = entries_page_html

        if path_layer == 'code':
            page_id = 'code'
            page_name = 'Code'
            page_html = code_page_html



        if path_layer == 'intro':
            page_id = 'intro'
            page_name = 'Intro'
            page_html = intro_html

        if path_layer == 'dashboard':
            page_id = 'dashboard'
            page_name = 'Dashboard'
            page_html = dashboard_html

        if path_layer == 'grades':
            page_id = 'grades'
            page_name = 'Grades'
            page_html = grades_html

        if path_layer == 'login':
            page_id = 'login'
            page_name = 'Login'
            page_html = login_html

        if path_layer == 'import':
            page_id = 'import'
            page_name = 'Import'
            page_html = import_html

        if path_layer == 'settings':
            page_id = 'settings'
            page_name = 'Settings'
            page_html = settings_page_html
               
      # - template
        objects = {
            'Site': app,
            'analytics': analytics,
            'login_key': login_key,
            'gate': gate,
            'user_name': user_name,
            'admin': admin,
          # -
            'path_layer': path_layer,
            'base': base,
            'page_name': page_name,
            'page_id': page_id,
            'page_html': page_html,
            
        }
      # - render
        path = os.path.join(os.path.dirname(__file__), 'html/publicSite.html')
        self.response.out.write(template.render(path, objects))


class listData(webapp2.RequestHandler):
    def get(self):
        page_address = self.request.uri
        base = os.path.basename(page_address)
        if users.is_current_user_admin():
            if base == 'grades':
                q = db.Query(Grade_db, projection=('data_id', 'student_name', 'class_grade'))
                db_data = q.order('-addTime').fetch(50)
        data = []
        for f in db_data:
            data.append(db.to_dict(f))
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(data))


app = webapp2.WSGIApplication([    # - Pages
    ('/', publicSite),
    ('/form/?', publicSite),
      ('/add_grade/?', addGrade_db),
      ('/add_settings/?', addUser_db),
      ('/delete/data/?', deleteData),
    ('/entries/?', publicSite),
      ('/list/grades/?', listData),

    ('/login/?', publicSite),
    ('/intro/?', publicSite),
    ('/dashboard/?', publicSite),
    ('/grades/?', publicSite),
    ('/import/?', publicSite),
    ('/settings/?', publicSite)


], debug=True)

