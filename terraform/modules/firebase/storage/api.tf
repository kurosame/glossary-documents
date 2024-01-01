resource "google_project_service" "this" {
  project = var.FIREBASE_PROJECT
  for_each = toset([
    "firebasestorage.googleapis.com"
  ])
  service                    = each.key
  disable_dependent_services = true
  disable_on_destroy         = true
}
