terraform {
  cloud {
    organization = "kurosame"

    workspaces {
      name = "glossary"
    }
  }
}
