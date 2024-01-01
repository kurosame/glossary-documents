resource "google_firebase_web_app" "this" {
  provider        = google-beta
  project         = var.FIREBASE_PROJECT
  display_name    = "Glossary"
  deletion_policy = "DELETE"
}

data "google_firebase_web_app_config" "this" {
  provider   = google-beta
  project    = var.FIREBASE_PROJECT
  web_app_id = google_firebase_web_app.this.app_id
}
