resource "google_firebaserules_ruleset" "this" {
  provider = google-beta
  project  = var.FIREBASE_PROJECT

  source {
    files {
      name    = "firestore.rules"
      content = file("${path.module}/firestore.rules")
    }
  }
}
