from flask import Flask, request, jsonify   #importa libreria per api
from pymongo import MongoClient    #importa libreria per mongodb
                                    #doc https://pymongo.readthedocs.io/en/stable/tutorial.html

#connessione database mongo
client = MongoClient('mongodb://mongo-service:27017')   #controlla porta mongoservice!!!!
db = client['mydatabase']
collection = db['mycollection']

#inizializza applicazione flask
app = Flask(__name__)

#def GET items 
@app.route('/api/documents', methods=['GET'])   # poi ricorda sostitutire DOCUMENTS con gli elementi che inserirai tipo macchine,...
def get_documens():
    documents=[]    #documents è la collezzione documenti intera
    for document in collection.find():
        documents.append({'data':document['data']})
    return jsonify(documents)

#def  GET specifc-item
@app.route('/api/documents/<id>', methods=['GET'])
def get_document(identificativo):
    document= collection.find_one({'_id':identificativo}) #non riconosciuto metodo ObjectId
    if document:
        return jsonify({'id': str(document['_id']), 'data': document['data']})
    else:
        return jsonify({'error':'non è stato trovato alcun prodotto con questo id'})
    
#def CREATE new item
@app.route('/api/documents', methods = ['POST'])
def insert_document():
    data = request.json
    result = collection.insert_one({'data':data})
    return jsonify({'id': str(result.inserted_id)})

#def UPDATE item
@app.route('/api/documents/<id>', methods=['PUT'])
def update_document(identificativo):
    data = request.json
    result = collection.update_one({'_id':identificativo}, {'$set': {'data' : data}})  #non riconosciuto metodo ObjectId
    if result.modified_count > 0:
        return jsonify({'id' : identificativo})
    else:
        return jsonify({'error':'documento non trovato nessuna modifica applicata'})
    
#def DELETE item
@app.route('/api/documents/<id>', methods =['DELETE'])
def delete_document(identificativo):
    result= collection.delete_one({'_id':identificativo}) 
    if result.modified_count > 0:
        return jsonify({'id':identificativo})
    else:
        return jsonify({'error': 'documento non trovato, nessu documento eliminato'})
    
#avvia Flask
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)  #si avvia l'applicazione Flask con l'host impostato su '0.0.0.0' e la porta impostata su 3000

