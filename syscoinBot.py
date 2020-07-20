import mechanize
import re

br = mechanize.Browser()
#br.set_all_readonly(False)    # allow everything to be written to
br.set_handle_robots(False)   # ignore robots
br.set_handle_refresh(False)  # can sometimes hang without this
br.addheaders = [("User-argent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36")]
response = br.open("https://faucet.syscoin.org/")
print(response.read())     # the text of the page
response1 = br.response()  # get the response again
print(response1.read())
for form in br.forms():
    br.select_form(nr=0)         # works when form has a name
    br.form = list(br.forms())[0]  # use when form is unnamed
    for control in br.form.controls:
        control = br.form.find_control("address")

    if control.type == "text":  # means it's class ClientForm.TextControl
        control.value = "sys1qvuncdxpaavf0zu7m96zsr87fsvpnm4zxvpq482"

    response = br.submit()
    mine = "faux"
    while br.geturl() == "https://faucet.syscoin.org/mine":
        mine = "true"
    print("fin")
    mine = "faux"


"""
class syscoinBot:
    def __init__(self):
        self.browser = mechanize.Browser()
        self.browser.addheaders = [("User-argent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36")]

    def connection(self, address):
        self.browser.open("https://faucet.syscoin.org/")
        self.browser.select_form(nr=0)
        self.browser.form["address"] = address
        self.browser.submit()

        if self.browser.geturl() == "https://faucet.syscoin.org/":
            print("IP déjà utilisé")
        else:
            print("Connexion effectuée !")"""