from flask import Flask
import rotas


 
app = Flask(__name__)


app.add_url_rule('/', view_func=rotas.index)
app.add_url_rule('/filtro', view_func=rotas.filtro, methods=['GET', 'POST'])
app.add_url_rule('/agrupamento', view_func=rotas.agrupamento, methods=['GET', 'POST'])
app.add_url_rule('/info', view_func=rotas.info, methods=['GET', 'POST'])
app.add_url_rule('/info/media', view_func=rotas.info, methods=['GET', 'POST'])





app.run(debug=True)