terraform {
  required_version = "1.6.6"

  cloud {
    organization = "kurosame"

    workspaces {
      name = "glossary"
    }
  }

  required_providers {
    google-beta = {
      source  = "hashicorp/google-beta"
      version = "5.10.0"
    }
  }
}

provider "google-beta" {
  region = "asia-northeast1"
}
