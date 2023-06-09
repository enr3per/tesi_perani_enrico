from flask import Flask, request, jsonify   
from pymongo import MongoClient    #ihttps://pymongo.readthedocs.io/en/stable/tutorial.html
                                  

#inizializza  flask
app = Flask(__name__)

#connessione database mongo
client = MongoClient('mongodb://mongo-service:27017')   #connessione docker
#client = MongoClient("mongodb://localhost:27017/")  #fconnessione locale
db = client['mydatabase']
collection = db['mycollection']


#verifico funzionamento su porta 5000********************************DA CANCELLARE***********************
@app.route('/')
def index():
    return 'App Works!'
    

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

#def PROVA
@app.route('/api/documents', methods=['VIEW'])
def prova():
    return jsonify("la connessione con il database funziona correttamente")


#def GET items --->FUNZIONA
@app.route('/api/documents', methods=['GET'])   
def get_documents():
    documents=[]    
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
    document = collection.find_one({"id":id}) 
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
    result = collection.update_one({'id':id}, {'$set': {'data' : data}})  
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
    
#avvia Flask    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # avvia l'app host impostato su '0.0.0.0' e la porta su 5000
    

