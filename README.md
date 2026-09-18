# AI Healthcare Workload Guard

Application reference for Triomics’ Bengaluru DevOps/SRE role. The executable admission policy blocks a production workload unless it uses an immutable image, preserves tenant isolation, scopes data access, has recovery readiness, and reports healthy workloads.

This maps the role’s Kubernetes, Terraform/Helm, cloud, security, AI/ML, single-tenant, and incident-readiness needs into a testable boundary. In production, a deployment controller would source these fields from GitOps metadata, IAM policy, backup verification, and Kubernetes health, then record the decision for audit and incident response.

```bash
python3 -m unittest discover -s tests -v
python3 -m src.app < examples/workloads.jsonl
```

The JSONL interface makes the admission decision consumable by a GitOps
pipeline. The sample demonstrates both an admissible workload and a blocked
workload with audit-friendly reasons.

This is illustrative and does not claim access to Triomics systems or patient data.

## Candidate links
- https://www.linkedin.com/in/rahul-h-bhatia/
- https://rahulhbhatia.vercel.app
- https://www.credly.com/users/rahul-h-bhatia/badges
