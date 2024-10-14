#gcp config
provider "google" {
  project = "amazing-jetty-429015-g8"
  region = "us-central1"
}

#cluster config
resource "google_container_cluster" "k8s_cluster" {
  name = "cluster-2"
  location = "us-central1-c"
  initial_node_count = 1

  node_config {
    machine_type = "e2-medium"
    disk_size_gb = 20
    disk_type = "pd-standard"
    image_type = "COS_CONTAINERD"
  }
}

#pv config
resource "google_compute_disk" "persistent_disk" {
  name = "volume-t"
  type = "pd-standard"
  zone = "us-central1-c" 
  size = 10
}