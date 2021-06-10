from flask import Flask
from flask import request, jsonify
from flask_cors import CORS
from flask import render_template
from forms import LoginForm
from config import Config
from mf_code import mf_code
from portfolio import rank_mf_categories, search_string

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    return render_template('base.html', title='Home', user=user)
#     carbrands = [(1, 'Toyota'),
# (2, 'Honda'),
# (3, 'Suzuki'),
# (4, 'Mitsubishi'),
# (5, 'Hyundai')]
#     return render_template('index.html', carbrands=carbrands)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)


@app.route('/dropdown', methods=['GET'])
def dropdown():
    colours = ['Red', 'Blue', 'Black', 'Orange']
    return render_template('dropdown.html', colours=colours)


@app.route('/search', methods=['GET'])
def search():
    carbrands = ['Red', 'Blue', 'Black', 'Orange']
    c1, codes_list = mf_code()
    return render_template('search_test.html', codes_list=codes_list)


@app.route('/rank', methods=['GET'])
def rank():
    ranked_mf = rank_mf_categories("ICICI")
    return render_template('ranked_mf.html', ranked_mf=ranked_mf)

# @app.route("/carbrand",methods=["POST","GET"])
# def carbrand():  
#     if request.method == 'POST':
#         category_id = request.form['category_id'] 
#         print(category_id)  
#         carmodel = []  
#         OutputArray = []
#         for row in carmodel:
#             outputObj = {
#                 'id': row['brand_id'],
#                 'name': row['car_models']}
#             OutputArray.append(outputObj)
#     return jsonify(OutputArray)



app.run(debug = True)