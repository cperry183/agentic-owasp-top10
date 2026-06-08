# OWASP Top 10 Assessment Checklist

## A01 Broken Access Control
- [ ] Review role mappings
- [ ] Verify object-level authorization
- [ ] Review administrative endpoints

## A02 Cryptographic Failures
- [ ] TLS configuration
- [ ] Secret management
- [ ] Password storage review

## A03 Injection
- [ ] Input validation review
- [ ] Parameterized query verification

## A04 Insecure Design
- [ ] Threat model available
- [ ] Security requirements documented

## A05 Security Misconfiguration
- [ ] Default credentials removed
- [ ] Debug interfaces disabled

## A06 Vulnerable Components
- [ ] SBOM generated
- [ ] Dependency scan completed

## A07 Authentication Failures
- [ ] MFA reviewed
- [ ] Session timeout validated

## A08 Software and Data Integrity
- [ ] Build pipeline reviewed
- [ ] Artifact signing verified

## A09 Logging and Monitoring
- [ ] Audit logs enabled
- [ ] Alerting configured

## A10 SSRF
- [ ] Outbound network restrictions
- [ ] URL validation controls
