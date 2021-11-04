
from flask import Flask, render_template,flash, redirect
from forms import NewClothingForm

class clothing:
	def __init__(self,id,brand,type,price,pic,size):
		self.id = id
		self.brand = brand
		self.type = type
		self.price = price
		self.pic = pic
		self.size = size
clothinglist = []
c = clothing(0,"Gucci","Shirt",200.00,"GucciShirt.jpg","Large")
c2 = clothing(1,"Nike","Shorts",55.00, "NikeShorts.jpg","Medium")
c3 = clothing(2,"Wrangler","Jeans",20.00, "WranglerJeans.jpg","Small")
c4 = clothing(3,"North Face","Hoodie",90.00, "NorthfaceHoodie.jpg","Medium")

clothinglist.append(c)
clothinglist.append(c2)
clothinglist.append(c3)
clothinglist.append(c4)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

@app.route("/addclothing",methods=['GET','POST'])
def addclothing():
	addform = NewClothingForm()
	if addform.validate_on_submit():
		flash('Adding clothing {}, which is a...{}'.format(
			addform.clothingbrand.data, addform.clothingtype.data))
		nextclothingid = len(clothinglist)
		newclothing = clothing(nextclothingid,addform.clothingbrand.data,addform.clothingtype.data,addform.clothingprice.data,addform.clothingpic.data)
		clothinglist.append(newclothing)
		return redirect('/')
	return render_template("addclothing.html",title='Add A Piece Of Clothing!',form=addform)

@app.route("/")
@app.route("/listclothing")
def list():
	return render_template("list.html",clothes=clothinglist)

@app.route("/detail/<int:pickclothes>")
def detail(pickclothes):
	return render_template("detail.html",clothes=clothinglist[pickclothes])

if __name__ == "__main__":
	app.run()
