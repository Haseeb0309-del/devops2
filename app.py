from flask import flask,request,render_template
app=Flask(_name_)
@app.route["/register":methods=['GET','POST']]
def register():
if request.method=='POST':
name=request.Form['name']
email=request.Form['email']
password=request.form['password']
return.render_template('success.html')
return.render_template('register.html')
if_name_='_main_';
app.run(host='0.0.0.0')