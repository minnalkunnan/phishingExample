import web

urls = (
   '/', 'index', 
   '/', 'templates'
)

render = web.template.render('templates/')

class index:
   def GET(self):
      return render.calpoly()

if __name__ == "__main__":
   app = web.application(urls, globals())
   app.run()
