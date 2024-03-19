// Variables to use accross the project
// which can be accessed by var.project_id
variable "project_id" {
  description = "The project ID to host the cluster in"
  default     = "trim-artifact-412211"
}

variable "region" {
  description = "The region the cluster in"
  default     = "asia-southeast1"
}

variable "zone" {
  description = "The region the cluster in"
  default     = "asia-southeast1-b"
}
