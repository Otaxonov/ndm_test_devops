# Architecture

Client → nginx1 → nginx2 → nginx3 → Flask app

---

# Run

## 1. Build and start all services

docker-compose up --build

## 2. Access entry point

http://localhost:8081

---

# Testing

## Normal request

curl http://localhost:8081

Expected output:

X-Forwarded-For: client-ip, nginx1, nginx2, nginx3

---

## Spoofing attempt

curl -H "X-Forwarded-For: 1.1.1.1,2.2.2.2" http://localhost:8081

Expected result:
- spoofed IP MUST NOT appear
- only real proxy chain is preserved