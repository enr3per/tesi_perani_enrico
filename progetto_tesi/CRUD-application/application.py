from flask import Flask, request, jsonify   #importa libreria per api
from pymongo import MongoClient    #importa libreria per mongodb
                                    #doc https://pymongo.readthedocs.io/en/stable/tutorial.html
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import socket


#inizializza applicazione flask
app = Flask(__name__)


#connessione database mongo
#client = MongoClient('mongodb://mongo-service:27017')   #controlla porta mongoservice!!!!
#client = MongoClient("mongodb://localhost:27017/")  #funziona per test oddia se app.py runna in locale
#db = client['mydatabase']
#collection = db['mycollection']

#seconda connessione non locale ma per k8s 
app.config["MONGO_URI"] = "mongodb://mongo:27017/dev"
#app.config["MONGO_URI"] = "mongodb://localhost:27017/dev"
client = PyMongo(app)
db = client.db
collection = db

#verifico funzionamento su porta 5000********************************DA CANCELLARE***********************
@app.route('/')
def index():
    return 'This Application Works correctly!'
    

@app.route('/documents/mycollection', methods=['GET'])
def index_get_all():
    return 'GET ALL works!'

@app.route('/documents/mycollection/<id>', methods=['GET'])
def index_get(id):
    return jsonify('GET works!',id)

@app.route('/documents/mycollection', methods=['POST'])
def index_post():
    return 'POST works!'

@app.route('/documents/mycollection/<id>', methods=['PUT'])
def index_update(id):
    return jsonify('PUT works!',id)
   

@app.route('/documents/mycollection/<id>', methods=['DELETE'])
def index_delete(id):
    return jsonify('Delete works',id)
#***********************************SEMBRA FUNZIONARE CORRETTAMENTE*****************************************************

#def PROVA --->FUNZIONA
@app.route('/api/documents', methods=['VIEW'])
def prova():
    return jsonify("la connessione con il database funziona correttamente")


#def GET items --->FUNZIONA
@app.route('/api/documents', methods=['GET'])   # poi ricorda sostitutire DOCUMENTS con gli elementi che inserirai tipo macchine,...
def get_documents():
    documents=[]    #documents è la collezzione documenti intera
    for document in collection.find():
        documents.append({"nome" : document["nome"],
                          "cognome":document["cognome"],
                          "data_nascita":document["data_nascita"],
                          "id":document["id"],
                          "email":document["email"],
                          "dipartimento": document["dipartimento"]})
    documents_sorted= sorted(documents,key=lambda p :p['id'])        
    return jsonify(documents_sorted= documents_sorted)
    

#def  GET specifc-item  --->FUNZIONA
@app.route('/api/documents/<id>', methods=['GET'])
def get_one_document(id):
    documents=[]
    document = collection.find_one({"id":id}) #non riconosciuto metodo ObjectId
    if document:
        documents.append({"nome" : document["nome"],
                          "cognome":document["cognome"],
                          "data_nascita":document["data_nascita"],
                          "id":document["id"],
                          "email":document["email"],
                          "dipartimento": document["dipartimento"]})
        return jsonify(documents)
    else:
        return jsonify({'error':'non è stato trovato alcun prodotto con questo id'})
    
#def CREATE new item    --->FUNZIONA
@app.route('/api/documents', methods = ['POST'])    #/api/documentes/<id> convenzione ! da cambiare
def insert_document():
    data = request.json
    result = collection.insert_one({'data':data})
    return jsonify({'id': str(result.inserted_id)})

#def UPDATE item    ---> FUNZIONA
@app.route('/api/documents/<id>', methods=['PUT'])
def update_document(id):
    data = request.json
    result = collection.update_one({'id':id}, {'$set': {'data' : data}})  #non riconosciuto metodo ObjectId
    if result.modified_count > 0:
        return jsonify({'id' : id})
    else:
        return jsonify({'error':'documento non trovato nessuna modifica applicata'})
    
#def DELETE item --->FUNZIONA
@app.route('/api/documents/<id>', methods =['DELETE'])
def delete_document(id):
    result= collection.delete_one({'id':id}) 
    #if result.modified_count > 0:
    if result.deleted_count > 0:
        return jsonify({'id':id})
    else:
        return jsonify({'error': 'documento non trovato, nessu documento eliminato'})
    

if __name__ == '__main__':
    app.run(host='0.0.0.0' , port =5000)  #si avvia l'applicazione Flask con l'host impostato su '0.0.0.0' e la porta impostata su 5000
    #app.run(debug=True, host='0.0.0.0', port=5000)