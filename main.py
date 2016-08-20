import cherrypy

class Core(object):
    @cherrypy.expose
    def index(self):
        return open("src/templates/index.html","r").read().format("TITU", "PARA")

if __name__ == '__main__':
    cherrypy.quickstart(Core())
