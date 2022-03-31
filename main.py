from flask import Flask, render_template, redirect, request
app = Flask('app')

contacts = [
  { 'title': 'João da Silva'},
  { 'title': 'Maria Souza'}
]

@app.route('/')
def agenda():
  return render_template(
    'agenda.html', 
    contacts=contacts
  )
  
@app.route('/create', methods=['POST'])
def create():
  title = request.form.get('title')
  todos.append({'title': title})
  return redirect('/')
    
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)