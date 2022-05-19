from flask import Flask, render_template, redirect, request
app = Flask('app')

contacts = [
  { 'name': 'João da Silva', },
  { 'name': 'Maria Souza', }
]

@app.route('/')
def agenda():
  return render_template(
    'agenda.html', 
    contacts=contacts
  )
  
@app.route('/create', methods=['POST'])
def create():
  name = request.form.get('name')
  email = request.form.get('email')
  phone = request.form.get('phone')
  contacts.append({'name': name, 'email': email, 'phone': phone, 'complete':False} )
  return redirect('/')

@app.route('/delete/<int:agenda>')
def delete(agenda):
 contacts.pop(agenda)
 return redirect('/')

@app.route('/complete/<int:agenda>')
def complete(agenda):
 contacts[agenda]['complete'] = True
 return redirect('/')

@app.route('/update/<int:agenda>', methods=['POST'])
def update(agenda):
 name = request.form.get('name')
 email = request.form.get('email')
 phone = request.form.get('phone')
 contacts[agenda]['name'] = name
 return redirect('/')


    
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)