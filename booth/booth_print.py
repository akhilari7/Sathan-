from flask import Flask, render_template, request
from bitstring import BitArray

def booth(m,r):
	 x = len(bin(m))
	 y = len(bin(r))
	 
	 if m < 0 and r < 0 or r < 0 :
	 	bugbit = 1                  
	 else:
		bugbit = 0
	 totalLength = x+y+1
	 A = BitArray(int = m, length = totalLength) << (y+1)	
	 compliment = BitArray(int = -m, length = totalLength) << (y+1) 
	 P = BitArray(int = r, length = totalLength)  
	 P = P << 1									
	 for i in range(1,y+1):  
	 	if P[-2:] == '0b01': 
	 		P = BitArray(int = P.int + A.int, length = totalLength)
	 	elif P[-2:] == '0b10': 
	 		P = BitArray(int = P.int +compliment.int, length = totalLength)
	 	P = BitArray(int=P.int >> 1,length=totalLength) 
	 P = P[:-1]	
	 P.int = P.int + bugbit
	 return '<h1>RESULT</h1><br><h3>decimal value: '+str(P.int)+'</br><br> binary value: '+str(P.bin)


# flask starts here

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')


@app.route('/', methods = ['POST'])
def my_form_post():
	r = request.form['Multiplier']
	m = request.form['Multiplicand']
	try:
		multiplicand = int(m)
		multiplier = int(r)
	except:
		return "<h1>ERROR</h1><br>Only one item for multiplication of two found"
	print multiplicand, multiplier
	return booth(multiplicand, multiplier)

if __name__ == '__main__':
    #app.debug = True
    app.run(debug = True)	
