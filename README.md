# coffee-email-service


1. kubectl apply -f k8s/namespace.yaml

2. kubectl create secret generic coffee-email-secrets --from-env-file=.env -n email-dev

3. kubectl apply -f k8s/api -n email-dev
