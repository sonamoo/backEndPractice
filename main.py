#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import os
import jinja2
import webapp2
import string


template_dir = os.path.join(os.path.dirname(__file__), 'template')
# os.path.join concatenates the current location and the template directory ex ) /__file__/template
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
							   autoescape = True)


class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

	def render_str(self, template, **params):
		t = jinja_env.get_template(template)
		return t.render(params)

	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))


class rot13(Handler):

	def rot13_function(self, str): 

		tab1 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
		tab2 = 'nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM'
		tab = string.maketrans(tab1, tab2)

		translated_string = str.translate(tab)
		return translated_string

	def get(self):
		self.render('rot13.html')

	def post(self):
		sss = self.request.get('text')
		if sss :
			sss = str(sss)
		show_string = self.rot13_function(sss)
		self.render('rot13.html', text = show_string)


	
app = webapp2.WSGIApplication([('/', rot13)], debug=True)
