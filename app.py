from flask import Flask, redirect, render_template, request, session, url_for
app = Flask(__name__)
app.config["SECRET_KEY"] = 'secret_key'
@app.route('/', methods=['GET', 'POST']) 
def index(): 
    if request.method == 'POST':
      amount = float(request.form['amount']) 
      option = request.form['option'] 

      if option == 'イートイン':
        tax_rate = 0.10
      elif option =='テイクアウト':
        tax_rate = 0.08
      else:
        tax_rate = 0.0
       
      tax=amount * tax_rate
      total = amount + tax

      session['amount'] = amount
      session['option'] = option
      session['total'] = round(total,2)
    
      return redirect(url_for('result'))
    return render_template('index.html')
@app.route('/result') 
def result(): 
  return render_template('result.html')
 
if __name__ == '__main__':
  app.run(debug=True,port=7777)

