import tornado.web
import tornado.ioloop

file_path = "Text FIle\accounts.txt"  # Replace with the actual path of your text file
accounts = []

def readTF():
    with open(file_path, "r") as file:
        headings = file.readline().strip().split("\t")  # Read and split the first line (headings)
        for line in file:
            values = line.strip().split("\t")  # Split the line into values
            row_dict = dict(zip(headings, values))  # Create a dictionary using headings as keys
            accounts.append(row_dict)  # Add the dictionary to the array
    return accounts
class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("web\login.html")

    def post(self):
        log_username = self.get_argument("log_username")
        log_password = self.get_argument("log_password")

        if log_username == "admin23" and log_password == "admin23":
            self.redirect("/admin")  # Redirect to the admin page
        else:
            self.write("Invalid login credentials")  # Handle invalid credentials


class SignUpHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("web\signup.html")

    def post(self):
        first_name = self.get_argument("firstname")
        last_name = self.get_argument("lastname")
        phone_number = self.get_argument("phonenumber")
        email = self.get_argument("email")
        reg_username = self.get_argument("reg_username")
        reg_password = self.get_argument("reg_password")
        reg_conf_password = self.get_argument("reg_conf_password")



class AdminHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("web\database.html")

class JobOpenings(tornado.web.RequestHandler):
    def get(self):
        self.render("web\index.html")

def make_app():
    return tornado.web.Application([
        (r"/", LoginHandler),
        (r"/signup", SignUpHandler),
        (r"/admin", AdminHandler),
        (r"/index", JobOpenings),
    	(r"/web/static/(.*)", tornado.web.StaticFileHandler, {"path": "web/static"}),
    ])

if __name__ == "__main__":
    readTF()
    app = make_app()
    app.listen(7784)
    print("sum on port 7784")
    tornado.ioloop.IOLoop.current().start()
