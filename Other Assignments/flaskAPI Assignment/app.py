from flask import Flask,render_template,request
from json import load

app = Flask(__name__)

try:
    with open('items.json') as f:
        items = load(f)

except FileNotFoundError:
    items={}


@app.route('/home/' , methods=['GET','POST'])
@app.route('/' , methods=['GET','POST'])
def home():
    return render_template('home.html',items=items)


@app.route('/cart',methods=['POST'])
def cartTotal():
    if request.method=='POST':
        Qty=dict()
        total=int()

        for item in items:
            if request.form[item] not in ('0',''):
                Qty[item]=int(request.form[item])
                total += Qty[item] * items[item]

        discount=0
        if 0<total<=100000:
            discount=10
        elif 100000<total<=200000:
            discount=20
        elif total>200000:
            discount=30

        return render_template('cart.html', Qty=Qty, items=items,
                               total=total, discount=discount)        

if __name__=='__main__':
    app.run()