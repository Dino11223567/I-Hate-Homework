#WHY YOU NO WORK PYTHON

#Imports
import urllib.request
import urllib.parse
import re, time
from robobrowser import RoboBrowser

#Suppose to login into MathXL (THIS PART DOESN"T WORK)
br = RoboBrowser()
br.open('https://www.mathxlforschool.com/login_school.htm')
form = br.get_form()
form['username'] = "USERNAME"
form['password'] = "PASSWORD"
br.submit_form(form)

src = str(br.parsed())
print(src)

#Suppose to give me the average
start = '<span class="score-value">'
end = "</span>"
result = re.search('%s(.*)%s' % (start,end), src).group(1)
print("Result: " + result)

time.sleep(15)
