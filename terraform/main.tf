provider "google" {
  project     = var.project_id
  region      = var.region
  credentials = file(var.credentials)
}

resource "google_storage_bucket" "bronze" {
  name     = "bronze-${var.project_id}"
  location = var.region
}

resource "google_storage_bucket" "silver" {
  name     = "silver-${var.project_id}"
  location = var.region
}

resource "google_storage_bucket" "gold" {
  name     = "gold-${var.project_id}"
  location = var.region
}

resource "google_bigquery_dataset" "silver" {
  dataset_id = "silver_dataset"
  location   = var.region
}
resource "google_bigquery_dataset" "gold" {
  dataset_id = "gold_dataset_1"
  location   = var.region
}