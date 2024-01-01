resource "google_storage_bucket" "this" {
  provider                    = google-beta
  project                     = var.FIREBASE_PROJECT
  name                        = "glossary-documents"
  location                    = "ASIA"
  uniform_bucket_level_access = true
  public_access_prevention    = "enforced"
}

resource "google_firebase_storage_bucket" "this" {
  provider  = google-beta
  project   = var.FIREBASE_PROJECT
  bucket_id = google_storage_bucket.this.id
}
