            Eseguire i seguenti comandi per creare cluster e visualizzare modificare aggiungere eliminare risorse:

        crea cluster
kind create cluster

        crea cluster definendo nome 
kind create cluster --name "nome cluster"

        visualizzare cluster
kind get clusters

        per interagire e avere info speciofica nome cluster
kubectl cluster-info --context kind-"nome cluster"

        cancellare cluster
kind delete cluster --name "nome cluster"

        caricare immagine docker nel cluster
kind load docker-image my-custom-image-0 my-custom-image-1 --name "nome cluster"

        PER INTERAGIRE CON KUBERNETES USO:
kubectl command type name flags
    command: specifica operazione : create, get describe, delete
    type: specifica la risorsa pod,pods,po
    name: il nome della risorsa
    flag: spefica la flag opzionale

varie
kubectl get node

kubectl get pod

kubectl get svc

kubectl get all

kubectl get deployments

kubectl get services

kubectl get ingress


            Dopo avre creato/costumizzato cluster passo ad integrazione OPA Gatekeeper:


passi:
1---> installa gatekeeper nel cluster
2--->crea constraint template in REGO
3--->crea constraint CRD
4---> crea deploy e test constraint
5---> ossserva l'enforcement

1	

kubectl apply -f https://raw.githubusercontent.com/open-policy-agent/gatekeeper/master/deploy/gatekeeper.yaml


2	https://kubernetes.io/blog/2019/08/06/opa-gatekeeper-policy-and-governance-for-kubernetes/
dove CRD spec names kind è il nome del temoplate che vogliamo costruire label type items
target per validation
target rego 
una volta creato il template:


3	
creo constraint CRD https://kubernetes.io/blog/2019/08/06/opa-gatekeeper-policy-and-governance-for-kubernetes/
kind riprende il nome del template
audit


implementazione:
https://kubernetes.io/blog/2019/08/06/opa-gatekeeper-policy-and-governance-for-kubernetes/ dal link primo link blu si va su github:
https://github.com/open-policy-agent/gatekeeper
vado su installation
https://open-policy-agent.github.io/gatekeeper/website/docs/install/
controlla di essere amministratore

	kubectl config current-context
	kubectl config view
	kubectl apply -f https://raw.githubusercontent.com/open-policy-agent/gatekeeper/master/deploy/gatekeeper.yaml

controlla

	kubectl get all -n gatekeeper-system

-come usare gatekeeper: 	https://open-policy-agent.github.io/gatekeeper/website/docs/howto

installo per esempio un constraintTemplete 	kubectl apply -f https://raw.githubusercontent.com/open-policy-agent/gatekeeper/master/demo/basic/templates/k8srequiredlabels_template.yaml

	kubectl api-resources 
	kubectl get constrainttemplates
	kubectl describe constrainttemplates

-crea constraint
	kubectl apply -f https://raw.githubusercontent.com/open-policy-agent/gatekeeper/master/demo/basic/constraints/all_ns_must_have_gatekeeper.yaml

sulla base delle constraint template e costraint posso verificare la loro validità  grazie ai test
