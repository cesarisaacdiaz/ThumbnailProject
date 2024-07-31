#!/bin/bash

# Variables
resourceGroup="myResourceGroup"
functionAppName="smallestPictures"
storageAccountName="mystorageaccount"
location="eastus"
pythonVersion="3.8"

# Crear un grupo de recursos
az group create --name $resourceGroup --location $location

# Crear una cuenta de almacenamiento
az storage account create --name $storageAccountName --location $location --resource-group $resourceGroup --sku Standard_LRS

# Crear una aplicación de funciones
az functionapp create \
  --resource-group $resourceGroup \
  --consumption-plan-location $location \
  --runtime python \
  --runtime-version $pythonVersion \
  --functions-version 3 \
  --name $functionAppName \
  --storage-account $storageAccountName
