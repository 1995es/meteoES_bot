
class Response(object):
    

    def __init__(self, title, content):
        self.title = title
        self.content = content 

class Location(object):

    def __init__(self, add, lat, lng):
        self.address = add
        self.latitude = lat
        self.longitude = lng