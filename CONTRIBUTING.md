# Contribution Guidelines
1. Implement all features via RFCs in docs/rfc/
2. All commits must pass
   - Static analysis
   - Determinism testing
3. For memory changes:
   - Submit memory schema RFC first
   - Provide version migration plan
4. Testing:
   - Local: make test
   - Distributed: make test-cluster

## Good First Issues
Check https://github.com/your/repo/labels/good-first-issue