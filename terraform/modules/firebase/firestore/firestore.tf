resource "google_firestore_database" "this" {
  project                 = var.FIREBASE_PROJECT
  name                    = "(default)"
  location_id             = "asia-northeast1"
  type                    = "FIRESTORE_NATIVE"
  delete_protection_state = "DELETE_PROTECTION_ENABLED"
  deletion_policy         = "DELETE"
}
