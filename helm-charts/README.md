# How-to Guide

## Deploy NGINX-ingress
```shell
kubectl create ns nginx-system
kubens nginx-system
cd helm-charts/nginx-ingress
helm upgrade --install nginx-ingress .
```

## Deploy model
```shell
kubectl create ns model-serving
kubens model-serving
cd helm-charts/model-deployment
helm upgrade --install news-summarization .
```

## Deploy Grafana
```shell
kubectl create ns monitoring
kubens nginx-monitoring
cd helm-charts/k8s-monitoring/kube-prometheus-stack
helm dependency build
cd helm-charts/k8s-monitoring
helm install -f kube-prometheus-stack.expanded.yaml kube-prometheus-stack kube-prometheus-stack -n monitoring
```
