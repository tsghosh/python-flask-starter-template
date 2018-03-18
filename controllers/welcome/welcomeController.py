from flask_restful import Resource

class WelcomeController(Resource):

    def get(self):
        return {"response" : "welcome get"} 
    
    def post(self):
        return {"response" : "welcome post"}

    def put(self):
        return {"response" : "welcome put"}

    def delete(self):
        return {"response" : "welocme delete"}


        
    
