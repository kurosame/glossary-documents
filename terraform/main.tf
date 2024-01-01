module "firebase_project" {
  source = "./modules/firebase/project"

  FIREBASE_PROJECT = var.FIREBASE_PROJECT
}

module "firebase_firestore" {
  source = "./modules/firebase/firestore"

  FIREBASE_PROJECT = var.FIREBASE_PROJECT
}

module "firebase_storage" {
  source = "./modules/firebase/storage"

  FIREBASE_PROJECT = var.FIREBASE_PROJECT
}
