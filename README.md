# Glossary documents

The documents for [Glossary](https://github.com/kurosame/glossary)

## Setup for Terraform

1. Create a Firebase project from the console
   - https://console.firebase.google.com
   - A GCP service account for Firebase will be created
1. Generate a key for this service account and set it to the GOOGLE_CREDENTIALS environment variable in Terraform Cloud
1. Grant roles to this service account from the console
