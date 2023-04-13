# Desc: Temporary Makefile to run the project
provision-local:
	cd terraform && terraform init && terraform apply -auto-approve && cd ..
	export KUBECONFIG=$(pwd)/infra/kindcluster-config
	kubectl get nodes

deploy:
	skaffold run


export-models:
	sqlacodegen --outfile src/models.py sqlite:///services/backend/db.sqlite3

