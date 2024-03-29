# FastAPI-App mit Grafana- und Prometheus-Monitoring

Dieses Repository enthält eine FastAPI-Anwendung mit Grafana- und Prometheus-Monitoring. Die Projektdateien umfassen:

- `app.py`: Die Hauptdatei der FastAPI-Anwendung.
- `docker-compose.yml`: Die Konfigurationsdatei für Docker Compose, um die Anwendung und ihre Abhängigkeiten auszuführen.
- `Dockerfile`: Die Datei zum Erstellen des Docker-Images für die Anwendung.
- `prometheus.yml`: Die Konfigurationsdatei für Prometheus-Monitoring.
- `README.md`: Die Datei mit Informationen über das Repository.
- `requirements.txt`: Die Datei, die die Python-Abhängigkeiten der Anwendung auflistet.

Die FastAPI-Anwendung kann mithilfe von Docker Compose ausgeführt werden, indem folgender Befehl ausgeführt wird:


```bash
docker-compose up
```

Dies startet die Anwendung und ihre Abhängigkeiten, einschließlich Grafana und Prometheus für das Monitoring.

Die prometheus.yml-Datei ist so konfiguriert, dass sie die FastAPI-Anwendung überwacht und kann über den Webbrowser unter http://localhost:9090 aufgerufen werden.

Das Grafana-Dashboard kann über den Webbrowser unter http://localhost:3000 aufgerufen werden. Die Standard-Login-Daten lauten <strong>test</strong> als Benutzername und <strong>test</strong> als Passwort.

Sobald man eingeloggt ist, können Benutzer benutzerdefinierte Dashboards erstellen, um die von Prometheus gesammelten Daten zu visualisieren.

Zusätzlich enthält das Repository das fastapi-grafana.json File, welches das vorkonfigurierte Dashboard für die FastAPI-Anwendung enthält. Das Dashboard kann in Grafana importiert werden, um eine schnelle und einfache Übersicht über die Leistung der Anwendung zu erhalten.
Dieses kannst du in der Benutzeroberfläche als Dashboard importieren. Quelle ist: `https://github.com/Kludex/fastapi-prometheus-grafana/blob/master/fastapi-dashboard.json`
