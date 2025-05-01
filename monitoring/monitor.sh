#!/bin/bash
aws cloudwatch get-metric-statistics --namespace AWS/EC2 \
  --metric-name CPUUtilization --start-time $(date -u -d "5 minutes ago" +%Y-%m-%dT%H:%M:%SZ) \
  --end-time $(date -u +%Y-%m-%dT%H:%M:%SZ) --period 300 --statistics Average \
  --region us-east-1
