
from flask import Flask, render_template,flash, redirect
from forms import NewPetForm

class Pet:
	def __init__(self,id,name,type,price,pic):
		self.id = id
		self.name = name
		self.type = type
		self.price = price
		self.pic = pic

petlist = []
p = Pet(0,"Fluffy","cat",12.99,"fluffy.jpg")
p2 = Pet(1,"Rover","dog", 140.00, "rover.jpg")
p3 = Pet(2,"Cod","fish",0.50,"cod.jpg")

petlist.append(p)
petlist.append(p2)
petlist.append(p3)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

@app.route("/addpet",methods=['GET','POST'])
def addpet():
	addform = NewPetForm()
	if addform.validate_on_submit():
		flash('Adding pet {}, which is a...{}'.format(
			addform.petname.data, addform.pettype.data))
		nextpetid = len(petlist)
		newpet = Pet(nextpetid,addform.petname.data,addform.pettype.data,addform.petprice.data,addform.petpicture.data)
		petlist.append(newpet)
		return redirect('/')
	return render_template("addpet.html",title='Add A Pet!',form=addform)

@app.route("/")
@app.route("/listpets")
def list():
	return render_template("list.html",pets=petlist)

@app.route("/detail/<int:pickapet>")
def detail(pickapet):
	return render_template("detail.html",pet=petlist[pickapet])

if __name__ == "__main__":
	app.run()
