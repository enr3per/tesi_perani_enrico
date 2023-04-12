creare l'immagine Docker dell'applicazione eseguendo il comando:
    docker build -t myapp:v1

Il punto alla fine del comando indica che la build deve essere effettuata nella directory corrente.
una volta completata la build dell'immagine Docker, puoi eseguire l'applicazione all'interno di un container Docker eseguendo il comando:
    docker run -p 5000:5000 myapp:v1
    
Dove "5000:5000" indica che la porta 5000 del container deve essere mappata sulla porta 5000 della macchina host.
